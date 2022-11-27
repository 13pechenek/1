import pygame

def draw_walls(screen, cord_mas):
    pygame.draw.line(screen, (255,255,255), (0,0),(1600,0), (10))
    pygame.draw.line(screen, (255,255,255), (1600,862),(1600,0), (80))
    pygame.draw.line(screen, (255,255,255), (1600,862),(0,862), (10))
    pygame.draw.line(screen, (255,255,255), (0,862),(0,0), (80))