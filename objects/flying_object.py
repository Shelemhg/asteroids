# objects/flying_object.py

import arcade
import pygame

class FlyingObject:

    def __init__(self):

        # Game object properties        
        self.alive = True        
        self.texture_orientation = 0
        self.position = pygame.Vector2(0, 0)  # 2D position vector
        self.velocity = pygame.Vector2(0, 0)  # 2D velocity vector

        # Visual properties
        self.width = 0
        self.height = 0
        self.alpha = 255
        self.texture = None
        self.radius = 0


    def draw(self):
        """
        Function called by diverse objects on "on_draw".
        
        It draw the texture of the objects according to their characteristics.
        """
        arcade.draw_texture_rectangle(
            self.position.x,
            self.position.y,
            self.width,
            self.height,
            self.texture,
            self.texture_orientation,
            self.alpha
        )


    def is_off_screen(self, screen_width, screen_height):
        """
        Function called by the update method on game.py.
        
        It calculates if a flying object is off screen and if so it moves it to the oposite side.

        Args:
            screen_width (int): width of the window in pixels.
            screen_height (int): height of the window in pixels.
        """
        
        if self.position.x > (screen_width + self.radius):
            self.position.x = -self.radius

        elif self.position.x < -self.radius:
            self.position.x = screen_width - self.radius

        if self.position.y > (screen_height + self.radius):
            self.position.y = -self.radius

        elif self.position.y < -self.radius:
            self.position.y = screen_height - self.radius