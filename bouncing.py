import sys, pygame
from Bug import Bug

pygame.init()

size = width, height = 600, 600
speed = [2, 2]
black = 0, 0, 0
FPS = 30
sprites = pygame.sprite.Group()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

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

	ballrect = ballrect.move(speed)

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]

	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	screen.fill(black)
	screen.blit(ball, ballrect)

	# calls update method on all sprites in group
	sprites.update()
	sprites.draw(screen)

	pygame.display.flip()

	# blocks to keep the loop running at the right no of FPS
	fps_clock.tick(FPS)