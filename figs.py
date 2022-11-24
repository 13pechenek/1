import pygame as pg


class Player:
    def __init__(self):
        self.x_player = 300
        self.y_player = 300
        self.v = (0, 0)

    def draw_player(self, screen):
        self.x_player += self.v[0]
        self.y_player += self.v[1]
        pg.draw.polygon(
            screen,
            (0, 255, 0),
            [
                (self.x_player + 5, self.y_player +5),
                (self.x_player - 5, self.y_player + 5),
                (self.x_player - 5, self.y_player - 5),
                (self.x_player + 5, self.y_player - 5)
                ]
                )


def draw_enemy(screen, x_enemy, y_enemy):
    pg.draw.polygon(
        screen,
        (255, 0, 0),
        [
            (x_enemy+5, y_enemy+5),
            (x_enemy-5, y_enemy+5),
            (x_enemy-5, y_enemy-5),
            (x_enemy+5, y_enemy-5)])


class DrawBullet:
    def type_1(self, screen, x_bullet, y_bullet):
        pg.draw.circle(screen, (255, 255, 0), (x_bullet, y_bullet), 3)

