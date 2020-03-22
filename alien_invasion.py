import sys
import pygame
from settings import Settings
from ship import Ship


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Redraw the screen per loop
            screen.fill(game_settings.bg_color)
            ship.blit_me()
            # Display the screen
            pygame.display.flip()


run_game()
