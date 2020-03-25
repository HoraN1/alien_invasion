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

    def blit_me(self):
        """
        Draw alien at specific position
        """
        self.screen.blit(self.image, self.rect)
