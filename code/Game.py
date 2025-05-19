import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        # Criando a janela
        self.window = pygame.display.set_mode(size=(600, 480))  # Initialize a window or screen for display

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            # check for all events https://www.pygame.org/docs/ref/event.html
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        print('Quitting...')
            #        pygame.quit()  # Close Window
            #        quit()  # Encerrar --  end pygame

        #
