import pygame
import game_functions as g_func
from settings import Settings
from ship import Ship
from pygame.sprite import Group


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
    ship = Ship(game_settings, screen)

    # Create a Bullet Group
    bullets = Group()

    # Start the game main loop
    while True:
        # Check for keys and mouse event
        g_func.check_events(game_settings, screen, ship, bullets)
        # Update ship states according to event
        ship.update()
        bullets.update()
        # Delete bullet if exceeding the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        g_func.update_screen(game_settings, screen, ship, bullets)


run_game()
