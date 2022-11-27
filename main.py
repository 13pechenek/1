import datetime
import pygame
from figs import *
from move import *


pygame.init()

elozh = Push()

screen = pygame.display.set_mode((1600, 862))
clock = pygame.time.Clock()
FINISHED = False
player = Player()
bullet = []
bullet_cord = []
player_and_walls_cord = []
enemies =[]
for i in range(5):
    e = Enemy()
    enemies.append(e)

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


while not FINISHED:
    clock.tick(60)
    screen.fill((0,0,0))
    v = controlls()
    player.v_player = v
    player.draw_player(screen, player_and_walls_cord)
    f = 0
    for e in enemies:
        f+=1
        tbul = e.draw_enemy(screen, player_and_walls_cord,f,player.x_player, player.y_player)
        if tbul is not None:
            bullet.append(tbul)
    u = elozh.push(player.x_player, player.y_player)
    if u is not None:
        bullet.append(u)
    for b in bullet:
        b.draw_shot(screen, bullet_cord, player_and_walls_cord, len(enemies))
        if b.h_pl:
            player.h_player -= 1
        if b.h_en != 0:
            enemies[b.h_en-1].lives -=1
            if enemies[b.h_en-1].lives == 0:
                enemies.remove(enemies[b.h_en-1])
        if player.h_player == 0:
            FINISHED = True


        if ((datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond) - b.l_time >= 1000000 or b.live == 0:
            bullet.remove(b)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                FINISHED = True
pygame.quit()
