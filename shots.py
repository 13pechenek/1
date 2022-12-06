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
            img = pg.image.load('ball.png')
            self.img1 = pg.transform.scale(img, (5, 5))
            self.mask = pg.mask.from_surface(self.img1)

        def draw_shot(self, screen):
            self.bul_x += self.bul_v[0]
            self.bul_y += self.bul_v[1]
            rect = pg.rect.Rect(self.bul_x-2.5, self.bul_y-2.5, 5, 5)
            screen.blit(self.img1, rect)

        def check_shot(self, obj):
            if self.mask.overlap_area(obj[0], (obj[1] - self.bul_x, obj[2] - self.bul_y)) > 0:
                return True
            else:
                return False