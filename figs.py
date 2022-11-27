import datetime
from random import random, randint
import pygame as pg
from ii import*
from shots import*

class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v_player = (0, 0)
        self.h_player = 5

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
        self.x_enemy = randint(100,1500)
        self.y_enemy = randint(200,600)
        self.v_enemy = (0, 0)
        self.lives = 1
        self.bullets = 20
        self.able_to = True
        self.time = ((
            datetime.datetime.today().hour * 60 * 60
            + datetime.datetime.today().minute * 60
            + datetime.datetime.today().second) * 1000000
            + datetime.datetime.today().microsecond)
        self.last_shot = 0
    def draw_enemy(self, screen, cord_mas, t, player_x, player_y):
        self.v_enemy = enemy_move(self, player_x, player_y)
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
                cord_mas[int(self.x_enemy) - 5 + i][ int(self.y_enemy) -5 + j] = t+1
        return enemy_shot(self, player_x, player_y)