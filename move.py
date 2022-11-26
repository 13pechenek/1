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

def push(x, y):
     for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sin = (y - event.pos[1]) / ( (x - event.pos[0] )**2 + (y - event.pos[1])**2)**0.5 
            cos = (x - event.pos[0]) / ( (x - event.pos[0] )**2 + (y - event.pos[1])**2)**0.5
            shot = shots().type_1()
            shot.set_shot(x, y, sin, cos)
    if shot != None:
        return shot
    else:
        return None
