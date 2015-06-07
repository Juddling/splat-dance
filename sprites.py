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

    def key_match_position(self, key):
        if self.position == 1 and key == pygame.K_UP:
            return True

        if self.position == 2 and key == pygame.K_DOWN:
            return True

        if self.position == 3 and key == pygame.K_LEFT:
            return True

        if self.position == 4 and key == pygame.K_RIGHT:
            return True

        return False

    def dance_button_match_position(self, dance_mat):
        if self.position == 1 and dance_mat.up():
            return True

        if self.position == 2 and dance_mat.down():
            return True

        if self.position == 3 and dance_mat.left():
            return True

        if self.position == 4 and dance_mat.right():
            return True

        return False


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = pygame.Color('white')
        self.score = 0
        self.change_score(self.score)
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        pass

    def change_score(self, score):
        self.score = score
        msg = "Score: %d" % self.score
        self.image = self.font.render(msg, 0, self.color)
