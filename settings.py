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
        self.ship_limit = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 100
        self.fleet_direction = 1  # 1 to the right, -1 to the left

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self. bullet_color = 230, 20, 20
        self.bullet_speed = 1
        self.bullets_allowed = 8
