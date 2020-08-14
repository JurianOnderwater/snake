import pygame
import time
import random
block = 10


def go(direction, x1_change, y1_change):
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
