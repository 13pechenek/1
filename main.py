import datetime
import pygame
from player import *
from enemy import *
from move import *
from Walls import*
from load import*


pygame.init()

fire = FirePlayer()
screen = pygame.display.set_mode((1600, 862))
clock = pygame.time.Clock()
FINISHED = False

bullet = []
enemies = []
obstacles = []
player = loading_positions('set.txt', enemies, obstacles)

while not FINISHED:
    clock.tick(60)
    screen.fill((0, 0, 0))
    v = controlls()
    draw_walls(screen)
    for o in obstacles:
        o.draw_obstacles(screen)
    player.v_player = v
    player.draw_player(screen, obstacles)
    player.our_lives(screen)
    object = []
    object.append([player.mask, player.x_player-10, player.y_player-20])
    for e in enemies:
        enemy = e.draw_enemy(screen, player.x_player, player.y_player, obstacles)
        if enemy is not None:
            bullet.append(enemy)
        if e.lives == 0:
            enemies.remove(e)
        else:
            object.append([e.mask, e.x_enemy-5, e.y_enemy-5])
    f = fire.fire(player.x_player, player.y_player)

    

    if f is not None:
        bullet.append(f)
    for BULLETS in bullet:
        BULLETS.draw_shot(screen)
        t = 0
        finish = False
        if BULLETS.bullet_x < 5 or BULLETS.bullet_x > 1595 or BULLETS.bullet_y < 7 or BULLETS.bullet_y > 855:
            bullet.remove(BULLETS)
            finish = True
        for g in obstacles:
            a = [g.mask, g.x_wall, g.y_wall]
            if BULLETS.check_shot(a):
                finish = True
                bullet.remove(BULLETS)
                break
        for obj in object:
            if BULLETS.check_shot(obj) and not finish:
                if t == 0 and BULLETS.type != 0 and not finish:
                    player.health_player -= 1
                    if player.health_player == 0:
                        FINISHED = True
                    finish = True
                    bullet.remove(BULLETS)
                    break
                elif t > 0 and BULLETS.type == 0 and not finish:
                    enemies[t-1].lives -= 1
                    finish = True
                    bullet.remove(BULLETS)
                    break
            t += 1
        if ((datetime.datetime.today().hour * 60 * 60 + datetime.datetime.today().minute * 60 + datetime.datetime.today().second) * 1000000 + datetime.datetime.today().microsecond) - BULLETS.l_time >= 1000000 and not finish:
            bullet.remove(BULLETS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                FINISHED = True
pygame.quit()
