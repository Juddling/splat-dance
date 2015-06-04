import pygame
import splat


class Bug(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("bug.png")
        self.size = self.image.get_size()
        # adjusts the position of the bug so the x,y the center of the bug
        # is at x, y not the top left
        self.rect = (x - self.size[0]/2, y - self.size[1]/2)

        # after this number of frames, the bug will disappear
        self.lifespan = 5

    def update(self):
        self.lifespan = self.lifespan - 1

        if self.lifespan <= 0:
            self.kill()
