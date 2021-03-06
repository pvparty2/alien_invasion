import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # Store a group of individual bullet classes.
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
            if event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and add it to the bullets group."""
        if self.settings.bullets_allowed > len(self.bullets):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Calls the update method of every member sprite.
        self.bullets.update()

        # Get rid of old bullets that have disappeared from screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    #### ALIENS
    def _create_fleet(self):
        """Create fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        available_space_x = self.settings.screen_width - (2 * alien.rect.width)
        number_aliens_x = available_space_x // (2 * alien.rect.width)

        # Determing the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien.rect.height) - ship_height)
        number_rows = available_space_y // (2 * alien.rect.height)                            

        # Create full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # Create an alien and place it in the row.
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self.aliens.update()

if __name__ == '__main__':
    # Make a game isntance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
