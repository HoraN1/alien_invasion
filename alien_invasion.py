import sys
import pygame


def run_game():
    # Initialize a game screen
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # Start the game main loop
    while True:
        # Check for keys and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(bg_color)
            # Display the screen
            pygame.display.flip()


run_game()
