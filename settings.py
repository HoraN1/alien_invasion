class Settings:
    """
    Storing all the settings for Alien Invasion game
    """
    def __init__(self):
        """
        Initialize game settings
        """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 40, 80)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self. bullet_color = 80, 20, 20
