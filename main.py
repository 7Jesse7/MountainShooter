import pygame

print('Setup Start')
pygame.init()


# Criando a janela
window = pygame.display.set_mode(size=(600,480)) #Initialize a window or screen for display

print('Setup End')
while True:
    # check for all events https://www.pygame.org/docs/ref/event.html
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close Window
            quit() # Encerrar --  end pygame

#
