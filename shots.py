import datetime
from random import random
import pygame as pg




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

        def cleaning(self, cord_mas):
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

        def draw_shot(self, screen, cord_mas, player_mas, t):
            self.cleaning(cord_mas)
            self.bul_x += self.bul_v[0]
            self.bul_y += self.bul_v[1]
            pg.draw.circle(screen, (255, 0, 0), (self.bul_x, self.bul_y), 7)
            self.move_shot(cord_mas, player_mas, t)

        def move_shot(self, cord_mas, player_mas, g):
            i, j = 0, 0
            h, h1, h2 = False, 0, False
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
                    if (player_mas[round(self.bul_x) + i][round(self.bul_y) + j] == -1 or player_mas[round(self.bul_x) + i][round(self.bul_y) - j] == -1 or player_mas[round(self.bul_x) - i][round(self.bul_y) + j] == -1 or player_mas[round(self.bul_x) - i][round(self.bul_y) - j] == -1 ):
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
                    for t in range(g):
                        if (player_mas[round(self.bul_x) + i][round(self.bul_y) + j] == t+2 or player_mas[round(self.bul_x) + i][round(self.bul_y) - j] == t+2 or player_mas[round(self.bul_x) - i][round(self.bul_y) + j] == t+2 or player_mas[round(self.bul_x) - i][round(self.bul_y) - j] == t+2 ) and self.type == 0:
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
                            h1 = t+1
                    if not h:
                        cord_mas[round(self.bul_x) + i][round(self.bul_y) + j] = 1
                        cord_mas[round(self.bul_x) - i][round(self.bul_y) + j] = 1
                        cord_mas[round(self.bul_x) - i][round(self.bul_y) - j] = 1
                        cord_mas[round(self.bul_x) + i][round(self.bul_y) - j] = 1
                    j += 1
                i += 1
                j = 0
            if h:
                self.live = 0
                if h1!=0:
                    self.h_en = h1
                if h2:
                    self.h_pl = True