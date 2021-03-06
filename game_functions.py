import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def start_game(game_settings, stats, score_board, screen, ship, aliens, bullets):
    stats.reset_stats()
    stats.game_active = True
    pygame.mouse.set_visible(False)

    # Reset score board, settings, aliens and bullets groups
    score_board.prep_score()
    score_board.prep_level()
    score_board.prep_ships()
    game_settings.initialize_settings()
    game_initialize(game_settings, screen, ship, aliens, bullets)


def fire_bullet(game_settings, screen, ship, bullets):
    """
    If not over the bullet limit, add one to the firing group
    """
    # Create a new bullet and add into Group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown(event, game_settings, stats, score_board, screen, ship, aliens, bullets):
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
    elif event.key == pygame.K_p:
        start_game(game_settings, stats, score_board, screen, ship, aliens, bullets)


def check_keyup(event, ship):
    """
    Check key up event
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(game_settings, stats, score_board, screen, ship, aliens, bullets, button, mouse_x, mouse_y):
    """
    Start the game when clicking the play button
    """
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(game_settings, stats, score_board, screen, ship, aliens, bullets)


def check_events(game_settings, stats, score_board, screen, button, ship, aliens, bullets):
    """
    Check the response from keyboard and mouse
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, game_settings, stats, score_board, screen, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, stats, score_board, screen, ship, aliens, bullets, button,
                              mouse_x, mouse_y)


def update_screen(game_settings, stats, score_board, screen, button, ship, alien, bullets):
    """
    Update surfaces on screen
    """
    screen.fill(game_settings.bg_color)

    # Redraw bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blit_me()
    alien.draw(screen)
    score_board.show_score()

    # If game not active, play button:
    if not stats.game_active:
        button.draw_button()

    pygame.display.flip()


def update_bullets(game_settings, stats, score_board, screen, ship, aliens, bullets):
    """
    Update the position of bullet and delete those are out of screen
    """
    # Update the position
    bullets.update()
    # Delete bullet if exceeding the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(game_settings, stats, score_board, screen, ship, aliens, bullets)


def check_aliens_bottom(game_settings, stats, score_board, screen, ship, aliens, bullets):
    """
    Check whether aliens reach the bottom of screen
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, score_board, screen, ship, aliens, bullets)
            break


def check_bullet_alien_collision(game_settings, stats, score_board, screen, ship, aliens, bullets):
    """
    Check if the bullet hit the alien
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            score_board.prep_score()
            check_max_score(stats, score_board)
    if len(aliens) == 0:
        bullets.empty()
        game_settings.increase_level()
        stats.level += 1
        score_board.prep_level()
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


def game_initialize(game_settings, screen, ship, aliens, bullets):
    """
    Initialize the game
    """
    aliens.empty()
    bullets.empty()
    # Create a new group of ship and initialize the ship
    create_fleet(game_settings, screen, ship, aliens)
    ship.center_ship()


def ship_hit(game_settings, stats, score_board, screen, ship, aliens, bullets):
    """
    Respond to the collision of ship and alien
    """
    if stats.ships_left > 1:
        stats.ships_left -= 1
        score_board.prep_ships()
        game_initialize(game_settings, screen, ship, aliens, bullets)

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(game_settings, stats, score_board, screen, ship, aliens, bullets):
    """
    Update aliens positions
    """
    check_fleet_edges(game_settings, aliens)
    aliens.update()

    # Check collision between ship and aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, score_board, screen, ship, aliens, bullets)

    check_aliens_bottom(game_settings, stats, score_board, screen, ship, aliens, bullets)


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


def check_max_score(stats, score_board):
    if stats.score > stats.max_score:
        stats.max_score = stats.score
        score_board.prep_max_score()
