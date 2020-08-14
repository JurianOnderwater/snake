import pygame
import time
import random
from snake import *
from pynput.keyboard import Key, Controller

keyboard = Controller()

gameLoop()
time.sleep(3)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.left)
keyboard.release(Key.left)
keyboard.press(Key.right)
keyboard.release(Key.right)
