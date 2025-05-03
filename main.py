import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullets import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable,)

    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    asteroidField = AsteroidField()
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
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        # Set the FPS to a max of 60
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for asteroid in asteroids:
            if not Player.collisions(player, asteroid):
                print("Game over!")
                exit()
            
            for bullet in shots:
                if not Asteroid.collisions(asteroid, bullet):
                    bullet.kill()
                    Asteroid.split(asteroid)
if __name__ == "__main__":
    main()