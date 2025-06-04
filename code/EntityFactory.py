import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:   #para ser invocada no level.py e então
                    #gerar os backgrounds, os player e os enemies

    #def __init__(self): #Não há init no EntityFactory - não se usa essa class para
    #    pass
                    #    #instanciar um objeto
                         #EntityFactory de acordo com  Design Patter sempre
                         # irá invocar outros objetos que serão instanciados

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)): # terá um entity_name e uma posição ((0,0) quando background)
        match entity_name: #match case
            case 'Level1Bg': #se o nome da entidade  que vier for Level1Bg
                list_bg = [] #pega todos os background e carrega todos dentro de 1 lista vazia
                            # e faz um loop juntando todos os Bgs dentro da lista que estava vazia
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))) #win_weight + 10 faz vir de fora da tela
            case 'Enemy2':                                                                 #random.randit biblioteca que posiciona randomicamente/aleatoriamente os inimigos
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))

        return None