import pygame

class Box(pygame.Rect):
    alive = False

    def __init__(self, pos, size) -> None:
        super().__init__(pos, size)
        self.alive = True

    def attack(self, enemy: pygame.Rect):
        print('attacking enemy:', enemy.center)
