import random
import sys

import pygame
from pygame import SurfaceType, Surface, Rect
# from pygame.examples.go_over_there import clock
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode  # game_mode irá receber o return do menu_option
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')  # adicionando o Player1
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL  # 20 seg
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')  # adicionando o Player1
            player.score = player_score[1]
            self.entity_list.append(player)
            # self.entity_list.append(EntityFactory.get_entity('Player2'))  # adicionando o Player2
        # utilizando o conceito de "eventos", vamos instanciar os inimigos a cada xis tempo:
        pygame.time.set_timer(EVENT_ENEMY,
                              SPAWN_TIME)  # evento a cada 2 seg para gerar o inimigo através de um if no level.py no run

        # criando condicao de vitoris
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # CHECAGEM CONDICAO DE VITORIA

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # incluida musica no lvl1 (importada)
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)  # rodando a mũsica indefinidamente
        clock = pygame.time.Clock()  # incluído um clock para rodar em um fps padrão
        while True:
            clock.tick(60)  # qtos fps irá utilizar no clock
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))

            for event in pygame.event.get():  # inclusao de gerenciado de eventos
                if event.type == pygame.QUIT:  # para poder fechar a janela qndo no lvl 1
                    pygame.quit()
                    sys.exit()  # = o quit
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:  # checa se o event time acontece
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # Incluindo textos de level referentes ao método level_text criado mais abaixo
            # aqui teremos os textos que aparecem na tela do level1 que será no canto superior esquerdo Timeout
            # no canto interior esquerdo texto e valor de FPS e texto e valor de Entidades
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # verificar as colisões entre player e enemy
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
