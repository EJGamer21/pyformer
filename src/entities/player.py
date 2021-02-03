import pygame as pg
from pygame import Vector2, sprite
from constants import *
from lib.functions import calculate_motion

# ----------------------------------- #
#  CONSTANTS
# ----------------------------------- #
SPEED = 10
MAX_JUMP_HEIGHT = 50
FRICTION = -0.10

# ----------------------------------- #

class Player(sprite.Sprite):
    health: float = 10.0

    velocity, acceleration = Vector2(0, 0), Vector2(0, GRAVITY)
    remaining_jumps = 1
    is_jumping, is_on_ground = False, False

    def __init__(self, pos: tuple[int, int], size: tuple[int, int]):
        super().__init__()

        self.position = Vector2(pos)

        self.image = pg.Surface(size)
        self.image.fill(COLORS['primary'])

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self, delta):
        self.movement(delta)

    def movement(self, delta):
        self.limit_velocity(SPEED)
        self.vertical_movement(delta)
        self.horizontal_movement(delta)

    def vertical_movement(self, delta):
        self.velocity.y += self.acceleration.y * delta

        if self.is_on_ground is False:
            self.fall(delta)
        else:
            self.velocity.y = 0

        self.rect.bottom = self.position.y

    def jump(self):
        if self.is_on_ground:
            self.is_jumping = True
            self.velocity.y -= SPEED
            self.is_on_ground = False

    def fall(self, delta):
        self.position.y += calculate_motion(self, 'y', delta)

    def horizontal_movement(self, delta):
        keys = pg.key.get_pressed()

        self.acceleration.x = 0
        if keys[pg.K_LEFT]:
            self.acceleration.x -= 0.3
        if keys[pg.K_RIGHT]:
            self.acceleration.x += 0.3

        self.acceleration.x += self.velocity.x * FRICTION

        self.velocity.x += self.acceleration.x * delta
        self.position.x += calculate_motion(self, 'x', delta)

        self.rect.x = self.position.x

    def limit_velocity(self, max_velocity):
        min(-max_velocity, max(self.velocity.x, max_velocity))
        min(-max_velocity, max(self.velocity.y, max_velocity))

        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0

        if self.velocity.y > SPEED:
            self.velocity.y = SPEED

    def recieve_damage(self, damage: float) -> float:
        self.health -= damage
        return self.health

    def has_collided_with(self, object: sprite.Sprite) -> bool:
        return self.rect.colliderect(object)

    def is_alive(self) -> bool:
        return self.health > 0.0
