import pygame
import time

pygame.init()
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

game_over = False

x1 = width/2
y1 = height/2

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
	mes = font_style.render(msg, True, color)
	dis.blit(mes, [width/2, height/2])


while not game_over:
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
	if x1 <= 0 or x1 >= width or y1 <= 0 or y1 >= 0:
		game_over = True
	x1 += x1_change
	y1 += y1_change

	pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
	pygame.display.update()
	clock.tick(speed)

message("Game Over", white)
pygame.quit()
quit()


