import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # só carrega o som
        pygame.mixer_music.play(-1)  # Toca o som carregado no load, e parametro -1 para tocar indefindamente

        while True:  # loop infinto fazendo o desenho da imagem e checagem, do evento para quando usuário clica e fechar
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)  # criando o retangulo onde ficará a imagem
            self.menu_text(50, "Mountain", C_WHITE,
                           ((WIN_WIDTH / 2), 70))  # escrevendo o texto sobre a imagem do retangulo criada acima
            self.menu_text(50, "Shooter", C_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # check for all events (fechar, minimizar, etc..) https://www.pygame.org/docs/ref/event.html
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()  # Close Window
                    quit()  # Encerrar --  end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
