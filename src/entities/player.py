import pygame

class Player(pygame.Rect):
    life = 0
    alive = life > 0
    speed = 5

    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.life = 100

    def move(self):
        # key is not being pressed
        self.center = (
            self.centerx,
            self.centery
        )

        # vertical movement
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.centery -= self.speed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.centery += self.speed

        # horizontal movement
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.centerx -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.centerx += self.speed
