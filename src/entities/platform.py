import pygame as pg
from pygame.locals import *

from constants import *

class Platform(pg.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], size: tuple[int, int]):
        super().__init__()

        self.image = pg.Surface(size)
        self.image.fill(COLORS['secondary'])

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass
