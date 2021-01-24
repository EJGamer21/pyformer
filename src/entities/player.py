import math, sys
import pygame as pg
from pygame import sprite
from constants import *

# ----------------------------------- #
#  CONSTANTS
# ----------------------------------- #
SPEED = 10
MAX_JUMP_HEIGHT = 50

# ----------------------------------- #

class Player(sprite.Sprite):
    life: float = 10.0
    speed: float = 3

    momentum = { 'x': 0, 'y': 0 }
    remaining_jumps = 1

    def __init__(self, pos: tuple[int, int], size: tuple[int, int]):
        super().__init__()

        self.image = pg.Surface(size)
        self.image.fill(COLORS['primary'])

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.fall()
        self.move_around()

    def fall(self, speed: int = None):
        _speed = (speed
            if speed is not None
            else SPEED)

        self.rect.y += _speed + (_speed * GRAVITY)

    def move_around(self):
        # get active keys
        keys = pg.key.get_pressed()

        # vertical movement
        if keys[pg.K_UP] == 1 and self.remaining_jumps > 0:
            jump_v = math.sqrt(2 * SPEED * abs(GRAVITY))
            self.momentum['y'] -= SPEED + jump_v
            self.rect.centery += self.momentum['y']

            self.remaining_jumps = 0

        elif keys[pg.K_UP] == 0 and self.remaining_jumps <= 0:
            if self.momentum['y'] <= 0.0:
                self.momentum['y'] += SPEED * GRAVITY
                self.rect.centery -= self.momentum['y']
            else:
                self.remaining_jumps = 1
                self.momentum['y'] = 0

        if keys[pg.K_DOWN]:
            self.rect.centery += SPEED + (SPEED * GRAVITY)

        # horizontal movement
        if keys[pg.K_LEFT]:
            self.rect.centerx -= SPEED * -0.12

        if keys[pg.K_RIGHT]:
            self.rect.centerx += SPEED * -0.12

    def recieve_damage(self, damage: float) -> float:
        self.life -= damage
        return self.life

    def has_collided_with(self, object: sprite.Sprite) -> bool:
        return self.rect.colliderect(object)

    def is_alive(self) -> bool:
        return self.life > 0.0
