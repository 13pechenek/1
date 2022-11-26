import pygame
from figs import *
from pygame.locals import *

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}


def controlls():
    player_v = (0, 0)
    if pygame.key.get_pressed()[K_LEFT]:
        player_v = (dir[K_LEFT][0], dir[K_LEFT][1])
    if pygame.key.get_pressed()[K_RIGHT]:
        player_v = (player_v[0] + dir[K_RIGHT][0], player_v[1] + dir[K_RIGHT][1])
    if pygame.key.get_pressed()[K_UP]:
        player_v = (player_v[0] + dir[K_UP][0], player_v[1] + dir[K_UP][1])
    if pygame.key.get_pressed()[K_DOWN]:
        player_v = (player_v[0] + dir[K_DOWN][0], player_v[1] + dir[K_DOWN][1])
    return player_v


def push(player_x, player_y):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sin = -(player_y - event.pos[1]) / ((player_x - event.pos[0])**2 + (player_y - event.pos[1])**2)**0.5
            cos = -(player_x - event.pos[0]) / ((player_x - event.pos[0])**2 + (player_y - event.pos[1])**2)**0.5
            bullet = Shots().TypeOne()
            bullet.set_shot(player_x, player_y, sin, cos)
            return bullet
