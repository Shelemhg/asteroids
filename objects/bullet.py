# objects/bullet.py

import arcade 
import pygame
import math

from objects.flying_object import FlyingObject

from constants import BULLET_RADIUS, BULLET_COLOR, BULLET_SPEED


class Bullet(FlyingObject):

    def __init__(self):
        """
        Creates a bullet object
        
        Args:
            No arguments are given here as the object will later be handle by the fire() function
        """
        
        super().__init__()
        self.radius = BULLET_RADIUS  # Size of the bullet
        self.direction = 0  # Angle of movement of the bullet


    def draw(self):
        # Draw the shape of the bullet using the corresponding arcade function
        arcade.draw_circle_filled(self.position.x, self.position.y, BULLET_RADIUS, BULLET_COLOR)


    def advance(self):
        # Update the bullet's position based on its velocity vector
        self.position += round(self.velocity, 2)
        

    def fire(self, x, y, direction, velocity):
        """
        Function called when the SPACE key is pressed
        It sets the position and the characteristics of the bullet

        Args:
            x, y (float): X and Y coordinates that will indicate the position of the bullet, on fire() they are the same as the current ship's position
            direction(float): Current angle of the ship texture (from 0-360)
            velocity (Vector(x, y)): Current velocity vector of the ship
        """
        # Split the direction angle into its X and Y components
        dx = round(-math.cos(math.radians(direction)), 2)
        dy = round(-math.sin(math.radians(direction)), 2)
        # Assign the current direction of the ship to the bullet
        self.direction = round(direction, 2)
        # Add the current ship's velocity (divided into x and y speed) to the energy of the shot to the bullet velocity (ship's speed + bullet's speed)
        self.velocity = pygame.Vector2( velocity.x/100 + dx * BULLET_SPEED, velocity.y/100 + dy * BULLET_SPEED)
        
        # Assign the current ship's position to the bullet
        self.position.x = x
        self.position.y = y
    
    
    def bullet_is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        # Check if a bullet reaches an edge of the screen, if so, delete the bullet
        
        if self.position.x > (SCREEN_WIDTH + self.radius):
            self.alive = False

        elif self.position.x < -self.radius:
            self.alive = False

        if self.position.y > (SCREEN_HEIGHT + self.radius):
            self.alive = False

        elif self.position.y < -self.radius:
            self.alive = False