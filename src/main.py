# --------- IMPORTS --------- #
from constants import *

from pygame import sprite
from core.game import Game

from entities.player import Player
from entities.platform import Platform

# --------------------------- #

player_sprite = Player((WIDTH/2, HEIGHT/2), (10, 10))
player = sprite.GroupSingle(player_sprite)

platforms = sprite.Group(
    Platform((0, 600), (WIDTH, 40))
)

all_sprites = sprite.Group(
    player,
    platforms
)

game = Game()
while game.is_running:
    # if player is not alive, is game over. End game.
    if player.sprite.is_alive() is not True:
        game.quit('Game Over!!')

    # fill the screen with background
    game.screen.fill(COLORS['background'])

    # draw all sprites onto screen
    game.draw(all_sprites)

    # Update game every game loop
    game.update()

game.quit()
