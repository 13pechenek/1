import datetime
from random import random, randint
import pygame as pg
from shots import *


class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v_player = (0, 0)
        self.health_player = 5
        self.img = pg.image.load('images/texture.bmp')
        img = pg.image.load('images/love1.png')
        self.img1 = pg.transform.scale(img, (40, 40))
        self.mask = pg.mask.from_surface(self.img)

    def our_lives(self, screen):
        
        for i in range(self.health_player):
            rect = pg.rect.Rect(i*50+100, 45, 35, 35)
            screen.blit(self.img1, rect)

    def draw_player(self, screen):
        if self.x_player + self.v_player[0] > 50 and self.x_player + self.v_player[0] < 1550:
            self.x_player += self.v_player[0]
        if self.y_player + self.v_player[1] > 10 and self.y_player + self.v_player[1] < 852:
            self.y_player += self.v_player[1]
        rect = pg.rect.Rect(self.x_player - 10, self.y_player - 20, 20, 40)
        screen.blit(self.img, rect)

    
        