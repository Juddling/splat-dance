import sys
import pygame
import random
from sprites import Bug, Score
from usb_dance import DanceMat

pygame.init()

size = width, height = 600, 600
# black represented in red, green and blue
background_colour = 0, 0, 0
FPS = 30
# legnth of time in seconds for new bug to spawn
bug_delay = 0.5
bug_delay_frames = bug_delay * FPS

sprites = pygame.sprite.Group()
screen = pygame.display.set_mode(size)
score = 0
score_increment = 10
score_decrement = 5


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
respawn_frames_remaining = 0
score_sprite = Score()
sprites.add(score_sprite)
dance_mat = DanceMat()

while True:
    dance_mat.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            for sprite in sprites.sprites():
                if not isinstance(sprite, Bug):
                    continue

                if sprite.is_bug_at_position(event.key, dance_mat):
                    score += score_increment
                    score_sprite.change_score(score)

                    punch_sound.play()
                    sprite.squish()
                    respawn_frames_remaining = bug_delay_frames
                else:
                    score -= score_decrement
                    score_sprite.change_score(score)

    screen.fill(background_colour)

    if len(sprites.sprites()) == 1:
        if respawn_frames_remaining == 0:
            sprites.add(random_bug())
        else:
            respawn_frames_remaining = respawn_frames_remaining - 1

    # calls update method on all sprites in group
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    # blocks to keep the loop running at the right number of FPS
    fps_clock.tick(FPS)
