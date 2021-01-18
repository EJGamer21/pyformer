import pygame as pg

from config.physics import GRAVITY

# ----------------------------------- #
#  CONSTANTS
# ----------------------------------- #
SPEED = 10
MAX_JUMP_HEIGHT = 50

# ----------------------------------- #

class Player(pg.Rect):
    def __init__(self, pos: tuple, size: tuple):
        super().__init__(pos, size)
        self.life: float = 10.0
        self.speed: float = 5
        self.momentum = { 'x': 0, 'y': 0 }

    def update(self):
        self.move_around()

    def move_around(self):
        # get active keys
        keys = pg.key.get_pressed()

        # vertical movement
        if (keys[pg.K_UP] == 1 and self.momentum['y'] <= MAX_JUMP_HEIGHT):
                self.momentum['y'] += SPEED*GRAVITY
                self.centery -= SPEED*GRAVITY

        if keys[pg.K_UP] == 0:
            if self.momentum['y'] > 0.0:
                self.momentum['y'] -= SPEED*GRAVITY
                self.centery += SPEED*GRAVITY
            if self.momentum['y'] < 0:
                self.momentum['y'] = 0

        if keys[pg.K_DOWN]:
            self.centery += SPEED + SPEED*GRAVITY

        # horizontal movement
        if keys[pg.K_LEFT]:
            self.centerx -= SPEED

        if keys[pg.K_RIGHT]:
            self.centerx += SPEED

    def recieve_damage(self, damage: float) -> float:
        self.life -= damage
        return self.life

    def has_collided(self, object) -> bool:
        return self.colliderect(object)

    def is_alive(self) -> bool:
        return self.life > 0.0
