# objects/bullet.py

import arcade, pygame, math

from objects.flying_object import FlyingObject

from constants import BULLET_RADIUS, BULLET_COLOR


class Bullet(FlyingObject):

    def __init__(self):
        
        super().__init__()
        self.radius = BULLET_RADIUS
        # self.velocity = 0
        self.direction = 0


    def draw(self):

        arcade.draw_circle_filled(self.position.x, self.position.y, 10, BULLET_COLOR)


    def advance(self, delta_time):
        # Update position based on velocity
        self.position += self.velocity
        

    def fire(self, x, y, direction, velocity):
        
        dx = -math.cos(math.radians(direction))
        dy = -math.sin(math.radians(direction))
        
        self.direction = direction
        # self.velocity = pygame.Vector2(velocity.x * 1.2, velocity.y * 1.2)
        # self.velocity = pygame.Vector2( velocity.x + dx * 2, velocity.y + dy * 2)
        self.velocity = pygame.Vector2( velocity.x/100 + dx * 10, velocity.y/100 + dy * 10)
        
        
        self.position.x = x
        self.position.y = y
        # self.draw()