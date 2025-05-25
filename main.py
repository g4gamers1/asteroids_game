import sys
import pygame # type: ignore
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        updatable_group.update(dt)   

        for astroids in asteroids_group:
            if astroids.check_collions(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
        
        screen.fill("black")
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()


        dt = clock.tick(240) / 1000.0
        

if __name__ == "__main__":
    main()