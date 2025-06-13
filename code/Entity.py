from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC): #ABC para indicar que é uma classe ABSTRATA, que irá gerar o Background o player e o inimigo
    def __init__(self, name: str, position: tuple): #sempre que inicializa um objeto entity,
                            # fornecemos com parametro um nome (string) e uma posição que será uma tupla
                            # que será a posição onde o objeto que será uma imagem deve aparecer na tela
        self.name = name

        #msm procedimento para carregar as imagens:
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha() #convert_alpha faz um tratamento das transparências das imagens .png
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod #decorator @ para indicar ao pythpn que o
                    #somente pelos seus filhos e não pela class Entry abstrata
    def move(self, ):
        pass