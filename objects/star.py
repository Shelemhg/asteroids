# objects/star.py

import arcade
import pygame
import random

from objects.flying_object import FlyingObject
from constants import (
    BASE_COLOR,
    COLOR_VARIATION,
    STAR_MIN_SIZE,
    STAR_MAX_SIZE,
    STARS_1_MIN_SIZE,
    STARS_2_MAX_SIZE,
    STARS_2_MIN_SIZE,
    STARS_2_MAX_SIZE,
    STARS_1_SPEED,
    STARS_2_SPEED
)

# class Star(FlyingObject):
class Star(arcade.Sprite):

    def __init__(self, x, y, type):
        
        super().__init__()
        """
        Draw stars from the specified list.

        Args:
            stars_list (List[Star]): The list of stars to draw.
        """     
        self.type = type
        # Variables for regular list
        # self.position.x = x
        # self.position.y = y
        
        # Variables for Sprite Object
        self.position = pygame.Vector2(x, y)  # 2D position vector
        self.velocity = pygame.Vector2(0, 0)  # 2D velocity vector
        
        
        
        if type == 1:
            self.size = round(random.uniform(STARS_2_MIN_SIZE, STARS_2_MAX_SIZE), 2)
            self.speed = STARS_1_SPEED # Assigned speed of the star
        elif type == 2:
            self.size = round(random.uniform(STARS_1_MIN_SIZE, STARS_2_MAX_SIZE), 2)
            self.speed = STARS_2_SPEED # Assigned speed of the star
        else:
            self.size = round(random.uniform(STAR_MIN_SIZE, STAR_MAX_SIZE), 2)
            self.speed = 0

        self.color = self.generate_random_color()
        self.angle = 0  # Angle at which the star is moving
        self.dx = 0
        self.dy = 0

    
    def generate_random_color(self):
        # Choose a random base color
        base_color = random.choice(BASE_COLOR)

        # Generate slight variations in RGB components
        r, g, b = base_color
        r_variation = random.randint(-COLOR_VARIATION, COLOR_VARIATION)
        g_variation = random.randint(-COLOR_VARIATION, COLOR_VARIATION)
        b_variation = random.randint(-COLOR_VARIATION, COLOR_VARIATION)

        # Ensure color components stay within valid range (0-255)
        r = max(0, min(255, r + r_variation))
        g = max(0, min(255, g + g_variation))
        b = max(0, min(255, b + b_variation))
        
        return (r, g, b)
    

    def advance(self):
        self.position += self.velocity

    def draw(self):
        arcade.draw_point(self.position.x, self.position.y, self.color, self.size)
            
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT