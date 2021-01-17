from game_manager import GameManager

window_title = 'Main screen'
game_manager = GameManager()

screen = game_manager.init_screen(window_title, screen_size=(980, 640))

is_running = True
while is_running:
    game_manager.check_quit()

if is_running is False:
    game_manager.quit()