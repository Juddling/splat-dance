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


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound


def random_bug():
    """
    create a random bug in one of the four positions:
    top, bottom, left or right
    """
    x = random.randint(1, 4)
    margin = 100

    if x == 1:
        return Bug(width/2, margin, 1)
    elif x == 2:
        return Bug(width/2, height-margin, 2)
    elif x == 3:
        return Bug(margin, height/2, 3)

    return Bug(width-margin, height/2, 4)

fps_clock = pygame.time.Clock()
punch_sound = load_sound("punch.wav")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for bug in sprites.sprites():
                if bug.is_bug_at_position(event.key):
                    punch_sound.play()
                    bug.squish()

    screen.fill(black)

    if len(sprites.sprites()) == 0:
        sprites.add(random_bug())

    # calls update method on all sprites in group
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    # blocks to keep the loop running at the right no of FPS
    fps_clock.tick(FPS)
