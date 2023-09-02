# objects/star.py

import random, math
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
)

# Define a Star class
class Star(FlyingObject):

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        if type == "1":
            self.size = random.uniform(STARS_2_MIN_SIZE, STARS_2_MAX_SIZE)
        elif type == "2":
            self.size = random.uniform(STARS_1_MIN_SIZE, STARS_2_MAX_SIZE)
        else:
            self.size = random.uniform(STAR_MIN_SIZE, STAR_MAX_SIZE)

        self.color = self.generate_random_color()
        self.velocity = 0  # Speed of the star
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
    

    def advance(self, delta_time):
        self.x += self.dx
        self.y += self.dy


    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        if self.x > SCREEN_WIDTH:
            self.x = 0

        elif self.x < 0:
            self.x = SCREEN_WIDTH

        if self.y > SCREEN_HEIGHT:
            self.y = 0

        elif self.y < 0:
            self.y = SCREEN_HEIGHT