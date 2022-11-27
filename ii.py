import datetime
from figs import Shots


class EnemyTypeOne:
    def __init__(self):
        self.bullets = 20
        self.able_to = True
        self.time = ((
            datetime.datetime.today().hour * 60 * 60
            + datetime.datetime.today().minute * 60
            + datetime.datetime.today().second) * 1000000
            + datetime.datetime.today().microsecond)
        self.last_shot = 0

    def enemy_shot(self, player_x, player_y, self_x, self_y):
        self.time = ((
            datetime.datetime.today().hour * 60 * 60
            + datetime.datetime.today().minute * 60
            + datetime.datetime.today().second) * 1000000
            + datetime.datetime.today().microsecond)
        if self.time - self.last_shot >= 4000000 and self.bullets == 0:
            self.bullets = 20
        if (self.able_to and self.time - self.last_shot >= 500000 and self.bullets != 0):
            bullet = Shots().TypeOne()
            cos = (player_x - self_x)/(((player_x - self_x)**2 + (player_y - self_y)**2)**0.5)
            sin = (player_y - self_y)/(((player_x - self_x)**2 + (player_y - self_y)**2)**0.5)
            bullet.set_shot(self_x, self_y, sin, cos, 1)
            self.bullets -= 1
            self.last_shot = self.time
            return bullet
        else:
            return None

    def enemy_move(self, player_x, player_y, self_x, self_y):
        r_to_player = ((player_x - self_x)**2 + (player_y - self_y)**2)**0.5
        if r_to_player >= 300:
            self.able_to = False
            cos = (player_x - self_x)/(((player_x - self_x)**2 + (player_y - self_y)**2)**0.5)
            sin = (player_y - self_y)/(((player_x - self_x)**2 + (player_y - self_y)**2)**0.5)
            v_enemy = (3*cos, 3*sin)
            return v_enemy
        else:
            self.able_to = True
        return (0, 0)
