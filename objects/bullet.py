# objects/bullet.py

import arcade, pygame, math

from objects.flying_object import FlyingObject

from constants import BULLET_RADIUS, BULLET_COLOR


class Bullet(FlyingObject):

    def __init__(self):
        
        super().__init__()
        self.radius = BULLET_RADIUS
        self.direction = 0


    def draw(self):
        # Draw the shape of the bullet using the corresponding function
        arcade.draw_circle_filled(self.position.x, self.position.y, BULLET_RADIUS, BULLET_COLOR)


    def advance(self):
        # Update position based on velocity vector
        self.position += round(self.velocity, 2)
        

    def fire(self, x, y, direction, velocity):
        # Divide the direction angle into its components
        dx = round(-math.cos(math.radians(direction)), 2)
        dy = round(-math.sin(math.radians(direction)), 2)
        # Assign the current direction of the ship to the bullet
        self.direction = round(direction, 2)
        # Assign the current ship velocity (divided into x and y speed) plus the energy of the shot to the bullet velocity
        self.velocity = pygame.Vector2( velocity.x/100 + dx * 10, velocity.y/100 + dy * 10)
        
        # Declare initial position of the bullet
        self.position.x = x
        self.position.y = y