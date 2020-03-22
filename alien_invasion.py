import sys
import pygame
from settings import Settings


def run_game():
    # Initialize a game screen
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Start the game main loop
    while True:
        # Check for keys and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(game_settings.bg_color)
            # Display the screen
            pygame.display.flip()


run_game()
