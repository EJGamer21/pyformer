import pygame

from entities.player import Player

class Box(pygame.Rect):
    life: float = 0.0
    alive: bool = life > 0.0
    damage: float = 0.10

    def __init__(self, pos: tuple, size: tuple) -> None:
        super().__init__(pos, size)
        self.life = 100

    def attack(self, enemy: Player):
        enemy.recieve_damage(self.damage)
        print('attacking enemy, remaining life:', enemy.health)
