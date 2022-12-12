from player import*
from enemy import*
from Walls import*


def loading_positions(name, enemies, obstacles):
    data_file = open(name, 'r')
    numbers = [int(x) for x in data_file.readline().split()]
    print(numbers)
    a = [int(x) for x in data_file.readline().split()]
    player = Player(a)
    for i in range(numbers[0]):
        a = [int(x) for x in data_file.readline().split()]
        enemy = Enemy(a)
        enemies.append(enemy)
    for i in range(numbers[1]):
        a = [int(x) for x in data_file.readline().split()]
        h_wall = WALLS.horizontal_obstacles(a)
        obstacles.append(h_wall)
    for i in range(numbers[2]):
        a = [int(x) for x in data_file.readline().split()]
        v_wall = WALLS.vertical_obstacles(a)
        obstacles.append(v_wall)
    return player

