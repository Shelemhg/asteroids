# objects/bullet.py

import arcade, math
from objects.flying_object import FlyingObject

from constants import BULLET_RADIUS, BULLET_COLOR


class Bullet(FlyingObject):

    def __init__(self):
        
        super().__init__()
        self.radius = BULLET_RADIUS
        self.velocity = 0
        self.angle = 0


    def draw(self):

        arcade.draw_circle_filled(self.center.x, self.center.y, 10, BULLET_COLOR)


    def advance(self):

        self.center.x += self.velocity * math.cos(math.radians(self.angle))
        self.center.y += self.velocity * math.sin(math.radians(self.angle))


    def fire(self, x, y, angle, velocity):

        self.angle = angle - 180
        self.velocity = velocity + 10
        self.center.x = x
        self.center.y = y
        self.draw()