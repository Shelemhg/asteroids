# objects/asteroid.py

import arcade
import math
import pygame
import random

from objects.flying_object import FlyingObject

from constants import (
    BIG_ROCK_TEXTURE,
    BIG_ROCK_SPEED,
    BIG_ROCK_SPIN,
    BIG_ROCK_RADIUS,
    MEDIUM_ROCK_TEXTURE,
    MEDIUM_ROCK_SPEED,
    MEDIUM_ROCK_SPIN,
    MEDIUM_ROCK_RADIUS,
    SMALL_ROCK_TEXTURE,
    SMALL_ROCK_SPEED,
    SMALL_ROCK_SPIN,
    SMALL_ROCK_RADIUS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class Asteroid(FlyingObject):

    def __init__(self, size, x, y, direction):
        """
        Creates an asteroid object
        
        Args:
            size (string): Size of the asteroid to create
            x, y (float): X and Y values for the spawn position of the asteroid
            direction (float): Angle of the bullet that impacted the asteroid or 0
        """
        super().__init__()
        self.size = size      # Size of the asteroid "Big", "Medium" or "Small"
        
        self.position.x = x      # Position in X of the ship on spawn
        self.position.y = y      # Position in Y of the ship on spawn
        
        self.texture_orientation = direction      # Angle of the asteroid's texture on spawn (pointing upwards)
        self.rotation_direction = random.randint(0, 1)  # Assign a random rotation direction


        if size == "Big":
            # Load the asteroid's texture
            self.texture = arcade.load_texture(BIG_ROCK_TEXTURE)
            # Assign a random movement in both x and y components, either possitive or negative
            self.velocity = pygame.Vector2(round(random.uniform(-BIG_ROCK_SPEED, BIG_ROCK_SPEED), 2), round(random.uniform(-BIG_ROCK_SPEED, BIG_ROCK_SPEED), 2))
            # Define the speed of the spin of the asteroid
            self.angular_velocity = BIG_ROCK_SPIN
            # Declares the radius of the asteroid to calculate impact distance to bullets and ship
            self.radius = BIG_ROCK_RADIUS
            
        elif size == "Medium":
            # Load the asteroid's texture
            self.texture = arcade.load_texture(MEDIUM_ROCK_TEXTURE)
            # Define the speed of the spin of the asteroid
            self.angular_velocity = MEDIUM_ROCK_SPIN
            # Obtain the X and Y components from the "direction" angle
            dx = -math.cos(math.radians(direction))
            dy = -math.sin(math.radians(direction))
            # Assigns to the velocity vector, the values from the "dx" and "dy" components multiplied by the rock speed constant
            self.velocity = round(pygame.Vector2((self.velocity.x + dx) * MEDIUM_ROCK_SPEED , (self.velocity.y + dy) * MEDIUM_ROCK_SPEED), 2)
            # Declares the radius of the asteroid to calculate impact distance to bullets and ship
            self.radius = MEDIUM_ROCK_RADIUS
            
        else:
            # Load the asteroid's texture
            self.texture = arcade.load_texture(SMALL_ROCK_TEXTURE)
            # Define the speed of the spin of the asteroid
            self.angular_velocity = SMALL_ROCK_SPIN
            # Obtain the X and Y components from the "direction" angle
            dx = -math.cos(math.radians(direction))
            dy = -math.sin(math.radians(direction))
            # Assign a random movement in both x and y components, either possitive or negative
            self.velocity = round(pygame.Vector2((self.velocity.x + dx) * SMALL_ROCK_SPEED , (self.velocity.y + dy) * SMALL_ROCK_SPEED), 2)
            # Declares the radius of the asteroid to calculate impact distance to bullets and ship
            self.radius = SMALL_ROCK_RADIUS
        # Defines the width and height value from the same values of the texture
        self.width = self.texture.width
        self.height = self.texture.height
        
        # Checks if the asteroid created is big, if so, it means that the game just started, so now it will check if the asteroids are too close to the middle, 
        # which is where the spaceship is located, and if so, they should move further away from the spaceship 
        if size == "Big":
            
            if (self.position.x > SCREEN_WIDTH / 2 - SCREEN_WIDTH / 4 and self.position.x < SCREEN_WIDTH / 2 + SCREEN_WIDTH / 4) and (
                    self.position.y > SCREEN_HEIGHT / 2 - SCREEN_WIDTH / 4 and self.position.y < SCREEN_HEIGHT / 2 + SCREEN_WIDTH / 4):
                if self.position.x > SCREEN_WIDTH / 2:
                    self.position.x += SCREEN_WIDTH / 4
                else:
                    self.position.x -= SCREEN_WIDTH / 4
                if self.position.y > SCREEN_HEIGHT / 2:
                    self.position.y += SCREEN_HEIGHT / 4
                else:
                    self.position.y -= SCREEN_HEIGHT / 4



    def advance(self):
        
        # MOVE the asteroid based on its velocity
        self.position += round(self.velocity, 2)
        
        # ROTATE either clockwise or counter clockwise, at its angular velocity
        if self.rotation_direction == 0:
            self.texture_orientation += round(self.angular_velocity, 2)
        else:
            self.texture_orientation -= round(self.angular_velocity, 2)