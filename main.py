"""Здесь запускается игра"""

import datetime
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN
from inputs import controlls, FirePlayer
from Walls import draw_walls
from load import loading_positions


pygame.init()

fire = FirePlayer()
screen = pygame.display.set_mode((1600, 862))
clock = pygame.time.Clock()
FINISHED = False

back_img = pygame.image.load('images/backs.jpeg')
back_ground = pygame.transform.smoothscale(back_img, (1600, 862))
bullet = []
enemies = []
obstacles = []
player = loading_positions('level1.txt', enemies, obstacles)

while not FINISHED:
    clock.tick(60)
    screen.blit(back_ground, (0, 0))
    v = controlls()
    draw_walls(screen)
    for o in obstacles:
        o.draw_obstacles(screen)
    player.v_player = v
    player.draw_player(screen, obstacles)
    player.our_lives(screen)
    objects = []
    objects.append([player.mask, player.x_player-10, player.y_player-20])
    for e in enemies:
        enemy = e.draw_enemy(
            screen,
            player.x_player,
            player.y_player,
            obstacles)
        if enemy is not None:
            bullet.append(enemy)
        if e.lives == 0:
            enemies.remove(e)
        else:
            objects.append([e.mask, e.x_enemy-5, e.y_enemy-5])
    f = fire.fire(player.x_player, player.y_player)
    if f is not None:
        bullet.append(f)
    for BULLETS in bullet:
        BULLETS.draw_shot(screen)
        t = 0
        FINISH = False
        if (
                BULLETS.bullet_x < 5 or
                BULLETS.bullet_x > 1595 or
                BULLETS.bullet_y < 7 or
                BULLETS.bullet_y > 855):
            bullet.remove(BULLETS)
            FINISH = True
        for g in obstacles:
            a = [g.mask, g.x_wall, g.y_wall]
            if BULLETS.check_shot(a):
                FINISH = True
                bullet.remove(BULLETS)
                break
        for obj in objects:
            if BULLETS.check_shot(obj) and not FINISH:
                if t == 0 and BULLETS.type != 0 and not FINISH:
                    player.health_player -= 1
                    if player.health_player == 0:
                        FINISHED = True
                        G_O = True
                    FINISH = True
                    bullet.remove(BULLETS)
                    break
                elif t > 0 and BULLETS.type == 0 and not FINISH:
                    enemies[t-1].lives -= 1
                    FINISH = True
                    bullet.remove(BULLETS)
                    break
            t += 1
        if (
                (
                    (
                        (
                            datetime.datetime.today().hour * 60 * 60
                            + datetime.datetime.today().minute * 60
                            + datetime.datetime.today().second) * 1000000
                        + datetime.datetime.today().microsecond)
                    - BULLETS.l_time >= 1000000) and
                not FINISH):
            bullet.remove(BULLETS)
    pygame.display.update()
    if not enemies:
        G_O = False
        FINISHED = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                FINISHED = True
                G_O = True
FINISHED = False
while not FINISHED:
    if not G_O:
        img = pygame.image.load('images/win.jpeg')
        img = pygame.transform.smoothscale(img, (1600, 860))
        screen.blit(img, (0, 0))
        pygame.display.update()
    else:
        img = pygame.image.load('images/loose.png')
        img = pygame.transform.smoothscale(img, (1600, 860))
        screen.blit(img, (0, 0))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                FINISHED = True
pygame.quit()
