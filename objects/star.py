# objects/star.py

import random, arcade

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

# Define a Star class
class Star(FlyingObject):

    def __init__(self, x, y, type):
        super().__init__()
        self.position.x = x
        self.position.y = y
        
        if type == "1":
            self.size = random.uniform(STARS_2_MIN_SIZE, STARS_2_MAX_SIZE)
            self.speed = STARS_1_SPEED # Assigned speed of the star
        elif type == "2":
            self.size = random.uniform(STARS_1_MIN_SIZE, STARS_2_MAX_SIZE)
            self.speed = STARS_2_SPEED # Assigned speed of the star
        else:
            self.size = random.uniform(STAR_MIN_SIZE, STAR_MAX_SIZE)
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
    

    def advance(self, delta_time):
        self.position += self.velocity * delta_time

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