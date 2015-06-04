import sys
import pygame
import random
from Bug import Bug

pygame.init()

size = width, height = 600, 600
black = 0, 0, 0
FPS = 30
sprites = pygame.sprite.Group()

screen = pygame.display.set_mode(size)


def random_bug():
    """
    create a random bug in one of the four positions:
    top, bottom, left or right
    """
    x = random.randint(1, 4)
    margin = 100

    if x == 1:
        return Bug(width/2, margin)
    elif x == 2:
        return Bug(width/2, height-margin)
    elif x == 3:
        return Bug(margin, height/2)

    return Bug(width-margin, height/2)

fps_clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if len(sprites.sprites()) == 0:
        sprites.add(random_bug())

    # calls update method on all sprites in group
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    # blocks to keep the loop running at the right no of FPS
    fps_clock.tick(FPS)
