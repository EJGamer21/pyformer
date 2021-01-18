import pygame as pg
from entities.box import Box
from entities.player import Player
from game_manager import GameManager
from config import colors

window_title = 'Main screen'
game_manager = GameManager()

# ----------------------------------- #
#  CONSTANTS
# ----------------------------------- #
SCREEN_SIZE=(980, 640)
FPS = 30

# ----------------------------------- #

screen = game_manager.init_screen(window_title, SCREEN_SIZE)

entities = []
player = Player((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), (10, 10))
obj = Player((player.x - 30, player.centery + 30), (100, 10))

enemies: list[Box] = [
    Box((player.centerx + 30, player.centery + 30), (20, 20))
]


while True:
    screen.fill(colors.background['rgb'])

    if player.is_alive() is False:
        game_manager.quit('Game Over!!')

    pg.draw.rect(screen, colors.primary['rgb'], player)
    pg.draw.rect(screen, colors.secondary['rgb'], obj)

    for enemy in enemies:
        pg.draw.rect(screen, colors.secondary['rgb'], enemy)

        if enemy.colliderect(player):
            enemy.attack(player)

    if player.has_collided(obj):
        player.bottomleft = obj.topleft

    player.update()

    game_manager.update_screen()
    game_manager.check_quit()
    game_manager.tick(FPS)
