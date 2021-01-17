import pygame
from entities.player import Player
from game_manager import GameManager
from config import colors

window_title = 'Main screen'
game_manager = GameManager()

SCREEN_SIZE=(980, 640)
FPS = 60

screen = game_manager.init_screen(window_title, SCREEN_SIZE)
player = Player((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), (50, 50))




is_running = True
while is_running:
    screen.fill(colors.background['rgb'])

    pygame.draw.rect(screen, colors.primary['rgb'], player)

    player.move()

    game_manager.update_screen()
    game_manager.check_quit()
    game_manager.tick(FPS)






if is_running is False:
    game_manager.quit()
