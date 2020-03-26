import pygame
import game_functions as g_func

from ship import Ship
from settings import Settings
from game_stats import GameStats
from score_board import Scoreboard
from button import Button
from pygame.sprite import Group


def run_game():
    """
    Initialize a game screen
    """
    # Game screen setup
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a object to store game stats
    stats = GameStats(game_settings)

    # Create a button and score board
    play_button = Button(game_settings, screen, "Play")
    score = Scoreboard(game_settings, screen, stats)

    # Create a ship, alien and bullet
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a group of alien
    g_func.create_fleet(game_settings, screen, ship, aliens)

    # Start the game main loop: check keyboard and mouse event, update ship, update bullet and screen
    while True:
        g_func.check_events(game_settings, stats, screen, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            g_func.update_bullets(game_settings, stats, score, screen, ship, aliens, bullets)
            g_func.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
        g_func.update_screen(game_settings, stats, score, screen, play_button, ship, aliens, bullets)


run_game()
