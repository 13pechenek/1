"""Данный файл содержит команды, отвечающие за поведение игрока"""

import pygame as pg


class Player:
    """Данный класс создает игрока  позволяет совершать операции над ним"""
    def __init__(self, mas):
        """Параметры по умолчанию"""
        self.x_player = mas[0]
        self.y_player = mas[1]
        self.v_player = (0, 0)
        self.health_player = mas[2]
        self.img = pg.image.load('images/texture.bmp')
        img_hurt = pg.image.load('images/love1.png')
        self.img_hurt = pg.transform.scale(img_hurt, (40, 40))
        img_bull = pg.image.load('images/bullet.png')
        self.img_bull = pg.transform.scale(img_bull, (30, 100))
        self.mask = pg.mask.from_surface(self.img)

    def draw_bullets(self, screen, bull_num):
        """Отображает на экране количество пуль в запасе"""
        for i in range(bull_num):
            rect = pg.rect.Rect(1500 - i*30, 45, 30, 100)
            screen.blit(self.img_bull, rect)

    def our_lives(self, screen):
        """Отобржает на экрани жизни:
        screen - экран
        """
        for i in range(self.health_player):
            rect = pg.rect.Rect(i*50+100, 45, 35, 35)
            screen.blit(self.img_hurt, rect)

    def draw_player(self, screen, obstacles):
        """1.Создает игрока
        2.Проверяет игрока на столкновение со стенкой
        3.Задает игроку скорость(движение);
        screen - экран,
        obstacles - стенки"""
        for obst in obstacles:
            if self.mask.overlap_area(
                    obst.mask,
                    (
                        obst.x_wall
                        - self.x_player
                        - self.v_player[0] + 10,
                        obst.y_wall - self.y_player
                        + 20)) > 0:
                self.v_player = (0, self.v_player[1])
            if self.mask.overlap_area(
                    obst.mask,
                    (
                        obst.x_wall
                        - self.x_player
                        + 10,
                        obst.y_wall
                        - self.v_player[1]
                        - self.y_player
                        + 20)) > 0:
                self.v_player = (self.v_player[0], 0)
        # В пределах нахождения игровой зоны:
        if (
                self.x_player + self.v_player[0] > 50
                and self.x_player + self.v_player[0] < 1550):
            self.x_player += self.v_player[0]
        if (
                self.y_player + self.v_player[1] > 10
                and self.y_player + self.v_player[1] < 852):
            self.y_player += self.v_player[1]
        rect = pg.rect.Rect(self.x_player - 10, self.y_player - 20, 20, 40)
        screen.blit(self.img, rect)
