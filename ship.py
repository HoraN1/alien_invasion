import pygame


class Ship:
    def __init__(self, game_settings, screen):
        """
        Initialize the ship and setup initial location
        """
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image
        image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(image, (123, 128))

        # Setup the rectangular of the ship and screen
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
        """
        # Update the location of the ship center
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed

        # Update the ship location based on self.center
        self.rect.centerx = self.center

    def blit_me(self):
        """
        Draw the ship at specific location
        """
        self.screen.blit(self.image, self.rect)
