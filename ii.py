import math
import datetime
from figs import shots

class enemy_type1:
    def __init__(self):
        self.bullets = 20
        a = datetime.datetime.today()
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
        if (self.able_to and self.time - self.last_shot >= 1000000 and self.bullets != 0):
            bullet = shots().type_1()
            cos = (player_x - self_x)/(((player_x - self_x)**2 + (player_y - self_y)**2)**0.5)
            sin = (player_y - self_y)/(((player_x - self_x)**2 + (player_y - self_y)**2)**0.5)
            bullet.set_shot(self_x, self_y, sin, cos)
            self.bullets -= 1
            self.last_shot = self.time
            return bullet
        else:
            return None
