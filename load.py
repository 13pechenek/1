"""Данный файл содержит команду,
считывающую положение и жизни врагов и игрока с файла,
а также считывающую с файла положение стен из файла
"""

from player import Player
from enemy import Enemy
from Walls import Walls


def loading_positions(file_name, enemies, obstacles):
    """Считывание положений и жизней врагов и игрока,
    считывание положений стен из файла(file_name)"""
    data_file = open(file_name, 'r')
    numbers = [int(x) for x in data_file.readline().split()]
    a = [int(x) for x in data_file.readline().split()]
    player = Player(a)
    for i in range(numbers[0]):
        a = [int(x) for x in data_file.readline().split()]
        enemy = Enemy(a)
        enemies.append(enemy)
    for i in range(numbers[1]):
        a = [int(x) for x in data_file.readline().split()]
        h_wall = Walls.HorizontalObstacles(a)
        obstacles.append(h_wall)
    for i in range(numbers[2]):
        a = [int(x) for x in data_file.readline().split()]
        v_wall = Walls.VerticalObstacles(a)
        obstacles.append(v_wall)
    return player
