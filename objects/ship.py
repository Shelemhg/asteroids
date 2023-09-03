# objects/ship.py

import arcade, math

from objects.flying_object import FlyingObject


from constants import SHIP_TEXTURE, SHIP_WIDTH, SHIP_LENGTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Ship(FlyingObject):
    
    def __init__(self):
        super().__init__()
        self.texture_orientation = +270
        self.position.x = SCREEN_WIDTH / 2
        self.position.y = SCREEN_HEIGHT / 2
        # self.direction = +90
        self.angular_velocity = 0      # Yaw speed of the ship
        # self.dx = 0        # Speed in x
        # self.dy = 0         # Speed in y
        self.height = SHIP_LENGTH
        self.radius = 30
        self.texture = arcade.load_texture(SHIP_TEXTURE)
        # self.velocity = 0
        self.width = SHIP_WIDTH


    def advance(self):
        # Update position based on velocity
        self.position += self.velocity
        # Update orientation based on angular velocity
        self.texture_orientation += self.angular_velocity
        

    def draw(self):
        arcade.draw_texture_rectangle(self.position.x, self.position.y, self.width, self.height, self.texture, self.texture_orientation + 90, self.alpha)
