import sys, pygame
from Bug import Bug

pygame.init()

size = width, height = 600, 600
black = 0, 0, 0
FPS = 30
sprites = pygame.sprite.Group()

screen = pygame.display.set_mode(size)

margin = 100

bug_top = Bug(width/2, margin)
bug_bottom = Bug(width/2, height-margin)
bug_left = Bug(margin, height/2)
bug_right = Bug(width-margin, height/2)

sprites.add(bug_top, bug_bottom, bug_left, bug_right)

fps_clock = pygame.time.Clock()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill(black)

	# calls update method on all sprites in group
	sprites.update()
	sprites.draw(screen)

	pygame.display.flip()

	# blocks to keep the loop running at the right no of FPS
	fps_clock.tick(FPS)