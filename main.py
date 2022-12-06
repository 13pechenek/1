import datetime
import pygame
from figs import *
from move import *
from Walls import*


pygame.init()

elozh = Push()
img1 = pg.image.load('walllllll.png')
img2 = pg.image.load('waaaaaaaaaaaallllllllll.png')
screen = pygame.display.set_mode((1600, 862))
clock = pygame.time.Clock()
FINISHED = False
player = Player()
bullet = []
enemies = []
for i in range(30):
    e = Enemy()
    enemies.append(e)

while not FINISHED:
    clock.tick(60)
    screen.fill((0, 0, 0))
    v = controlls()
    draw_walls(screen, img1, img2)
    player.v_player = v
    player.draw_player(screen)
    player.our_lives(screen)
    obj = []
    obj.append([player.mask, player.x_player-10, player.y_player-20])
    for e in enemies:
        enemy = e.draw_enemy(screen, player.x_player, player.y_player)
        if enemy is not None:
            bullet.append(enemy)
        if e.lives == 0:
            enemies.remove(e)
        else:
            obj.append([e.mask, e.x_enemy-5, e.y_enemy-5])
    u = elozh.push(player.x_player, player.y_player)

    if u is not None:
        bullet.append(u)
    for b in bullet:
        b.draw_shot(screen)
        t = 0
        fin = False
        if b.bul_x < 5 or b.bul_x > 1595 or b.bul_y < 7 or b.bul_y > 855:
            bullet.remove(b)
            fin = True
        for ob in obj:
            if b.check_shot(ob) and not fin:
                if t == 0 and b.type != 0 and not fin:
                    player.h_player -= 1
                    if player.h_player == 0:
                        FINISHED = True
                    fin = True
                    bullet.remove(b)
                    break
                elif t > 0 and b.type == 0 and not fin:
                    enemies[t-1].lives -= 1
                    fin = True
                    bullet.remove(b)
                    break
            t += 1
        if ((datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond) - b.l_time >= 1000000 and not fin:
            bullet.remove(b)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                FINISHED = True
pygame.quit()
