import pygame

from constants import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    
    # Set screen settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # While loop to run the game
    while screen != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()