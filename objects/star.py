# objects/star.py
import arcade
import pygame
import random

from constants import (
    BASE_COLOR,
    COLOR_VARIATION,
    STAR_MIN_SIZE,
    STAR_MAX_SIZE,
    STARS_1_MIN_SIZE,
    STARS_1_MAX_SIZE,
    STARS_2_MIN_SIZE,
    STARS_2_MAX_SIZE,
    STARS_1_SPEED,
    STARS_2_SPEED
)

class Star(arcade.Sprite):
    
    def __init__(self, x, y, type):
        """Initialize a star object.

        Args:
            x (int): X-coordinate to assign to the star.
            y (int): Y-coordinate to assign to the star.
            star_type (int): Type of the star to generate:
                - 0: Background star (no movement).
                - 1: Layer 1 star with variable size and speed.
                - 2: Layer 2 star with variable size and speed.
        """
        super().__init__()

        self.type = type
        self.center_x = x  # Set the x-coordinate of the center of the sprite
        self.center_y = y  # Set the y-coordinate of the center of the sprite
        self.texture = arcade.load_texture("assets/images/star.png")

        if type == 1:
            self.width = self.height = round(random.uniform(STARS_1_MIN_SIZE, STARS_1_MAX_SIZE), 2)
            self.speed = STARS_1_SPEED
        elif type == 2:
            self.width = self.height = round(random.uniform(STARS_2_MIN_SIZE, STARS_2_MAX_SIZE), 2)
            self.speed = STARS_2_SPEED
        else:
            self.width = self.height = round(random.uniform(STAR_MIN_SIZE, STAR_MAX_SIZE), 2)
            self.speed = 0

        self.color = self.generate_random_color()
        self.angle = 0  # Angle at which the star is moving
        self.velocity = pygame.Vector2(0, 0)  # Velocity vector (you can set this as needed)

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
        self.center_x += self.velocity.x
        self.center_y += self.velocity.y

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.right < 0:
            self.left = SCREEN_WIDTH
        elif self.left > SCREEN_WIDTH:
            self.right = 0
        if self.bottom < 0:
            self.top = SCREEN_HEIGHT
        elif self.top > SCREEN_HEIGHT:
            self.bottom = 0
