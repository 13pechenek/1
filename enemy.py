import datetime
from random import random, randint
import pygame as pg
from shots import *


class Enemy:
    def __init__(self, mas):
        img = pg.image.load('images/enemy.jpg')
        self.Is = pg.transform.smoothscale(img, (10, 10))
        self.x_enemy = mas[0]
        self.y_enemy = mas[1]
        self.v_enemy = (0, 0)
        self.lives = mas[2]
        self.bullets = 20
        self.able_to = True
        self.time = ((
            datetime.datetime.today().hour * 60 * 60
            + datetime.datetime.today().minute * 60
            + datetime.datetime.today().second) * 1000000
            + datetime.datetime.today().microsecond)
        self.last_shot = 0
        self.mask = pg.mask.from_surface(self.Is)
        self.see_player = True

    def draw_enemy(self, screen, player_x, player_y, obstacles):
        self.v_enemy = self.enemy_move(player_x, player_y, obstacles)
        if self.see_player:
            for obst in obstacles:
                if self.mask.overlap_area(obst.mask, (obst.x_wall - self.x_enemy - self.v_enemy[0] + 5 , obst.y_wall - self.y_enemy + 5 )) > 0:
                    self.v_enemy = (0, self.v_enemy[1])
                if self.mask.overlap_area(obst.mask, (obst.x_wall - self.x_enemy + 5 , obst.y_wall - self.v_enemy[1]- self.y_enemy + 5 )) > 0 :
                    self.v_enemy = (self.v_enemy[0], 0)
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
        if (self.able_to and self.time - self.last_shot >= 500000 and self.bullets != 0 and self.see_player):
            bullet = Shots().TypeOne()
            cos = (player_x - self.x_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            sin = (player_y - self.y_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            bullet.set_shot(self.x_enemy, self.y_enemy, sin, cos, 1)
            self.bullets -= 1
            self.last_shot = self.time
            return bullet
        else:
            return None

    def enemy_move(self, player_x, player_y, obstacles):
        t = True
        self.see_player = True
        for o in obstacles:
            if o.type_w == 'h' and t:
                if abs(o.y_wall - self.y_enemy) < abs(player_y-self.y_enemy) and (o.y_wall - self.y_enemy)*(player_y-self.y_enemy)>0:
                    g=[]
                    tan_one = (self.x_enemy-o.x_wall)/(self.y_enemy-o.y_wall+o.heith)
                    tan_two = (self.x_enemy-o.x_wall-o.width)/(self.y_enemy-o.y_wall+o.heith)
                    g.append(max(tan_one,tan_two))
                    g.append(min(tan_one,tan_two))
                    tan_player = (self.x_enemy-player_x)/(self.y_enemy-player_y)
                    if tan_player> g[1] and tan_player<g[0]:
                        self.see_player = False
                        t = False
            if o.type_w == 'v' and t:
                if abs(o.x_wall - self.x_enemy) < abs(player_x-self.x_enemy) and (o.x_wall - self.x_enemy)*(player_x-self.x_enemy)>0:
                    g=[]
                    tan_one = (self.y_enemy-o.y_wall)/(self.x_enemy-o.x_wall)
                    tan_two = (self.y_enemy-o.y_wall-o.heith)/(self.x_enemy-o.x_wall)
                    g.append(max(tan_one, tan_two))
                    g.append(min(tan_one, tan_two))
                    tan_player = (self.y_enemy-player_y)/(self.x_enemy-player_x)
                    if tan_player> g[1] and tan_player<g[0]:
                        self.see_player = False
                        t = False

        distance_to_player = ((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5
        if distance_to_player >= 300:
            self.able_to = False
            cos = (player_x - self.x_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            sin = (player_y - self.y_enemy)/(((player_x - self.x_enemy)**2 + (player_y - self.y_enemy)**2)**0.5)
            v_enemy = (3*cos, 3*sin)
            return v_enemy
        else:
            self.able_to = True
        return (0, 0)
