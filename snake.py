import pygame
import time

pygame.init()
# Game settings
width = 800
height = 600
speed = 30
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Me')

# Colors
blue = (0, 0, 255)
red = (255, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
	mes = font_style.render(msg, True, color)
	dis.blit(mes, [round(width/2), round(height/2)])


def gameLoop():
	game_over = False
	game_close = False

	x1 = width / 2
	y1 = height / 2

	x1_change = 0
	y1_change = 0
	while not game_over:
		while game_close == True:
			message("Press 1 to play again, 2 to close game", white)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						gameLoop()
					elif event.key == pygame.K_2:
						game_over = True
						game_close = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -10
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = 10
					y1_change = 0
				elif event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -10
				elif event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = 10
		if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
			game_close = True
		x1 += x1_change
		y1 += y1_change
		dis.fill(blue)
		pygame.draw.rect(dis, white, [round(x1), round(y1), 10, 10])
		pygame.display.update()
		clock.tick(speed)

	message("Game Over", white)
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	quit()

gameLoop()


