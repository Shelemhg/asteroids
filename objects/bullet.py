# objects/bullet.py

import arcade, math

from objects.flying_object import FlyingObject

from constants import BULLET_RADIUS, BULLET_COLOR


class Bullet(FlyingObject):

    def __init__(self):
        
        super().__init__()
        self.radius = BULLET_RADIUS
        # self.velocity = 0
        self.angle = 0


    def draw(self):

        arcade.draw_circle_filled(self.position.x, self.position.y, 10, BULLET_COLOR)


    def advance(self, delta_time):

        # self.position.x += self.velocity * math.cos(math.radians(self.angle))
        # self.position.y += self.velocity * math.sin(math.radians(self.angle))
        # self.position.x += self.velocity.dx
        # self.position.y += self.velocity.dy


        # Update position based on velocity
        self.position += self.velocity * delta_time
        

    def fire(self, x, y, angle, velocity):
        
        self.angle = angle
        self.velocity += 10
        
        
        self.position.x = x
        self.position.y = y
        self.draw()