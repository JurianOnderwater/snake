import pygame
import time
import random
from ai import *
from helper import *


def game_loop():
	game_over = False
	game_close = False

	x1 = width / 2
	y1 = height / 2

	x1_change = 0
	y1_change = 0

	snake_list = []
	snake_length = 1
	food_x = round(random.randrange(0, width - block) / 10.0) * 10.0
	food_y = round(random.randrange(0, height - block) / 10.0) * 10.0
	
	while not game_over:
		# Play again loop
		while game_close:
			message("Press 1 to play again, 2 to close game", white)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						game_loop()
					elif event.key == pygame.K_2:
						game_over = True
						game_close = False
				if event.type == pygame.QUIT:
					game_over = True
					game_close = False

		# User input loop
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
		
		# Search algorithm
		direction = best_first_search(food_x, food_y, x1, y1)
		move = go(direction)
		x1 += move[0]
		y1 += move[1]
		dis.fill(black)
		pygame.draw.rect(dis, blue, [round(food_x), round(food_y), block, block])

		# Game rule checks
		if [x1, y1] in snake_list:
			game_close = True
		if len(snake_list) > snake_length:
			del snake_list[0]
		if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
			game_close = True
		
		# Update score and snake
		snake_list.append([x1, y1])
		draw_snake(snake_list)
		if x1 == food_x and y1 == food_y:
			food_x = round(random.randrange(0, width - block) / 10.0) * 10.0
			food_y = round(random.randrange(0, height - block) / 10.0) * 10.0
			snake_length += 1
		show_score(snake_length)
		pygame.display.update()
		clock.tick(speed)

	message("Thank you for playing!", white)
	pygame.display.update()
	pygame.quit()
	quit()


game_loop()
