class GameStats:
    """
    Track game stats
    """
    def __init__(self, game_settings):
        """
        Initialize stats data
        """
        self.game_settings = game_settings
        self.reset_stats()

        # Game activate when started
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit
