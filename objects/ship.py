# objects/ship.py

import arcade
from objects.flying_object import FlyingObject


from constants import SHIP_TEXTURE, SHIP_WIDTH, SHIP_LENGTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Ship(FlyingObject):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(SHIP_TEXTURE)
        self.width = SHIP_WIDTH
        self.height = SHIP_LENGTH
        self.angle = -90
        self.velocity = 0
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.direction = +90
        self.dx = 0
        self.dy = 0
        self.dYaw = 0
        self.radius = 30

    def advance(self, delta_time):
        self.center.x += self.dx
        self.center.y += self.dy
        self.angle += self.dYaw

    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture,
                                      self.angle + 90, self.alpha)
