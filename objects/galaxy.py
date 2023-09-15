# objects/galaxy.py
import arcade
import pygame
import random

from constants import (
    BASE_COLOR,
    COLOR_VARIATION,
    STARS_1_SPEED
)

class Galaxy(arcade.Sprite):
    
    def __init__(self, x, y):
        """Initialize a galaxy object.

        Args:
            x (int): X-coordinate to assign to the galaxy.
            y (int): Y-coordinate to assign to the galaxy.
        """
        super().__init__()

        self.type = type     # Type of the galaxy to create, either 0, 1 or 2 
        self.center_x = x     # Set the x-coordinate of the center of the sprite
        self.center_y = y     # Set the y-coordinate of the center of the sprite
        self.texture = arcade.load_texture("assets/images/galaxy1.gif")
        
        # Assign the width, height and speed of the galaxys based on the type of galaxyt to be created
        self.width = 100
        self.height = 100
        
        self.speed = STARS_1_SPEED

        self.color = self.generate_random_color()
        self.angle = 0  # Angle at which the galaxy is moving
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
        
        # Update the position of the galaxy with an increment based on its velocity vector
        self.center_x += self.velocity.x
        self.center_y += self.velocity.y


    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        # If the galaxy is off screen, update its position so it now shows on the oposite side of the screen
        if self.right < 0:
            self.left = SCREEN_WIDTH
        elif self.left > SCREEN_WIDTH:
            self.right = 0
        if self.bottom < 0:
            self.top = SCREEN_HEIGHT
        elif self.top > SCREEN_HEIGHT:
            self.bottom = 0
