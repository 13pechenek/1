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

#ВЫСТРЕЛЫ (вариант 1)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.Vx = 0
        self.Vy = 0
        self.dest_x = 0
        self.dest_y = 0

    def move(self):
        self.x += self.Vx
        if self.x <= display_width:
            display.blit(bullet , (self.x , self. y)) #ПУЛЯ ЗДЕСЬ!
            return True
        else:
            return False

    def find_path(self, dest_x, dest_y):
        self.dest_x = dest_x
        self.dest_y = dest_y

        dx = dest_x - self.x
        count_up = dx // self.Vx
 
        if self.y >= dest_y: 
             dy = self.y - dest_y
             self.Vy = dy / count_up
        else:
            dy = dest_y -self.y
            self.Vy = - (dy / count_up)


    def move_to(self):
         self.x += self.Vx
         self.y -= self.Vy

        if self.x <= self.dest_x:
            display.blit(bullet , (self.x , self.y))
            return True
        else:
            return False