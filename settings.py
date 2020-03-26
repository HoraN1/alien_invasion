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

        # level setup
        self.speedup_scale = 1.1

        # Ship settings
        self.ship_speed = None
        self.ship_limit = 3

        # Alien settings
        self.alien_speed = None
        self.fleet_drop_speed = None
        self.fleet_direction = 1  # 1 to the right, -1 to the left
        self.alien_points = 50

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self. bullet_color = 230, 20, 20
        self.bullet_speed = None
        self.bullets_allowed = 8

        # Button settings
        self.button_size = 200, 50
        self.button_color = (70, 165, 70)
        self.font_color = (245, 245, 245)

        self.initialize_settings()

    def initialize_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 0.7
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_level(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
        self.alien_points *= 2
