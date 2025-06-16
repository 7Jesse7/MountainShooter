import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple): #player terá um nome (name) que será str e uma position que é uma tupla
        super().__init__(name, position) # isso (name e position) herda da super classe
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed() # get_pressed é para enquanto a tecla estiver pressionada fazer algo
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0: #se a tecla pressionada for seta para cima (K_UP)
            self.rect.centery -= ENTITY_SPEED[self.name] #então o objeto do player (self) se movimenta. O objeto se movimento
                                    # mexendo-se no retangulo (rect) dele
                                    # e o centery mexe no eixo y, reduzindo conforme Const.py ENTITY_SPEED para o Player1, pois o top é igual a 0
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT: #se a tecla pressionada for seta para cima (K_DOWN) irá até o bot da imagem
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0: #se a tecla pressionada for seta para cima (K_UP)
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH: #se a tecla pressionada for seta para cima (K_UP)
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self): #metodo para player atirar
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery)) #instanciando o tiro dentro do player
            else:
                return None
        else:
            return None
