import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        # Criando a janela
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Initialize a window or screen for display

    def run(self): #loop que chama o Menu.py
        while True:
            menu = Menu(self.window)
            #menu.run()
            menu_return = menu.run() # recebe o return lá do menu e coloca na variável menu_return. A partir desse returno do Menu, podemos inciar alguma ação

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: # aqui vamos iniciar a acção de entrar no lvel
                level = Level(self.window, 'Level 1', menu_return) # inicializa o objeto//construtor da classe level
                                        #passando a janela como parâmetro (self.window)
                                        #um nome 'level1' e também uma possibilidade de opções de jogo menu_return
                level_return = level.run() #para iniciar a execução da level

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # Encerrar --  end pygame
            else:
                pass





#precisamos prepara o Game.py para receber o return do Menu.py
