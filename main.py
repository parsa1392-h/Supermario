import pgzrun
import random
import pygame.display
import sys
from ctypes import windll
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def correct_location(actor):
    if actor.x > WIDTH + actor.width//2:
        actor.x = -actor.width//2
    if actor.x < -actor.width//2:
        actor.x = WIDTH + actor.width//2
    if actor.y > WIDTH + actor.width//2:
        actor.y = -actor.width//2
    if actor.y < -actor.width//2:
        actor.y = WIDTH + actor.width//2

def random_location(actor):
    actor.x = random.randint(0, 1280)
    actor.y = random.randint(0, 720)

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
    correct_location(mario)
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
    correct_location(luigi)

WIDTH = 1280
HEIGHT = 720

hwnd = pygame.display.get_wm_info()['window']
windll.user32.MoveWindow(hwnd, 130, 30, WIDTH, HEIGHT, False)
mod = sys.modules['__main__']

mario = Actor("mario_right")
random_location(mario)

luigi = Actor("luigi_right")
random_location(luigi)

coin = Actor("coin")
random_location(coin)

enemy = Actor("enemy_right")
random_location(enemy)

pgzrun.go()
 