import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in its fleet."""

    def __init__(self, ai_game):
        """Initialize alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and set its rect attributes.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()   

        # Start each new alien at top left corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)


    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

