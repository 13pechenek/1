import pygame
from pygame.locals import*

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

def controlls(v):
    if pygame.key.get_pressed()[K_LEFT]:
        v=dir[K_LEFT]
    elif pygame.key.get_pressed()[K_RIGHT]:
        v=dir[K_RIGHT]
    elif pygame.key.get_pressed()[K_UP]:
        v=dir[K_UP]
    elif pygame.key.get_pressed()[K_DOWN]:
        v=dir[K_DOWN]
    else:
        v=(0,0) 
    return v