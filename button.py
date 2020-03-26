import pygame.font


class Button:
    def __init__(self, game_settings, screen, msg):
        """
        Initialize button properties
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Setup button size and other properties
        self.width, self.height = game_settings.button_size
        self.button_color = game_settings.button_color
        self.text_color = game_settings.font_color
        self.font = pygame.font.SysFont(None, 48)

        # Create button rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Create button tag once
        self.pre_msg(msg)

    def pre_msg(self, msg):
        """
        Make msg image and center it in the button
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
