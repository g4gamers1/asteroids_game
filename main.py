import pygame # type: ignore
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable_group = pygame.sprite.Group(player)
    drawable_group = pygame.sprite.Group(player)
    Player.containers = (updatable_group, drawable_group)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatable_group:
            updatable.update(dt)    
        screen.fill("black")
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()


        dt = clock.tick(240) / 1000.0
        

if __name__ == "__main__":
    main()