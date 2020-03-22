import pygame
from settings import Settings
from ship import Ship
import game_functions as g_func


def run_game():
    """
    Initialize a game screen
    :return: None
    """
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a ship
    ship = Ship(screen)

    # Start the game main loop
    while True:
        # Check for keys and mouse event
        g_func.check_events(ship)
        ship.update()
        g_func.update_screen(game_settings, screen, ship)


run_game()
