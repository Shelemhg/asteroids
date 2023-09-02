# objects/asteroid.py

import arcade
from objects.flying_object import FlyingObject
import random
import math

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

    def __init__(self, size, x, y):

        super().__init__()
        self.size = size

        if size == "Big":
            self.texture = arcade.load_texture(BIG_ROCK_TEXTURE)
            self.speed = BIG_ROCK_SPEED
            self.spin = BIG_ROCK_SPIN
            self.radius = BIG_ROCK_RADIUS
        elif size == "Medium":
            self.texture = arcade.load_texture(MEDIUM_ROCK_TEXTURE)
            self.speed = MEDIUM_ROCK_SPEED
            self.spin = MEDIUM_ROCK_SPIN
            self.radius = MEDIUM_ROCK_RADIUS
        else:
            self.texture = arcade.load_texture(SMALL_ROCK_TEXTURE)
            self.speed = SMALL_ROCK_SPEED
            self.spin = SMALL_ROCK_SPIN
            self.radius = SMALL_ROCK_RADIUS

        # This following condition checks if the asteroid created is big, and if so, it means that the game just started, so now it will check if the asteroids are too close to the middle, 
        # which is where the spaceship is located, and if so, they should move further away from the spaceship 

        if size == "Big":
            
            if (x > SCREEN_WIDTH / 2 - SCREEN_WIDTH / 4 and x < SCREEN_WIDTH / 2 + SCREEN_WIDTH / 4) and (
                    y > SCREEN_HEIGHT / 2 - SCREEN_WIDTH / 4 and y < SCREEN_HEIGHT / 2 + SCREEN_WIDTH / 4):
                if x > SCREEN_WIDTH / 2:
                    x += SCREEN_WIDTH / 4
                else:
                    x -= SCREEN_WIDTH / 4
                if y > SCREEN_HEIGHT / 2:
                    y += SCREEN_HEIGHT / 4
                else:
                    y -= SCREEN_HEIGHT / 4

        self.center.x = x
        self.center.y = y
        self.direction = random.uniform(0, 360)

        self.width = self.texture.width
        self.height = self.texture.height
        self.angle = 0
        self.rotation_direction = random.randint(0, 1)
        self.hit_points = 0


    def advance(self, delta_time):

        self.center.x += math.cos(math.radians(self.direction)) * self.speed * 30 * delta_time
        self.center.y += math.sin(math.radians(self.direction)) * self.speed * 30 * delta_time

        if self.rotation_direction == 0:
            self.angle += self.spin
        else:
            self.angle -= self.spin