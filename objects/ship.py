# objects/ship.py

import arcade
from objects.flying_object import FlyingObject


from constants import SHIP_TEXTURE, SHIP_WIDTH, SHIP_LENGTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Ship(FlyingObject):
    def __init__(self):
        super().__init__()
        self.angle = -90
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.direction = +90
        self.dYaw = 0
        self.dx = 0
        self.dy = 0
        self.height = SHIP_LENGTH
        self.radius = 30
        self.texture = arcade.load_texture(SHIP_TEXTURE)
        self.velocity = 0
        self.width = SHIP_WIDTH


    def advance(self, delta_time):
        self.center.x += self.dx
        self.center.y += self.dy
        self.angle += self.dYaw

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture,
                                      self.angle + 90, self.alpha)
