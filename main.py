import pgzrun
import random
import pygame.display
import sys
from ctypes import windll
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

def draw():
    mod.screen.blit("back", (0, 0))
    mario.draw()
    luigi.draw()
    coin.draw()
    enemy.draw()

def update():
    #mario sections
    if keyboard.up:
        mario.y -= 5
    if keyboard.down:
        mario.y += 5
    if keyboard.left:
        mario.x -= 5
        mario.image = "mario_left"
    if keyboard.right:
        mario.x += 5
        mario.image = "mario_right"
    #luigi sections
    if keyboard.w:
        luigi.y -= 5
    if keyboard.s:
        luigi.y += 5
    if keyboard.a:
        luigi.x -= 5
        luigi.image = "luigi_left"
    if keyboard.d:
        luigi.x += 5
        luigi.image = "luigi_right"


WIDTH = 1280
HEIGHT = 720

hwnd = pygame.display.get_wm_info()['window']
windll.user32.MoveWindow(hwnd, 130, 30, WIDTH, HEIGHT, False)
mod = sys.modules['__main__']

mario = Actor("mario_right")
mario.x = random.randint(0, 1280)
mario.y = random.randint(0, 720)

luigi = Actor("luigi_right")
luigi.x = random.randint(0, 1280)
luigi.y = random.randint(0, 720)

coin = Actor("coin")
coin.x = random.randint(0, 1280)
coin.y = random.randint(0, 720)

enemy = Actor("enemy_right")
enemy.x = random.randint(0, 1280)
enemy.y = random.randint(0, 720)

pgzrun.go()
 