import pygame.font


class Scoreboard:
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = game_settings
        self.stats = stats

        # Font settings
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the score board
        self.prep_score()

    def prep_score(self):
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
