import pygame
from pygame.locals import*

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

def controlls(v):
    v=(0,0)
    if pygame.key.get_pressed()[K_LEFT]:
        v = (dir[K_LEFT][0], dir[K_LEFT][1])
    if pygame.key.get_pressed()[K_RIGHT]:
        v = (v[0] + dir[K_RIGHT][0], v[1] +dir[K_RIGHT][1])
    if pygame.key.get_pressed()[K_UP]:
        v = (v[0] + dir[K_UP][0], v[1] +dir[K_UP][1])
    if pygame.key.get_pressed()[K_DOWN]:
        v = (v[0] + dir[K_DOWN][0], v[1] +dir[K_DOWN][1])
    return v

