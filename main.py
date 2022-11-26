import pygame
from figs import*
from move import*
from ii import*

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
finished = False
v=(0,0)
player = Player()
player.__init__()
enemy = enemy_type1()
bullet=[]

while not finished:
    clock.tick(60)
    screen.fill((0,0,0))
    v = controlls(v)
    player.v = v
    player.draw_player(screen)
    draw_enemy(screen, 500, 500)
    tbul = enemy.enemy_shot(player.x_player, player.y_player, 500, 500)
    if tbul != None:
        bullet.append(tbul)
    for b in bullet:
        b.draw_shot(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                finished= True
pygame.quit()
