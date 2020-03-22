import sys
import pygame


def check_events(ship):
    """
    Check the response from keyboard and mouse
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.rect.centerx += 1


def update_screen(game_settings, screen, ship):
    """
    Update surfaces on screen
    :param game_settings:
    :param screen:
    :param ship:
    :return:
    """
    # Redraw the screen per loop
    screen.fill(game_settings.bg_color)
    ship.blit_me()
    # Display the screen
    pygame.display.flip()
