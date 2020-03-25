import sys
import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


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


def update_screen(game_settings, screen, ship, alien, bullets):
    """
    Update surfaces on screen
    """
    # Redraw the screen per loop
    screen.fill(game_settings.bg_color)

    # Redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blit_me()
    alien.draw(screen)

    pygame.display.flip()


def update_bullets(game_settings, screen, ship, aliens, bullets):
    """
    Update the position of bullet and delete those are out of screen
    """
    # Update the position
    bullets.update()
    # Delete bullet if exceeding the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collision(game_settings, screen, ship, aliens, bullets):
    """
    Check if the bullet hit the alien
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(game_settings, screen, ship, aliens)


def check_fleet_edges(game_settings, aliens):
    """
    Move another way if the aliens are at the edge
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """
    Move the aliens down and change direction
    """
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def update_aliens(game_settings, aliens):
    """
    Update aliens positions
    """
    check_fleet_edges(game_settings, aliens)
    aliens.update()


def get_number_aliens(game_settings, alien_width):
    """
    Calculate numbers of aliens each line
    """
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(game_settings, ship_height, alien_height):
    """
    Calculate how mane rows of aliens can be obtained
    """
    available_space_y = (game_settings.screen_height - (5 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """
    Create one alien to determine the amount
    """
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    """
    Create a group of aliens
    """
    alien = Alien(game_settings, screen)
    number_alien_x = get_number_aliens(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    # Create first line of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)
