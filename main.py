import pygame

from constants import *
from player import *

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    
    # Set screen settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # While loop to run the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        pygame.display.flip()
        # Set the FPS to a max of 60
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()