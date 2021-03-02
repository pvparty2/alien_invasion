import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Update screen's rect settings
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Respond for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_keydown_events(event)
            self._check_keyup_events(event)
            
    
    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                self.ship.moving_right = True
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game isntance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
