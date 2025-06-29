import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE
from code.DbProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load(
            './asset/ScoreBg.png').convert_alpha()  # convert_alpha trata transparÊncias das imagens
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')  # só carrega o som
        pygame.mixer_music.play(-1)  # Toca o som carregado no load, e parametro -1 para tocar indefindamente
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'You Win!!', C_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player 1 name(4 characters):'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter TEAM name(4 characters):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name(4 characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name(4 characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():  # inclusao de gerenciado de eventos
                if event.type == pygame.QUIT:  # para poder fechar a janela qndo no lvl 1
                    pygame.quit()
                    sys.exit()  # = o quit
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show(game_mode, player_score)
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self, menu_return, player_score):
        pygame.mixer_music.load('./asset/Score.mp3')  # só carrega o som
        pygame.mixer_music.play(-1)  # Toca o som carregado no load, e parametro -1 para tocar indefindamente
        self.window.blit(source=self.surf, dest=self.rect)
        screen_width = self.window.get_width()  # Obtém a largura da tela IA
        base_x = screen_width // 2  # Define o centro da tela IA

        #self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        #self.score_text(20, 'NAME            SCORE                           DATE', C_YELLOW, SCORE_POS['Label'])
        self.score_text(32, 'TOP 10 SCORE', C_YELLOW, (base_x, SCORE_POS['Title'][1]))  # IA Centraliza título
        #self.score_text(16, 'NAME        SCORE       DATE', C_YELLOW, #IA
        #                (base_x, SCORE_POS['Label'][1]))  # Centraliza cabeçalhos
        self.score_text(16, 'NAME', C_YELLOW, (base_x - 100, SCORE_POS['Label'][1]))  # Nome alinhado corretamente
        self.score_text(16, 'SCORE', C_YELLOW, (base_x, SCORE_POS['Label'][1]))  # Score centralizado
        self.score_text(16, 'DATE', C_YELLOW, (base_x + 100, SCORE_POS['Label'][1]))  # Data corretamente posicionada

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            #self.score_text(20,f'        {name}               {score:05d}                       {date}',
            #                C_YELLOW, SCORE_POS[list_score.index(player_score)])
            for i, player_score in enumerate(list_score):
                id_, name, score, date = player_score
                y_offset = SCORE_POS['Label'][1] + 20 * (i + 1)  # Ajusta posição vertical

                # Nome à esquerda, Score centralizado, Data à direita
                self.score_text(20, name, C_YELLOW, (base_x - 100, y_offset))  # Nome alinhado com o título NAME
                self.score_text(20, f'{score:05d}', C_YELLOW, (base_x, y_offset))  # Score centralizado
                self.score_text(20, date, C_YELLOW, (base_x + 175, y_offset))  #
        while True:
            for event in pygame.event.get():  # inclusao de gerenciado de eventos
                if event.type == pygame.QUIT:  # para poder fechar a janela qndo no lvl 1
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Courier New", size=text_size) #IA
        #text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
