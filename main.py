import pygame
from figs import*
from move import*
from ii import*
import datetime

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
finished = False
v=(0,0)
player = Player()
player.__init__()
enemy = enemy_type1()
bullet=[]
x_en = 500
y_en = 500

while not finished:
    clock.tick(60)
    screen.fill((0,0,0))
    v = controlls(v)
    player.v = v
    player.draw_player(screen)
    draw_enemy(screen, x_en, y_en)
    v_en = enemy.enemy_move(player.x_player, player.y_player, x_en, y_en)
    x_en += v_en[0]
    y_en += v_en[1]
    tbul = enemy.enemy_shot(player.x_player, player.y_player, x_en, y_en)
    if tbul != None:
        bullet.append(tbul)
    for b in bullet:
        b.draw_shot(screen)
        if ((datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond) - b.l_time >= 2000000:
            bullet.remove(b)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                finished= True
pygame.quit()
