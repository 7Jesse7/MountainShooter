from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):  # player terá um nome (name) que será str e uma position que é uma tupla
        super().__init__(name, position)  # isso (name e position) herda da super classe

    def move(self,):
        self.rect.centerx -= ENTITY_SPEED[self.name]
