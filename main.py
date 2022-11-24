import pygame
from figs import*
from move import*


pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
finished = False
v=(0,0)
player = Player()
player.__init__()

while not finished:
    clock.tick(60)
    screen.fill((0,0,0))
    v = controlls(v)
    player.v = v
    player.draw_player(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                finished= True
pygame.quit()
