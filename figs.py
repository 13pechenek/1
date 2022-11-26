import datetime
from random import random
import pygame as pg


class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v_player = (0, 0)

        

    def draw_player(self, screen):
        self.x_player += self.v_player[0]
        self.y_player += self.v_player[1]
        img = pg.image.load('texture.bmp')
        rect = pg.rect.Rect(self.x_player - 10, self.y_player - 20, 20, 40)
        screen.blit(img, rect)


class Enemy:
    def __init__(self):
        self.x_enemy = 300
        self.y_enemy = 300
        self.v_enemy = (0, 0)


def draw_enemy(screen, x_enemy, y_enemy):
    pg.draw.polygon(
        screen,
        (255, 0, 0),
        [
            (x_enemy+5, y_enemy+5),
            (x_enemy-5, y_enemy+5),
            (x_enemy-5, y_enemy-5),
            (x_enemy+5, y_enemy-5)])


class Shots:
    class TypeOne:
        def set_shot(self, bul_x, bul_y, sin, cos, enemy_or_player):
            self.enemy_or_player = enemy_or_player
            self.bul_x = bul_x
            self.bul_y = bul_y
            self.l_time = ((
                datetime.datetime.today().hour * 60 * 60
                + datetime.datetime.today().minute * 60
                + datetime.datetime.today().second) * 1000000
                + datetime.datetime.today().microsecond)
            a_rand = random() - 0.5
            self.bul_v = (5*(a_rand/5+cos), 5*(sin-a_rand/5))

        def draw_shot(self, screen):
            self.bul_x += self.bul_v[0]
            self.bul_y += self.bul_v[1]
            pg.draw.circle(screen, (255, 0, 0), (self.bul_x, self.bul_y), 7)

        def hit_enemy(self , x_enemy, y_enemy):
            if (self.bul_x - x_enemy)**2 + (self.bul_y - y_enemy)**2 <= (7 + 5*1.4142)**2:
                return True
            else:
                return False


        
        
