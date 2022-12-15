"""Файл с командами, отвечающими за выстрелы в заданных направлениях и управление движением игрока"""


import pygame
from player import *
from enemy import *
from pygame.locals import *
 # from datetime import *  

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}


def controlls():
    """Управление движением нажатием на стрелки"""
    # player_v - скорость игрока
    player_v = (0, 0)
    if pygame.key.get_pressed()[K_LEFT]:
        player_v = (dir[K_LEFT][0], dir[K_LEFT][1])
    if pygame.key.get_pressed()[K_RIGHT]:
        player_v = (player_v[0] + dir[K_RIGHT][0], player_v[1] + dir[K_RIGHT][1])
    if pygame.key.get_pressed()[K_UP]:
        player_v = (player_v[0] + dir[K_UP][0], player_v[1] + dir[K_UP][1])
    if pygame.key.get_pressed()[K_DOWN]:
        player_v = (player_v[0] + dir[K_DOWN][0], player_v[1] + dir[K_DOWN][1])
    return player_v





class FirePlayer: 
    """Класс, отвечающий за стрельбу"""
    def __init__(self):
        """Параметры по умолчанию
        """
        self.flag =False        
        self.bullets = 10
        self.time = (datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond
        self.last_shot = 0
        # datetime.timestamp(datetime.now())  #

    def fire(self , player_x, player_y):
        """1. Реализует перезарядку 2. При нажатии выпускает пули, летящие в указанном(нажатием) направлении; возвращает пули
        player_x - х-координата игрока
        player_y - у-координата игрока"""
        if pygame.mouse.get_pressed()[0]:
            self.time =  (datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond
            if self.time - self.last_shot >= 4000000 and self.bullets == 0:
                self.bullets = 10
            if (self.time - self.last_shot >= 500000 and self.bullets != 0):
                self.sin = -(player_y - pygame.mouse.get_pos()[1]) / ((player_x - pygame.mouse.get_pos()[0])**2 + (player_y - pygame.mouse.get_pos()[1])**2)**0.5
                self.cos = -(player_x - pygame.mouse.get_pos()[0]) / ((player_x -pygame.mouse.get_pos()[0])**2 + (player_y - pygame.mouse.get_pos()[1])**2)**0.5
                bullet = Shots().TypeOne()
                bullet.set_shot(player_x, player_y, self.sin, self.cos, 0)
                self.last_shot = self.time
                self.bullets-=1
                return bullet