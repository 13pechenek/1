"""Данный файл содержит команды, отвечающие за поведение пули"""

import datetime
from random import random
import pygame as pg




class Shots:
    """Класс, в котором хранятся выстрелы разных типов"""
    class TypeOne:
        """Первый тип выстрелов"""
        def set_shot(self, bullet_x, bullet_y, sin, cos, typ):
            """1. Создает новый выстрел в заданном направлении;
                bullet_x - х-координата пули,
                bullet_y - y-координата пули,
                sin и cos - синус и косинус угла прямой, задающей направление выстрела,
                typ - тип пули(врага или игрока)
            """
            self.bullet_x = bullet_x
            self.bullet_y = bullet_y
            self.live = 1
            self.l_time = (datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond
            a_random = random() - 0.5
            self.bullet_v = (5*(a_random/5+cos), 5*(sin-a_random/5))
            self.type = typ

            img = pg.image.load('images/ball.png')
            self.img1 = pg.transform.scale(img, (5, 5))
            self.mask = pg.mask.from_surface(self.img1)

        def draw_shot(self, screen):
            """Рисует и двигает пули; screen - экран"""
            self.bullet_x += self.bullet_v[0]
            self.bullet_y += self.bullet_v[1]
            rect = pg.rect.Rect(self.bullet_x-2.5, self.bullet_y-2.5, 5, 5)
            screen.blit(self.img1, rect)

        def check_shot(self, object):
            """Проверяет попадание пули по объекту;
               object - объект, с которым идет проверка попадания
            """
            if self.mask.overlap_area(object[0], (object[1] - self.bullet_x, object[2] - self.bullet_y)) > 0:
                return True
            else:
                return False