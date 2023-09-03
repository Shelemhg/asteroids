# objects/ship.py

import arcade, math

from objects.flying_object import FlyingObject


from constants import (
    SHIP_TEXTURE, 
    SHIP_WIDTH, 
    SHIP_LENGTH, 
    SHIP_RADIUS, 
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
    LEFT_LIMIT,
    RIGHT_LIMIT,
    BOTTOM_LIMIT,
    TOP_LIMIT    
)

class Ship(FlyingObject):
    
    def __init__(self):
        super().__init__()
        self.texture_orientation = +270
        self.position.x = SCREEN_WIDTH / 2
        self.position.y = SCREEN_HEIGHT / 2
        self.angular_velocity = 0      # Yaw speed of the ship
        self.height = SHIP_LENGTH
        self.radius = SHIP_RADIUS
        self.texture = arcade.load_texture(SHIP_TEXTURE)
        self.width = SHIP_WIDTH


    def advance(self):
        # Update position based on velocity
        self.position += self.velocity
            
        # Update orientation based on angular velocity
        self.texture_orientation += self.angular_velocity


    def draw(self):
        arcade.draw_texture_rectangle(self.position.x, self.position.y, self.width, self.height, self.texture, self.texture_orientation + 90, self.alpha)
