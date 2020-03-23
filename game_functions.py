import sys
import pygame
from bullet import Bullet


def fire_bullet(game_settings, screen, ship, bullets):
    """
    If not over the bullet limit, add one to the firing group
    """
    # Create a new bullet and add into Group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown(event, game_settings, screen, ship, bullets):
    """
    Check keydown event
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


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


def update_bullets(bullets):
    """
    Update the position of bullet and delete those are out of screen
    """
    # Update the position
    bullets.update()
    # Delete bullet if exceeding the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
