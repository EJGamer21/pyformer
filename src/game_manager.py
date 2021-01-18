import pygame as pg
import sys

class GameManager():
    clock = None

    def __init__(self):
        pg.init()

    def init_screen(self, title: str, size: tuple[int, int]) -> pg.Surface:
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()

        return pg.display.set_mode(size)

    def update_screen(self):
        pg.display.update()

    def quit(self, message: str = None):
        print('Game has finished.')
        if message is not None:
            print('message:', message)

        pg.quit()
        sys.exit()

    def tick(self, fps: float):
        self.clock.tick(fps)


    def check_quit(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT
                or (event.type == pg.KEYUP
                    and event.key == pg.K_ESCAPE)):
                quit()
