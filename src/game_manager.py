import pygame
import sys

class GameManager():
    clock = None

    def __init__(self):
        pygame.init()

    def init_screen(self, title, screen_size) -> pygame.Surface:
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        return pygame.display.set_mode(screen_size)

    def update_screen(self):
        pygame.display.update()

    def quit(self):
        pygame.quit()
        sys.exit()

    def tick(self, fps):
        self.clock.tick(fps)


    def check_quit(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT
            or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)):
                quit()
