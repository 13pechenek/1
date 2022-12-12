import pygame as pg
from random import randint


class WALLS:
    class horizontal_obstacles:

        def __init__(self, mas):
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
            pg.draw.rect(screen, (255, 255, 0),
                        (self.x_wall, self.y_wall, self.width, self.heith))            
    class vertical_obstacles:

        def __init__(self, mas):
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

           
            pg.draw.rect(screen, (255, 255, 0),
                        (self.x_wall, self.y_wall, self.width, self.heith))








def draw_walls(screen):

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





