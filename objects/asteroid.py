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

    def __init__(self, size, x, y, angle):

        super().__init__()
        self.size = size
        
        self.position.x = x
        self.position.y = y
        
        # self.texture_orientation = random.randint(0, 360)
        self.texture_orientation = angle
        self.rotation_direction = random.randint(0, 1)
        self.hit_points = 0


        if size == "Big":
            self.texture = arcade.load_texture(BIG_ROCK_TEXTURE)
            # Assign a random movement in both x and y components, either possitive or negative
            self.velocity = pygame.Vector2(random.uniform(-BIG_ROCK_SPEED, BIG_ROCK_SPEED), random.uniform(-BIG_ROCK_SPEED, BIG_ROCK_SPEED))
            self.angular_velocity = BIG_ROCK_SPIN
            self.radius = BIG_ROCK_RADIUS
        elif size == "Medium":
            self.texture = arcade.load_texture(MEDIUM_ROCK_TEXTURE)
            # Assign a random movement in both x and y components, either possitive or negative
            self.velocity = pygame.Vector2(random.uniform(-MEDIUM_ROCK_SPEED,MEDIUM_ROCK_SPEED), random.uniform(-MEDIUM_ROCK_SPEED, MEDIUM_ROCK_SPEED))
            self.angular_velocity = MEDIUM_ROCK_SPIN
            self.radius = MEDIUM_ROCK_RADIUS
        else:
            self.texture = arcade.load_texture(SMALL_ROCK_TEXTURE)
            # Assign a random movement in both x and y components, either possitive or negative
            self.velocity = pygame.Vector2(random.uniform(-SMALL_ROCK_SPEED,SMALL_ROCK_SPEED), random.uniform(-SMALL_ROCK_SPEED, SMALL_ROCK_SPEED))
            self.angular_velocity = SMALL_ROCK_SPIN
            self.radius = SMALL_ROCK_RADIUS

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



    def advance(self, delta_time):
        
        # MOVE based on velocity
        self.position += self.velocity
        
        # ROTATE either clockwise or counter clockwise, based on angular velocity
        if self.rotation_direction == 0:
            self.texture_orientation += self.angular_velocity
        else:
            self.texture_orientation -= self.angular_velocity
        
        # self.texture_orientation += self.angular_velocity