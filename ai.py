import pygame
import time
import random
from snake import *
from pynput.keyboard import Key, Controller

keyboard = Controller()

gameLoop()
time.sleep(2)
keyboard.press('a')
keyboard.release('a')
