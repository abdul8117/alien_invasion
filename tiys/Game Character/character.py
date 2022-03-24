import sys

import pygame

"""
Create __init__()
Initialise pygame
create the display (self.screen)

Create run_game()
indefinite loop to check for keyboard/mouse events and to update the screen (flip) 

"""

class GameCharacher:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pacman")
        
        # load pacman img
        self.pacman = Pacman(self)

    def run_game(self):
        while True:
            self._check_events()
            
            # update screen
            pygame.display.flip()
            self.pacman.blitme()
    
    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


class Pacman:
    def __init__(self, gc):
        self.screen= gc.screen
        self.screen_rect = self.screen.get_rect()

        # load image, get its rect
        self.pacman_image = pygame.image.load('tiys/Game Character/pacman.png')
        self.pacman_rect = self.pacman_image.get_rect()

        # start each pacman at the middle of the screen
        self.pacman_rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.pacman_image, self.pacman_rect)

if __name__ == '__main__':
    gc = GameCharacher()
    gc.run_game()