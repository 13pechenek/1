import datetime
import pygame
from figs import *
from move import *
from ii import *


pygame.init()

elozh = Push()

screen = pygame.display.set_mode((1600, 862))
clock = pygame.time.Clock()
FINISHED = False
player = Player()
enemy = EnemyTypeOne()
bullet = []
bullet_cord = []
player_and_walls_cord = []
for i in range(1600):
    a=[]
    for j in range(862):
        a.append(0)
    bullet_cord.append(a)
for i in range(1600):
    a=[]
    for j in range(862):
        a.append(0)
    player_and_walls_cord.append(a)
X_EN = 500
Y_EN = 500

while not FINISHED:
    clock.tick(60)
    screen.fill((0, 0, 0))
    v = controlls()
    player.v_player = v
    player.draw_player(screen, player_and_walls_cord)
    draw_enemy(screen, X_EN, Y_EN)
    v_en = enemy.enemy_move(player.x_player, player.y_player, X_EN, Y_EN)
    X_EN += v_en[0]
    Y_EN += v_en[1]
    tbul = enemy.enemy_shot(player.x_player, player.y_player, X_EN, Y_EN)
    if tbul is not None:
        bullet.append(tbul)
    u = elozh.push(player.x_player, player.y_player)
    if u is not None:
        bullet.append(u)
    for b in bullet:
        b.draw_shot(screen, bullet_cord, player_and_walls_cord)
        if ((datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond) - b.l_time >= 1000000 or b.live == 0:
            bullet.remove(b)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                FINISHED = True
pygame.quit()
