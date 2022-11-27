import pygame as pg

def draw_walls(screen, cord_mas, img1, img2):
    

    
    rect = pg.rect.Rect(0, 0, 1600, 5)
    screen.blit(img1, rect)
    
    rect = pg.rect.Rect(0, 857, 1600, 5)
    screen.blit(img1, rect)

    

    rect = pg.rect.Rect(30, 0, 40, 862)
    screen.blit(img2, rect)

    rect = pg.rect.Rect(1562, 0, 40, 862)
    screen.blit(img2, rect)







