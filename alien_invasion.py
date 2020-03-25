import pygame
import game_functions as g_func

from ship import Ship
from alien import Alien
from settings import Settings
from pygame.sprite import Group


def run_game():
    """
    Initialize a game screen
    """
    # Game screen setup
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a ship, alien and bullet
    ship = Ship(game_settings, screen)
    alien = Alien(game_settings, screen)
    bullets = Group()

    # Start the game main loop: check keyboard and mouse event, update ship, update bullet and screen
    while True:
        g_func.check_events(game_settings, screen, ship, bullets)
        ship.update()
        g_func.update_bullets(bullets)
        g_func.update_screen(game_settings, screen, ship, alien, bullets)


run_game()
