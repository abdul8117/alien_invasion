import sys

import pygame

# Create a class for the game
# The window is simply a blue background

class BlueBackground:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((0, 0, 255))
        pygame.display.set_caption("Blue screen")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    blue_bg = BlueBackground()
    blue_bg.run_game()