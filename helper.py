import pygame
import time
import random

pygame.init()

# Game settings
width = 800
height = 600
speed = 250
block = 10
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Me')
font_style = pygame.font.SysFont(None, 25)

# Colors
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
white = (255, 255, 255)

clock = pygame.time.Clock()


def go(direction):
	if direction == 'left':
		x1_change = -block
		y1_change = 0
	elif direction == 'right':
		x1_change = block
		y1_change = 0
	elif direction == 'up':
		x1_change = 0
		y1_change = -block
	elif direction == 'down':
		x1_change = 0
		y1_change = block
	return x1_change, y1_change


def distance_get(fx, fy, sx, sy):
	dx = abs(fx-sx)
	dy = abs(fy-sy)
	pyt = dx*dx + dy*dy
	distance = math.sqrt(pyt)
	return distance


def message(msg, color):
	mes = font_style.render(msg, True, color)
	dis.blit(mes, [round(width/10), round(height/3)])


def show_score(score):
	mes = font_style.render("Score: " + str(score), True, yellow)
	dis.blit(mes, [0, 0])


def draw_snake(snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, green, [round(x[0]), round(x[1]), block, block])

