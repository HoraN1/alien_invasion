import sys
import pygame
from bullet import Bullet


def check_keydown(event, game_settings, screen, ship, bullets):
    """
    Check keydown event
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add into Group
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup(event, ship):
    """
    Check key up event
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(game_settings, screen, ship, bullets):
    """
    Check the response from keyboard and mouse
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(game_settings, screen, ship, bullets):
    """
    Update surfaces on screen
    """
    # Redraw the screen per loop
    screen.fill(game_settings.bg_color)
    ship.blit_me()

    # Redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Display the screen
    pygame.display.flip()
