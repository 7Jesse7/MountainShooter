import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() #convert_alpha trata transparÊncias das imagens
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        menu_option= 0

        pygame.mixer_music.load('./asset/Menu.mp3')  # só carrega o som
        pygame.mixer_music.play(-1)  # Toca o som carregado no load, e parametro -1 para tocar indefindamente

        while True:  # loop infinto fazendo o desenho da imagem e checagem, do evento para quando usuário clica e fechar
            # DRAW IMAGES (desenho das imagens):
            self.window.blit(source=self.surf, dest=self.rect)  # criando o retangulo onde ficará a imagem
            self.menu_text(50, "Mountain", C_ORANGE,
                           ((WIN_WIDTH / 2), 70))  # escrevendo o texto sobre a imagem do retangulo criada acima
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()
            #criada as cores no for i in range, agora precisamos criar as setas para navegar entre as opções
            #para isso, precisamos utilizar os eventos



            # check for all events (fechar, minimizar, etc..) https://www.pygame.org/docs/ref/event.html
            # daqui para baixo é checagem de evento das teclas
            for event in pygame.event.get(): #pega todos os eventos que estão na fila
                if event.type == pygame.QUIT:
                    print('Quitting...')
                    pygame.quit()  # Close Window
                    quit()  # Encerrar --  end pygame
                    # o código acima executa o evento de fechar a janela. Agora vamos buscar o evento de navegar na biblioteca pygame.event
                # para a parte de navegar KEYDOWN/KEYUP, precisamos codar dentro deste mesmo loop de eventos
                if event.type == pygame.KEYDOWN: # se o evento for pressionar a tecla (KEYDOWN) - OBS: KEYUP seria soltar a tecla
                    if event.key == pygame.K_DOWN: # verifica se a tecla é igual a seta para baixo
                        #menu_option += 1  se a tecla foi pressionada, incrementamos 1 no menu_option para fazer a cor descer
                        #porém precisamos colocar um delimitador para quando passar da posição 5 (são 5 itens no MENU_OPTION, cfe
                        #pode ser visto na const.py
                        if menu_option < len(MENU_OPTION) - 1: #se as cores do menu_option forem menor que o tamanho (quantidade) da const MENU_OPTION - 1
                            menu_option += 1 # incrementa 1
                        else: # se não, se for maior que o tamanho da tupla MENU_OPTION, então reseta
                            menu_option = 0 # reset
                    #agora o processo inverso, ou seja, pressionar a tecla para cima
                    if event.key == pygame.K_UP: # verifica se a tecla é igual a seta para cima
                        #menu_option -= 1  se a tecla foi pressionada, decrementamos 1 no menu_option para fazer a cor subir
                        #porém precisamos colocar um delimitador para quando passar da posição 0
                        #voltar para a útlima posição da tupla
                        if menu_option > 0: #se as cores do menu_option for maior que a primeira posição da tupla MENU_OPTION que é 0
                            menu_option -= 1 #decrementa 1
                        else: # se não, se for menor que a posição inicial (0) da tupla MENU_OPTION, então reseta para a última posição
                            menu_option = len(MENU_OPTION) - 1 # reset end position
                    #criando agora o evento para "acionar" o menu selecionado
                    if event.key == pygame.K_RETURN: #isso indica que se for pressionada a telca ENTER (ingles RETURN) ocorrerá o comando abaixo
                        return MENU_OPTION[menu_option]# return encerra o metodo run() atual que está inserido esse if
                                # se adicionarmos após o return algo, ele retornará o que foi adicionado
                                # como add ao return o MENU_OPTION[menu_option] ele encerra o loop do run e em seguida já reinicia o método
                                #iremoa alterar posteriormente para voltar (return) para um level (ir para um lugar)
                                # o return daqui volta para o Game.py que tem um loop que faz voltar para o Menu.py (def run(self): #loop que chama o Menu.py)




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
