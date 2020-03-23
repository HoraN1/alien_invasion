import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    A class to manage the bullet
    """
    def __init__(self, game_settings, screen, ship):
        """
        Create a bullet at the location of ship
        """
        super().__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) then correct the position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Mark the bullet position with float
        self.y = float(self.rect.y)
        # Properties of bullet
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed

    def update(self):
        """
        Move the bullet
        """
        # Update the position(float)
        self.y -= self.speed_factor
        # Update bullet rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw bullet on screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
