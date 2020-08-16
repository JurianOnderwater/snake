import pygame
import time
import random
import math

block = 10


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


def best_first_search(fx, fy, sx, sy, exception=[]):
	if fx > sx and 'right' not in exception:
		move = 'right'
	elif fx < sx and 'left' not in exception:
		move = 'left'
	elif fy > sy and 'down' not in exception:
		move = 'down'
	elif fy < sy and 'up' not in exception:
		move = 'up'
	else:
		move = 'none'
	return move


def avoid_tail(snake_List, move, x1, y1):
	x1_change = move[0]
	y1_change = move[1]
	x1 += x1_change
	y1 += y1_change
	snake_Head = []
	snake_Head.append(x1)
	snake_Head.append(y1)
	snake_List.append(snake_Head)
	for x in snake_List[:-1]:
		if x == snake_Head:
			return False
	return True

def hill_climbing(possible_moves, explored, d1, fx, fy, sx, sy):
	best_move = 'none'
	check = 0
	for direction in possible_moves:
		if direction == 'left' and (sx-block, sy) not in explored:
			sx -= block
			sy = sy
		elif direction == 'right' and (sx+block, sy) not in explored:
			sx += block
			sy = sy
		elif direction == 'up' and (sx, sy-block) not in explored:
			sx = sx
			sy -= block
		elif direction == 'down' and (sx, sy+block) not in explored:
			sx = sx
			sy += block
		distance = distance_get(fx, fy, sx, sy)
		if distance < d1:
			best_move = direction
			explored.append((sx, sy))
			print(best_move)
			d1 = distance
		elif distance == d1:
			if direction == 'up':
				best_move = direction
				explored.append((sx, sy))
				d1 = distance
				break
			elif direction == 'right':
				best_move = direction
				explored.append((sx, sy))
				d1 = distance
				break
			elif direction == 'left':
				best_move = direction
				explored.append((sx, sy))
				d1 = distance
				break
			elif direction == 'down':
				best_move = direction
				explored.append((sx, sy))
				d1 = distance
				break
	if best_move == 'none':
		return 0
	else:
		print(best_move)
		return best_move, explored
