import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    A class for alien unit
    """
    def __init__(self, game_settings, screen):
        """
        Initialize alien and its position
        """
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load image of alien
        image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(image, (64, 45))
        self. rect = self.image.get_rect()

        # Initial position at left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the initial position
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        Check if the aliens are at the edge.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """
        Move the alien to the right
        """
        self.x += (self.game_settings.alien_speed * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def blit_me(self):
        """
        Draw alien at specific position
        """
        self.screen.blit(self.image, self.rect)
