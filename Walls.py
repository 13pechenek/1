"""Данный файл содержит команды, которые создают стены"""

import pygame as pg
from random import randint


class WALLS:
    """Отвечает за стены"""
    class horizontal_obstacles:
        """Горизонтальные стены"""

        def __init__(self, mas):
            """Параметры по умолчанию;
               mas - массив(0 - х, 1 - у, 2 - ширина)
            """
            #type - тип стены(h - гор-ая, v - вертик-я), x_wall, y_wall - координаты угла стенки
            self.type_w = 'h'
            self.x_wall = mas[0]
            self.y_wall = mas[1]
            self.heith = 10
            self.width = mas[2]
            self.surface = pg.Surface((self.width, self.heith))
            pg.draw.rect(self.surface, (255, 255, 0),
                        (self.x_wall, self.y_wall, self.width, self.heith))
            self.mask = pg.mask.from_surface(self.surface)

                

        def draw_obstacles(self, screen):
            """Создает препятствие;
               screen - экран
            """
            pg.draw.rect(screen, (255, 255, 0),
                        (self.x_wall, self.y_wall, self.width, self.heith))            
    class vertical_obstacles:
        """Вертикальные стенки"""

        def __init__(self, mas):
            """Параметры по умолчанию;
               mas - массив(0 - х, 1 - у, 2 - высота)
            """
            self.type_w = 'v'
            self.x_wall = mas[0]
            self.y_wall = mas[1]
            self.width = 10
            self.heith = mas[2]
            self.surface = pg.Surface((self.width, self.heith))
            pg.draw.rect(self.surface, (255, 255, 0),
                        (self.x_wall, self.y_wall, self.width, self.heith))
            self.mask = pg.mask.from_surface(self.surface)
        def draw_obstacles(self, screen):
            """Создает препятствие;
               screen - экран
            """

           
            pg.draw.rect(screen, (255, 255, 0),
                        (self.x_wall, self.y_wall, self.width, self.heith))


def draw_walls(screen):
    """Рисует боковые стены:
       screen - экран
    """

    img1 = pg.image.load('images/walllllll.png')
    img2 = pg.image.load('images/waaaaaaaaaaaallllllllll.png')
   
    rect = pg.rect.Rect(0, 0, 1600, 5)
    screen.blit(img1, rect)
    
    rect = pg.rect.Rect(0, 857, 1600, 5)
    screen.blit(img1, rect)
    rect = pg.rect.Rect(30, 0, 40, 862)
    screen.blit(img2, rect)

    rect = pg.rect.Rect(1562, 0, 40, 862)
    screen.blit(img2, rect)





