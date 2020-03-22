import pygame


class Ship:
    def __init__(self, screen):
        """
        Initialize the ship and setup initial location
        :param screen:
        """
        self.screen = screen
        # Loading ship image
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Put every ship at the middle bottom of the screen
        self.rect.center_x = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blit_me(self):
        """
        Draw the ship at specific location
        :return:
        """
        self.screen.blit(self.image, self.rect)
