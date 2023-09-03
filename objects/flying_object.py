# objects/flying_object.py

import arcade, pygame

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
        self.radius = 0
        self.alpha = 255
        self.texture = None




    def draw(self):

        arcade.draw_texture_rectangle(
            self.position.x,
            self.position.y,
            self.width,
            self.height,
            self.texture,
            self.texture_orientation,
            self.alpha
        )


    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        if self.position.x > (SCREEN_WIDTH + self.radius):
            self.position.x = -self.radius

        elif self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH - self.radius

        if self.position.y > (SCREEN_HEIGHT + self.radius):
            self.position.y = -self.radius

        elif self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT - self.radius