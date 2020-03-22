import sys
import pygame


def check_keydown(event, ship):
    """
    Check keydown event
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup(event, ship):
    """
    Check key up event
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """
    Check the response from keyboard and mouse
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(game_settings, screen, ship):
    """
    Update surfaces on screen
    """
    # Redraw the screen per loop
    screen.fill(game_settings.bg_color)
    ship.blit_me()
    # Display the screen
    pygame.display.flip()
