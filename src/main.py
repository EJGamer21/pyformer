# --------- IMPORTS --------- #
import pygame as pg
from constants import *

from pygame import sprite
from core.game import Game

from entities.player import Player
from entities.platform import Platform

# --------------------------- #

player_sprite = Player((WIDTH/2, HEIGHT/2), (20, 20))
player = sprite.GroupSingle(player_sprite)

platforms = sprite.Group(
    Platform((WIDTH/2, 620), (WIDTH/2, 40))
)

all_sprites = sprite.Group(
    player,
    platforms
)

game = Game()
keys = []
while game.is_running:
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        player.sprite.jump()
    else:
        # player_sprite.velocity.y *= .25
        player_sprite.is_jumping = False

    # if player is not alive, is game over. End game.
    if player.sprite.is_alive() is not True:
        game.quit('Game Over!!')

    # fill the screen with background
    game.screen.fill(COLORS['background'])

    # draw all sprites onto screen
    game.draw(all_sprites)

    # check if player hits a platform
    collision = sprite.spritecollideany(player_sprite, platforms)
    if collision:
        player_sprite.is_on_ground = True
        player_sprite.position.y = collision.rect.top
    else:
        player_sprite.is_on_ground = False

    if player_sprite.position.y > HEIGHT:
        player_sprite.position.y = 0

    # Update game every game loop
    game.update()

game.quit()
