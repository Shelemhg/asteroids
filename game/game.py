# game/game.py

import arcade
import random
import math
from objects.asteroid import Asteroid
from objects.bullet import Bullet
from objects.ship import Ship
from objects.star import Star


from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SHIP_THRUST_AMOUNT,
    SHIP_TEXTURE,
    SHIP_TEXTURE_THRUST,
    SHIP_TEXTURE_REVERSE,
    SHIP_TURN_AMOUNT,
    SHIP_TEXTURE_LEFT_TURN,
    SHIP_TEXTURE_RIGHT_TURN,
    INITIAL_ROCK_COUNT,
    NUMBER_OF_BACKGROUND_STARS,
    NUMBER_OF_STARS_1,
    NUMBER_OF_STARS_2,
    STARS_1_SPEED,
    STARS_2_SPEED,
)


class AsteroidsGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        self.timer = 0
        self.ship = Ship()
        self.bullets = []
        self.asteroids = []

        self.dx = 0
        self.dy = 0

        # Initialize asteroids at the start of the game
        for new_asteroid in range(INITIAL_ROCK_COUNT):
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            new_asteroid = Asteroid("Big", x, y)
            self.asteroids.append(new_asteroid)

        # Initialize the list of Stars
        self.background_stars = []
        self.stars_1 = []
        self.stars_2 = []


        # Generate stars for each layer
        self.generate_stars(self.background_stars, NUMBER_OF_BACKGROUND_STARS, "")
        self.generate_stars(self.stars_1, NUMBER_OF_STARS_1, "1")
        self.generate_stars(self.stars_2, NUMBER_OF_STARS_2, "2")


    def generate_stars(self, stars_list, num_stars, type):
        for _ in range(num_stars):
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            star = Star(x, y, type)
            stars_list.append(star)

    # Draw objects 60 times per second
    def on_draw(self):

        arcade.start_render()
        # This will draw the objects in layers in the same order they where rendered
         
        # Draw stars
        self.draw_stars(self.background_stars)
        self.draw_stars(self.stars_1)
        self.draw_stars(self.stars_2)


        # Draw ship, asteroids, and bullets
        self.ship.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()
        
        # If the ship is not alive, draw the "Game Over" text and instructions to continue.
        if not self.ship.alive:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.WHITE, font_size=50, anchor_x="center")
            arcade.draw_text("Press ESC to Exit", SCREEN_WIDTH // 8, 40,
                             arcade.color.WHITE, font_size=20, anchor_x="left")
            arcade.draw_text("Press ENTER to Restart", SCREEN_WIDTH - SCREEN_WIDTH // 8, 40,
                             arcade.color.WHITE, font_size=20, anchor_x="right")
            
    
    def draw_stars(self, stars_list):
        
        for star in stars_list:
            arcade.draw_point(star.x, star.y, star.color, star.size)


    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed

        """
        # If the ship is still alive (hasn't been hit) then keep updating all the objects positions
        if self.ship.alive:

            self.check_keys(delta_time)
            self.check_collisions()
            self.ship.advance(delta_time)
            self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
            # Update the position of all the Asteroids
            for asteroid in self.asteroids:

                asteroid.advance(delta_time)
                asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
            # Update the position of all the Bullets
            for bullet in self.bullets:

                bullet.advance()
                bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

            # S T A R S
            # --------------
            # Update the position of the far_stars
            for star in self.stars_1:
                star.advance(delta_time)
                star.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
            
            # Update the position of the close_stars
            for star in self.stars_2:
                star.advance(delta_time)
                star.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)


    def update_star_positions(self, stars_list, ship_velocity, delta_time):
        for star in stars_list:
            # Calculate the change in star's position based on its angle and speed
            dx = math.cos(math.radians(star.angle)) * star.speed * delta_time
            dy = math.sin(math.radians(star.angle)) * star.speed * delta_time

            # Update the star's position
            star.x += dx - ship_velocity[0]
            star.y += dy - ship_velocity[1]

            # Wrap stars around the screen
            if star.x < 0:
                star.x = SCREEN_WIDTH
                star.y = random.uniform(0, SCREEN_HEIGHT)
      

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.

        """
        for asteroid in self.asteroids:

            too_close_ship = 30 + asteroid.radius
            # Check if the ship is too close from an asteroid, if so, stop the spaceship and kill the spaceship.
            if (abs(self.ship.center.x - asteroid.center.x) < too_close_ship and
                    abs(self.ship.center.y - asteroid.center.y) < too_close_ship):
                
                self.ship.velocity = 0
                self.ship.alive = False

            for bullet in self.bullets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:

                    too_close = 30 + asteroid.radius
                    # If the position in X is greater than too_close then kill both the bullet and the asteroid
                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                            abs(bullet.center.y - asteroid.center.y) < too_close):
                        
                        bullet.alive = False
                        asteroid.alive = False

                         # Split of big asteroids into smaller ones upon impact of bullet
                        if asteroid.size == "Big":

                            self.asteroids.append(Asteroid("Medium", asteroid.center.x, asteroid.center.y, bullet.angle + 45))
                            self.asteroids.append(Asteroid("Small", asteroid.center.x, asteroid.center.y, bullet.angle))
                            self.asteroids.append(Asteroid("Medium", asteroid.center.x, asteroid.center.y, bullet.angle - 45))

                        elif asteroid.size == "Medium":

                            self.asteroids.append(Asteroid("Small", asteroid.center.x, asteroid.center.y, bullet.angle + 45))
                            self.asteroids.append(Asteroid("Small", asteroid.center.x, asteroid.center.y, bullet.angle - 45))
        self.cleanup_dead_objects()


    def cleanup_dead_objects(self):

        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)


    def check_keys(self, delta_time):

        """
        Check for key presses and update the ship's behavior accordingly.
        """

        if arcade.key.UP in self.held_keys:
            # Calculate the size of each component from its current angle
            ship_dx = math.cos(math.radians(self.ship.angle))
            ship_dy = math.sin(math.radians(self.ship.angle))

            self.ship.dx -= ship_dx * SHIP_THRUST_AMOUNT
            self.ship.dy -= ship_dy * SHIP_THRUST_AMOUNT

            # Update movement of stars
            for star in self.stars_1:
                star.dx += ship_dx * STARS_1_SPEED
                star.dy += ship_dy * STARS_1_SPEED

            for star in self.stars_2:
                star.dx += ship_dx * STARS_2_SPEED
                star.dy += ship_dy * STARS_2_SPEED


            # Draw the different texture
            if random.randint(0, 1) == 0:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE_THRUST)
            else:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE)


        if arcade.key.DOWN in self.held_keys:
            # Calculate the size of each component from its current angle
            ship_dx = math.cos(math.radians(self.ship.angle))
            ship_dy = math.sin(math.radians(self.ship.angle))

            # Apply thrust to the ship and change its texture
            self.ship.dx += ship_dx * SHIP_THRUST_AMOUNT
            self.ship.dy += ship_dy * SHIP_THRUST_AMOUNT

            # Update movement of stars
            for star in self.stars_1:
                star.dx -= ship_dx * STARS_1_SPEED
                star.dy -= ship_dy * STARS_1_SPEED

            for star in self.stars_2:
                star.dx -= ship_dx * STARS_2_SPEED
                star.dy -= ship_dy * STARS_2_SPEED

            # Draw the different texture
            if random.randint(0, 1) == 0:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE_REVERSE)
            else:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE)


        if arcade.key.LEFT in self.held_keys:
            # self.ship.angle += 3
            self.ship.dYaw += SHIP_TURN_AMOUNT

            # Draw the different texture
            if random.randint(0, 1) == 0:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE_LEFT_TURN)
            else:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE)


        if arcade.key.RIGHT in self.held_keys:
            # self.ship.angle -= 3
            self.ship.dYaw -= SHIP_TURN_AMOUNT

            # Draw the different texture
            if random.randint(0, 1) == 0:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE_RIGHT_TURN)
            else:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE)


    def on_key_press(self, key, modifiers):

        self.held_keys.add(key)

        if key == arcade.key.SPACE:
            if self.ship.alive:
                bullet = Bullet()
                bullet.fire(self.ship.center.x, self.ship.center.y, self.ship.angle, self.ship.velocity)
                self.bullets.append(bullet)

        if key == arcade.key.ENTER:

            self.ship.center.x = SCREEN_WIDTH / 2
            self.ship.center.y = SCREEN_HEIGHT / 2
            del self.ship
            del self.bullets
            del self.asteroids
            self.ship = Ship()
            self.bullets = []
            self.asteroids = []

            for star in self.stars_1:
                # star.velocity = 0
                # star.angle = 0
                star.dx = 0
                star.dy = 0
            
            for star in self.stars_2:
                # star.velocity = 0
                # star.angle = 0
                star.dx = 0
                star.dy = 0

            for new_asteroid in range(INITIAL_ROCK_COUNT):

                x = random.uniform(0, SCREEN_WIDTH)
                y = random.uniform(0, SCREEN_HEIGHT)
                new_asteroid = Asteroid("Big", x, y)
                self.asteroids.append(new_asteroid)

        if key == arcade.key.ESCAPE:
            # Quit Game
            arcade.close_window()


    def on_key_release(self, key, modifiers):
        
        if key in self.held_keys:

            self.held_keys.remove(key)
            self.ship.texture = arcade.load_texture(SHIP_TEXTURE)