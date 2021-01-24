import pygame as pg
from pygame.sprite import *
from constants import *
import sys

class Game():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)

        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SCALED)
        self.clock = pg.time.Clock()
        self.is_running = True

    # Main game loop
    def update(self):
        if self.is_running is not True:
            self.quit('Game is not running anymore.')

        self.events()
        pg.display.flip()
        self.clock.tick(FPS)

    def draw(self, sprites: AbstractGroup):
        sprites.draw(self.screen)
        sprites.update()

    def events(self):
        for event in pg.event.get():
            self.verify_quit(event)

    def verify_quit(self, event):
        if (event.type == pg.QUIT
            or (event.type == pg.KEYUP
                and event.key == pg.K_ESCAPE)):
            self.quit()

    def quit(self, message: str = None):
        print('Game has finished.')
        if message is not None:
            print('message:', message)

        self.is_running = False

        pg.quit()
        sys.exit()
