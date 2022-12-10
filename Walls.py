import pygame as pg
from random import randint



class WALLS:
    def __init__(self):
        self.x1_vertic_wall = randint(100, 500)
        self.y1_vertic_wall = randint(100,400)
        self.x2_vertic_wall = randint(600, 1400)
        self.y2_vertic_wall = randint(100,400)
        self.x1_horizont_wall = randint(100, 1400)
        self.y1_horizont_wall = randint(100,400)
        self.x2_horizont_wall = randint(100, 1400)
        self.y2_horizont_wall = randint(100,400)

    def draw_walls(self, screen):

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



    def draw_obstacles(self, screen):
    
        pg.draw.rect(screen, (255, 255, 0), (self.x1_vertic_wall, self.y1_vertic_wall, 10, 250))
        pg.draw.rect(screen, (255, 255, 0), (self.x2_vertic_wall, self.y2_vertic_wall, 10, 250))
        pg.draw.rect(screen, (255, 255, 0), (self.x1_horizont_wall, self.y1_horizont_wall, 400, 10))
        pg.draw.rect(screen, (255, 255, 0), (self.x2_horizont_wall, self.y2_horizont_wall, 400, 10))



   



   

    





