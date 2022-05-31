import sys

import pygame

class Main:
    """Overall class."""

    def __init__(self):
        """Initialise the game."""
        pygame.init()

        # screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.screen_width = self.screen.get_rect().width
        # self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Rocket")

        self.rocket = Rocket(self)
    

    def run_game(self):
        """Main loop for the game"""

        while True:
            # check for key events, q for quit for now
            self._check_events()
            self.rocket.update()
                
            self.screen.fill((200, 200, 200))
            self.rocket.blit_rocket()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Handle key pressess."""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
            # self.rocket.update()
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
            # self.rocket.update()
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
    
    def _check_keyup_events(self, event):
        """Handle key releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

class Rocket:
    """Class for managing a rocket."""

    def __init__(self, game_assets):
        self.screen = game_assets.screen
        self.screen_rect = self.screen.get_rect()

        # Load the image, get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()

        # position the rocket to the middle of the screen
        # the image's center coordinates are set to the center coordinates of the screen
        self.image_rect.center = self.screen.get_rect().center

        # flags for movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blit_rocket(self):
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        """Updates the position of the rocket every time the arrow keys are pressed."""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += 1
        if self.moving_left and self.image_rect.left > 0:
            self.image_rect.x -= 1
        if self.moving_up and self.image_rect.top > 0:
            self.image_rect.y -= 1
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += 1


if __name__ == '__main__':
    screen = Main()
    screen.run_game()