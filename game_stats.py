class GameStats:
    """
    Track game stats
    """
    def __init__(self, game_settings):
        """
        Initialize stats data
        """
        self.game_settings = game_settings
        self.ships_left = None
        self.reset_stats()

        # Game activate when started
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit
