# objects/flying_object.py

import arcade

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0


class FlyingObject:

    def __init__(self):

        self.center = Point()
        self.radius = 0
        self.alive = True
        self.texture = None
        self.angle = 0
        self.width = 0
        self.height = 0
        self.alpha = 255


    def draw(self):

        arcade.draw_texture_rectangle(
            self.center.x,
            self.center.y,
            self.width,
            self.height,
            self.texture,
            self.angle + 90,
            self.alpha
        )


    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        if self.center.x > (SCREEN_WIDTH + self.radius):
            self.center.x = -self.radius

        elif self.center.x < -self.radius:
            self.center.x = SCREEN_WIDTH - self.radius

        if self.center.y > (SCREEN_HEIGHT + self.radius):
            self.center.y = -self.radius

        elif self.center.y < -self.radius:
            self.center.y = SCREEN_HEIGHT - self.radius