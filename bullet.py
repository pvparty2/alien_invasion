import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from a ship."""

    def __init__(self, ai_game):
        """Create a bullet object at a ship's current position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        # Update the rect position.
        self.rect.y = float(self.rect.y) - self.settings.bullet_speed

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)