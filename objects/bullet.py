# objects/bullet.py

import arcade 
import pygame
import math

from objects.flying_object import FlyingObject

from constants import BULLET_RADIUS, BULLET_COLOR, BULLET_SPEED


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
        """
        Function called by the Arcade framework every time a keyboard key is pressed.
        Inside the function, specific actions will be performed if specific keys 
        were pressed (SPACE - Fire bullet, ENTER - Restart Game, ESCAPE - Exit game)

        Args:
            key ()
            delta_time (float): The time elapsed since the last update.
        """
        # Divide the direction angle into its components
        dx = round(-math.cos(math.radians(direction)), 2)
        dy = round(-math.sin(math.radians(direction)), 2)
        # Assign the current direction of the ship to the bullet
        self.direction = round(direction, 2)
        # Assign the current ship velocity (divided into x and y speed) plus the energy of the shot to the bullet velocity
        self.velocity = pygame.Vector2( velocity.x/100 + dx * BULLET_SPEED, velocity.y/100 + dy * BULLET_SPEED)
        
        # Declare initial position of the bullet
        self.position.x = x
        self.position.y = y
        
    def bullet_is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        if self.position.x > (SCREEN_WIDTH + self.radius):
            self.alive = False

        elif self.position.x < -self.radius:
            self.alive = False

        if self.position.y > (SCREEN_HEIGHT + self.radius):
            self.alive = False

        elif self.position.y < -self.radius:
            self.alive = False