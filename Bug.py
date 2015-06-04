import pygame


class Bug(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)

        self.position = position

        self.image = pygame.image.load("bug.png")
        self.size = self.image.get_size()
        # adjusts the position of the bug so the x,y the center of the bug
        # is at x, y not the top left
        self.rect = (x - self.size[0]/2, y - self.size[1]/2)

        # after this number of frames, the bug will disappear
        self.lifespan = 90

    def update(self):
        self.lifespan = self.lifespan - 1

        if self.lifespan <= 0:
            self.kill()

    def squish(self):
        self.kill()

    def is_bug_at_position(self, key):
        if key == pygame.K_UP and self.position == 1:
            return True

        if key == pygame.K_DOWN and self.position == 2:
            return True

        if key == pygame.K_LEFT and self.position == 3:
            return True

        if key == pygame.K_RIGHT and self.position == 4:
            return True

        return False
