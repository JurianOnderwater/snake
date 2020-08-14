import pygame
import time
import random

pygame.init()
# Game settings
width = 800
height = 600
speed = 30
block = 10
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Me')

# Colors
blue = (0, 0, 255)
red = (255, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)


def message(msg, color):
	mes = font_style.render(msg, True, color)
	dis.blit(mes, [round(width/10), round(height/3)])


def our_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [round(x[0]), round(x[1]), block, block])


def gameLoop():
	game_over = False
	game_close = False

	x1 = width / 2
	y1 = height / 2

	x1_change = 0
	y1_change = 0

	snake_List = []
	Length_of_snake = 1

	foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
	foody = round(random.randrange(0, height - block) / 10.0) * 10.0

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
				if event.type == pygame.QUIT:
					game_over = True
					game_close = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -block
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = block
					y1_change = 0
				elif event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -block
				elif event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = block
		if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
			game_close = True
		x1 += x1_change
		y1 += y1_change
		dis.fill(black)
		pygame.draw.rect(dis, blue, [round(foodx), round(foody), block, block])
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)
		if len(snake_List) > Length_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = True

		our_snake(block, snake_List)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, width - block) / 10.0) * 10.0
			foody = round(random.randrange(0, height - block) / 10.0) * 10.0
			Length_of_snake += 1

		clock.tick(speed)

	message("Thank you for playing!", white)
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	quit()

gameLoop()


