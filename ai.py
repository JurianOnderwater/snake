import pygame
import time
import random
from snake import *
from pynput.keyboard import Key, Controller

keyboard = Controller()

gameLoop()
time.sleep(5)
keyboard.press(Key.up)
keyboard.release(Key.up)
