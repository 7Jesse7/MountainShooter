import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Criando a janela
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Initialize a window or screen for display

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()



