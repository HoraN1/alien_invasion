import pygame


class Ship:
    def __init__(self, game_settings, screen):
        """
        Initialize the ship and setup initial location
        :param screen:
        """
        self.screen = screen
        self.game_settings = game_settings
        # Loading ship image
        image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(image, (123, 128))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Put every ship at the middle bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # Moving signal
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Adjust the location of ship by command
        :return:
        """
        if self.moving_right:
            self.center += self.game_settings.ship_speed
        if self.moving_left:
            self.center -= self.game_settings.ship_speed
        # Update the ship location based on self.center
        self.rect.centerx = self.center

    def blit_me(self):
        """
        Draw the ship at specific location
        :return:
        """
        self.screen.blit(self.image, self.rect)
