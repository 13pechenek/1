import pygame as pg
import math
from random import random
import datetime

class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v = (0, 0)

    def draw_player(self, screen):
        self.x_player += self.v[0]
        self.y_player += self.v[1]
        img = pg.image.load('texture.png')
        rect = pg.rect.Rect(self.x_player-5,self.y_player-5,10,10)
        img = pg.transform.scale(img,(10,10))
        screen.blit(img, rect)


def draw_enemy(screen, x_enemy, y_enemy):
    pg.draw.polygon(
        screen,
        (255, 0, 0),
        [
            (x_enemy+5, y_enemy+5),
            (x_enemy-5, y_enemy+5),
            (x_enemy-5, y_enemy-5),
            (x_enemy+5, y_enemy-5)])


class shots:
    class type_1:
        def set_shot(self, bul_x, bul_y, sin, cos):
            self.bul_x = bul_x
            self.bul_y = bul_y
            self.l_time = ((
                datetime.datetime.today().hour * 60 * 60
                + datetime.datetime.today().minute * 60
                + datetime.datetime.today().second) * 1000000
                + datetime.datetime.today().microsecond)
            a = random() - 0.5
            self.bul_v = (5*(a/5+cos), 5*(sin-a/5))
        def draw_shot(self, screen):
            self.bul_x += self.bul_v[0]
            self.bul_y += self.bul_v[1]
            pg.draw.circle(screen, (255, 0, 0), (self.bul_x, self.bul_y), 7)
