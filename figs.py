import datetime
from random import random
import pygame as pg


class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v_player = (0, 0)
        self.h_player = 3

    def draw_player(self, screen, cord_mas):
        for i in range(20):
            for j in range(40):
                cord_mas[int(self.x_player) - 10 + i][ int(self.y_player) -20 + j] = 0
        self.x_player += self.v_player[0]
        self.y_player += self.v_player[1]
        img = pg.image.load('texture.bmp')
        rect = pg.rect.Rect(self.x_player - 10, self.y_player - 20, 20, 40)
        screen.blit(img, rect)
        for i in range(20):
            for j in range(40):
                cord_mas[int(self.x_player) - 10 + i][ int(self.y_player) -20 + j] = 1

class Enemy:
    def __init__(self):
        self.x_enemy = 400
        self.y_enemy = 400
        self.v_enemy = (0, 0)

    
    def draw_enemy(self, screen, cord_mas):
        for i in range(10):
            for j in range(10):
                cord_mas[int(self.x_enemy) - 5 + i][ int(self.y_enemy) -5 + j] = 0
        self.x_enemy += self.v_enemy[0]
        self.y_enemy += self.v_enemy[1]
        pg.draw.polygon(
            screen,
            (255, 0, 0),
            [
                (self.x_enemy+5, self.y_enemy+5),
                (self.x_enemy-5, self.y_enemy+5),
             (self.x_enemy-5, self.y_enemy-5),
                (self.x_enemy+5, self.y_enemy-5)])
        for i in range(10):
            for j in range(10):
                cord_mas[int(self.x_enemy) - 5 + i][ int(self.y_enemy) -5 + j] = 2


class Shots:
    class TypeOne:
        def set_shot(self, bul_x, bul_y, sin, cos, typ):
            self.bul_x = bul_x
            self.bul_y = bul_y
            self.live=1
            self.l_time = ((
                datetime.datetime.today().hour * 60 * 60
                + datetime.datetime.today().minute * 60
                + datetime.datetime.today().second) * 1000000
                + datetime.datetime.today().microsecond)
            a_rand = random() - 0.5
            self.bul_v = (5*(a_rand/5+cos), 5*(sin-a_rand/5))
            self.type = typ
            self.h_en = False
            self.h_pl = False

        def draw_shot(self, screen, cord_mas, player_mas):
            i, j = 0, 0
            while i**2 + j**2 <= 49:
                while i**2 + j**2 <= 49:
                    cord_mas[round(self.bul_x) + i][round(self.bul_y) + j] = 0
                    cord_mas[round(self.bul_x) - i][round(self.bul_y) + j] = 0
                    cord_mas[round(self.bul_x) - i][round(self.bul_y) - j] = 0
                    cord_mas[round(self.bul_x) + i][round(self.bul_y) - j] = 0
                    j += 1
                i += 1
                j = 0
            self.bul_x += self.bul_v[0]
            self.bul_y += self.bul_v[1]
            pg.draw.circle(screen, (255, 0, 0), (self.bul_x, self.bul_y), 7)
            i, j = 0, 0
            h, h1, h2 = False, False, False
            while i**2 + j**2 <= 49 and not h:
                while i**2 + j**2 <= 49 and not h:
                    if (player_mas[round(self.bul_x) + i][round(self.bul_y) + j] == 1 or player_mas[round(self.bul_x) + i][round(self.bul_y) - j] == 1 or player_mas[round(self.bul_x) - i][round(self.bul_y) + j] == 1 or player_mas[round(self.bul_x) - i][round(self.bul_y) - j] == 1 ) and self.type == 1:
                        i, j = 0, 0
                        while i**2 + j**2 <= 49:
                            while i**2 + j**2 <= 49:
                                cord_mas[round(self.bul_x) + i][round(self.bul_y) + j] = 0
                                cord_mas[round(self.bul_x) - i][round(self.bul_y) + j] = 0
                                cord_mas[round(self.bul_x) - i][round(self.bul_y) - j] = 0
                                cord_mas[round(self.bul_x) + i][round(self.bul_y) - j] = 0
                                j += 1
                            i += 1
                            j = 0
                        h = True
                        h2 = True
                    if (player_mas[round(self.bul_x) + i][round(self.bul_y) + j] == 2 or player_mas[round(self.bul_x) + i][round(self.bul_y) - j] == 2 or player_mas[round(self.bul_x) - i][round(self.bul_y) + j] == 2 or player_mas[round(self.bul_x) - i][round(self.bul_y) - j] == 2 ) and self.type == 0:
                        i, j = 0, 0
                        while i**2 + j**2 <= 49:
                            while i**2 + j**2 <= 49:
                                cord_mas[round(self.bul_x) + i][round(self.bul_y) + j] = 0
                                cord_mas[round(self.bul_x) - i][round(self.bul_y) + j] = 0
                                cord_mas[round(self.bul_x) - i][round(self.bul_y) - j] = 0
                                cord_mas[round(self.bul_x) + i][round(self.bul_y) - j] = 0
                                j += 1
                            i += 1
                            j = 0
                        h = True
                        h1 = True
                    else:
                        cord_mas[round(self.bul_x) + i][round(self.bul_y) + j] = 1
                        cord_mas[round(self.bul_x) - i][round(self.bul_y) + j] = 1
                        cord_mas[round(self.bul_x) - i][round(self.bul_y) - j] = 1
                        cord_mas[round(self.bul_x) + i][round(self.bul_y) - j] = 1
                    j += 1
                i += 1
                j = 0
            if h:
                self.live = 0
                if h1:
                    self.h_en = True
                if h2:
                    self.h_pl = True
                
