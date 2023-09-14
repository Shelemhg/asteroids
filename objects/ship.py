# objects/ship.py

import arcade

from objects.flying_object import FlyingObject


from constants import (
    SHIP_TEXTURE, 
    SHIP_WIDTH, 
    SHIP_LENGTH,
    SCREEN_WIDTH,
    SHIP_RADIUS,
    SCREEN_HEIGHT
)

class Ship(FlyingObject):
    
    def __init__(self):
        """
        Creates a Ship object
        
        Args:
            No arguments are received as the Ship is only created at the begining of every attempt
            and is placed in the center of the screen
        """
        super().__init__()
        self.angular_velocity = 0      # Current turn speed of the ship
        self.position.x = SCREEN_WIDTH / 2      # Position in X of the ship on spawn
        self.position.y = SCREEN_HEIGHT / 2      # Position in Y of the ship on spawn
        self.height = SHIP_LENGTH      # Length of the ship to render the texture
        self.width = SHIP_WIDTH      # Width of the ship to render the texture
        self.texture = arcade.load_texture(SHIP_TEXTURE)      # Loading of the ship's image
        self.texture_orientation = +270      # Angle of the ship's image on spawn (pointing upwards)
        self.radius = SHIP_RADIUS      # Distance to calculate if the object is_off_screen() 
        self.shots = 0     # Number of shots done in order to calculate final score

    def advance(self):
        # Update position based on ts own velocity vector (x, y)
        self.position += self.velocity
            
        # Update orientation based on angular velocity
        self.texture_orientation += self.angular_velocity
        # Prevent texture_orientation to become more than 360 or negative and restarting the variable to a positive value between 0 and 360
        if self.texture_orientation > 360:
            self.texture_orientation = 0
        elif self.texture_orientation < 0:
            self.texture_orientation = 360


    def draw(self):
        # Defines the parameters to draw a rectangle filled with the ship.texture image
        arcade.draw_texture_rectangle(self.position.x, self.position.y, self.width, self.height, self.texture, self.texture_orientation + 90, self.alpha)
