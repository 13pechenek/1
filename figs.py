import datetime
from random import random, randint
import pygame as pg
from shots import *


class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v_player = (0, 0)
        self.h_player = 5
        self.img = pg.image.load('texture.bmp')
        img = pg.image.load('love1.png')
        self.img1 = pg.transform.scale(img, (40, 40))
        self.mask = pg.mask.from_surface(self.img)

    def our_lives(self, screen):
        
        for i in range(self.h_player):
            rect = pg.rect.Rect(i*50+100, 45, 35, 35)
            screen.blit(self.img1, rect)

    def draw_player(self, screen):
        if self.x_player + self.v_player[0] > 50 and self.x_player + self.v_player[0] < 1550:
            self.x_player += self.v_player[0]
        if self.y_player + self.v_player[1] > 10 and self.y_player + self.v_player[1] < 852:
            self.y_player += self.v_player[1]
        rect = pg.rect.Rect(self.x_player - 10, self.y_player - 20, 20, 40)
        screen.blit(self.img, rect)


class Enemy:
    def __init__(self):
        img = pg.image.load('ang.jpg')
        self.Is = pg.transform.smoothscale(img, (10, 10))
        self.x_enemy = randint(100, 1500)
        self.y_enemy = randint(200, 600)
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
        self.mask = pg.mask.from_surface(self.Is)

    def draw_enemy(self, screen, player_x, player_y):
        self.v_enemy = self.enemy_move(player_x, player_y)
        self.x_enemy += self.v_enemy[0]
        self.y_enemy += self.v_enemy[1]
        rect = pg.rect.Rect(self.x_enemy-5, self.y_enemy-5, 10, 10)
        screen.blit(self.Is, rect)
        return self.enemy_shot(player_x, player_y)

    def enemy_shot(self, player_x, player_y):
        self.time = ((
            datetime.datetime.today().hour * 60 * 60
            + datetime.datetime.today().minute * 60
            + datetime.datetime.today().second) * 1000000
            + datetime.datetime.today().microsecond)
        if self.time - self.last_shot >= 4000000 and self.bullets == 0:
            self.bullets = 20
        if (self.able_to and self.time - self.last_shot >= 500000 and self.bullets != 0):
            bullet = Shots().TypeOne()
            cos = (player_x - self.x_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            sin = (player_y - self.y_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            bullet.set_shot(self.x_enemy, self.y_enemy, sin, cos, 1)
            self.bullets -= 1
            self.last_shot = self.time
            return bullet
        else:
            return None

    def enemy_move(self, player_x, player_y):
        r_to_player = ((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5
        if r_to_player >= 300:
            self.able_to = False
            cos = (player_x - self.x_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            sin = (player_y - self.y_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            v_enemy = (3*cos, 3*sin)
            return v_enemy
        else:
            self.able_to = True
        return (0, 0)
