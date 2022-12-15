"""При запуске данной программы появляется экран, 
на котором пользователь должен задать
расположение игрока, врагов, вертикальных и горизонтальных стен
"""


import pygame
import datetime
from player import*
from enemy import*
from pygame.locals import *
from Walls import*


# flag, pl_set(установка игрока), en_set(установка врага)
# vwall_shape(установка вертикальных стен),hwall_sеt(установка вертикальных стен)
# hwall_shape(задание размеров стен) - флаги
# nemies, walls - массивы врагов и стен соответственно
# h и v - число горизонтальных и вертикальных стен соответственно


pygame.init()
screen = pygame.display.set_mode((1600,862))
running = True
flag= True
pl_set = True
en_set = False
hwall_set = False
vwall_set = False
vwall_shape = False
hwall_shape = False
h= 0
v=0
enemies = []
walls =[]
clock = pygame.time.Clock()
last_time = 0


 
while running:
    time = datetime.datetime.today().second
    clock.tick(15)
    screen.fill((0,0,0))

    # m - считывание точки нажатия, 1 - чтобы игрок просто отобразился
    if pl_set and pygame.mouse.get_pressed()[0]:
        m = pygame.mouse.get_pos()
        n=[]
        print(m)
        n.append(m[0])
        n.append(m[1])
        n.append(1)
        player = Player(n)
        pl_set=False

    # После нажатия клавиши "d" задаем положения врагов
    if pl_set is False and flag:
        if pygame.key.get_pressed()[K_d]:
            en_set = True
            flag = False
    if pl_set is not True:
        player.draw_player(screen,[])

    # Добавляем каждого нового врага не чаще, чем раз в секунду
    if en_set and pygame.mouse.get_pressed()[0] and abs(time - last_time)>0:
        m = pygame.mouse.get_pos()
        n=[]
        print(m)
        n.append(m[0])
        n.append(m[1])
        n.append(1)
        enemy = Enemy(n)
        enemies.append(enemy)
        last_time = time

    # После нажатия клавиши "k" задаем расположение стен
    if pygame.key.get_pressed()[K_f] and en_set:
        en_set = False
        hwall_set = True
    if hwall_set and pygame.mouse.get_pressed()[0] and not hwall_shape:
        m = pygame.mouse.get_pos()
        n=[]
        print(m)
        n.append(m[0])
        n.append(m[1])
        n.append(100)
        hwall = WALLS.horizontal_obstacles(n)
        walls.append(hwall)
        hwall_shape = True
        h+=1

    # Регулируем длину/высоту стены нажатим верхней/нижней стрелочки
    if hwall_shape and pygame.key.get_pressed()[K_DOWN]:
        walls[len(walls)-1].width -= 5
    if hwall_shape and pygame.key.get_pressed()[K_UP]:
        walls[len(walls)-1].width += 5
    # Нажимаем пробел, чтобы создать новую стену
    if hwall_shape and pygame.key.get_pressed()[K_SPACE]:
        hwall_set = False
        hwall_shape = False
        vwall_set = True
    if pygame.key.get_pressed()[K_s] and hwall_set:
        hwall_shape = False
    if vwall_set and pygame.mouse.get_pressed()[0] and not vwall_shape:
        m = pygame.mouse.get_pos()
        n=[]
        print(m)
        n.append(m[0])
        n.append(m[1])
        n.append(100)
        vwall = WALLS.vertical_obstacles(n)
        walls.append(vwall)
        vwall_shape = True
        v+=1
    if vwall_shape and pygame.key.get_pressed()[K_DOWN]:
        walls[len(walls)-1].heith -=5
    if vwall_shape and pygame.key.get_pressed()[K_UP]:
        walls[len(walls)-1].heith +=5
    if pygame.key.get_pressed()[K_s] and vwall_set:
        vwall_shape = False

    
    for e in enemies:
        pygame.draw.rect(screen, (255,0,0), (e.x_enemy-5, e.y_enemy-5, 10, 10))
    for w in walls:
        pygame.draw.rect(screen, (255,0,0), (w.x_wall, w.y_wall, w.width, w.heith))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_ESCAPE]:
                running = False


# Сохранение уровня в файл, название которому дается после нажатия esc(при выходе)
if not running:
    pygame.quit()
    st = input()+'.txt'
    level_struc = open(st, 'w')
    level_struc.write(str(len(enemies))+' '+str(h)+' '+str(v)+'\n')
    level_struc.write(str(player.x_player)+' '+str(player.y_player)+' 5'+'\n')
    for e in enemies:
        level_struc.write(str(e.x_enemy)+' '+str(e.y_enemy)+' 1'+'\n')
    for w in walls:
        if w.type_w == 'h':
            level_struc.write(str(w.x_wall)+' '+str(w.y_wall)+' '+str(w.width)+'\n')
        else:
            level_struc.write(str(w.x_wall)+' '+str(w.y_wall)+' '+str(w.heith)+'\n')
