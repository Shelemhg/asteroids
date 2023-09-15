"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import arcade
import gc
from pyglet.window.key import S
import random
from random import randint
import math
import pygame, sys
from pygame import mixer

pygame.mixer.init()
mixer.music.load('assets/sounds/adagio_for_strings_tiesto.wav')
mixer.music.play(-1)

# These are Global constants to use throughout the game
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 900

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_COLOR = arcade.color.BRIGHT_GREEN

SHIP_TEXTURE = "assets/images/spaceship.png"
SHIP_TEXTURE2 = "assets/images/spaceship2.png"
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25/4
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_TEXTURE = "assets/images/meteorGrey_big1.png"
BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_TEXTURE = "assets/images/meteorGrey_medium1.png"
MEDIUM_ROCK_SPEED = 1.5
MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_TEXTURE = "assets/images/meteorGrey_small1.png"
SMALL_ROCK_SPEED = 7
SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2



class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

class Flying_object:
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
        #for the correct drawing of the Ship this angle was set to +90 so it could show pointing up
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle +90 , self.alpha)

    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.center.x > (SCREEN_WIDTH + self.radius):
            self.center.x = -self.radius
        elif self.center.x < -self.radius:
            self.center.x = SCREEN_WIDTH -self.radius

        if self.center.y > (SCREEN_HEIGHT + self.radius):
            self.center.y = -self.radius
        elif self.center.y < -self.radius:
            self.center.y = SCREEN_HEIGHT -self.radius

class Asteroid(Flying_object):
    def __init__(self, size, x, y, direction):
        super().__init__()
        if size == "Big":
            self.texture = arcade.load_texture(BIG_ROCK_TEXTURE)
            self.speed = BIG_ROCK_SPEED
            self.spin = BIG_ROCK_SPIN
            self.radius = 30
        elif size == "Medium":
            self.texture = arcade.load_texture(MEDIUM_ROCK_TEXTURE)
            self.speed = MEDIUM_ROCK_SPEED
            self.spin = MEDIUM_ROCK_SPIN
            self.radius = 5
        else:
            self.texture = arcade.load_texture(SMALL_ROCK_TEXTURE)
            self.speed = SMALL_ROCK_SPEED
            self.spin = SMALL_ROCK_SPIN
            self.radius = 2
        self.size = size
        # This following condition is to judge if the asteroids being created are big it means that the game just started, the starship is in the center and they
        # should not spwawn too close or else they should move further  ofthe spaceship 
        if size == "Big":
            if (x > SCREEN_WIDTH/2 - SCREEN_WIDTH/4 and x < SCREEN_WIDTH/2 + SCREEN_WIDTH/4) and (y > SCREEN_HEIGHT/2 - SCREEN_WIDTH/4 and y < SCREEN_HEIGHT/2 + SCREEN_WIDTH/4):
                if x > SCREEN_WIDTH/2:
                    x+=SCREEN_WIDTH/4
                else:
                    x-=SCREEN_WIDTH/4

                if y > SCREEN_HEIGHT/2:
                    y+=SCREEN_HEIGHT/4
                else:
                    y-=SCREEN_HEIGHT/4

        self.center.x = x
        self.center.y = y
        self.direction = direction
        
        self.width = self.texture.width
        self.height = self.texture.height
        self.angle = 0
        self.rotation_direction = random.randint(0,1)

        self.hit_points = 0
        
        

    def advance(self, delta_time):
        self.center.x += math.cos(math.radians(self.direction)) * self.speed * 30 * delta_time
        self.center.y += math.sin(math.radians(self.direction)) * self.speed * 30 * delta_time

        
        if self.rotation_direction == 0:
            self.angle += self.spin
        else:
            self.angle -= self.spin





class Bullet(Flying_object):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.velocity = 0
        self.angle = 0
        
    def draw(self):
        # arcade.draw_circle_filled(100, 100, BULLET_RADIUS, BULLET_COLOR)
        arcade.draw_circle_filled(self.center.x, self.center.y, 10, BULLET_COLOR)

    def advance(self):
        # Move the bullet by updating the center location
        ...
        self.center.x += self.velocity * math.cos(math.radians(self.angle))
        self.center.y += self.velocity * math.sin(math.radians(self.angle))
        
    # Defines the angle of the gun by receiving the angle of the cursor and updating its position   
    def fire(self, x, y, angle, velocity):
        self.angle = angle -180
        self.velocity = velocity + 10
        self.center.x = x
        self.center.y = y
        self.draw()
        ...

class Ship(Flying_object):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(SHIP_TEXTURE)
        self.width = self.texture.width/10
        self.height = self.texture.height/10
        self.angle = -90
        self.velocity = 0
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.direction = +90
        self.dx = 0
        self.dy = 0
        self.radius = 30
    
    # def advance(self, delta_time, direction):
    #     #The angle is actually pointing originally left so we made it turn 90 degrees
    #     self.center.y -= math.sin(math.radians(direction)) * self.velocity * 30 * delta_time
    #     self.center.x -= math.cos(math.radians(direction)) * self.velocity * 30 * delta_time

    def advance(self, delta_time):
        # #The angle is actually pointing originally left so we made it turn 90 degrees
        # self.center.x -= math.cos(math.radians(self.direction)) * self.dx * delta_time
        # self.center.y -= math.sin(math.radians(self.direction)) * self.dy * delta_time

        
        self.center.x += self.dx
        self.center.y += self.dy

    def draw(self):
        #for the correct drawing of the Ship this angle was set to +90 so it could show pointing up
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle +90 , self.alpha)

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """

        
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()
        self.timer = 0
        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        
        
        self.bullets = []
        self.asteroids = []
        
        for new_asteroid in range(INITIAL_ROCK_COUNT):
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            direction = random.uniform(0,360)
            new_asteroid = Asteroid("Big", x, y, direction)
            
            self.asteroids.append(new_asteroid)



    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # EXTODO: draw each object
        self.ship.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

        for bullet in self.bullets:
            bullet.draw()
        
        

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        # TODO: Tell everything to advance or move forward one step in time
        if self.ship.alive == True:

            self.check_keys(delta_time)
            self.check_collisions()

            self.ship.advance(delta_time)
            self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

            for asteroid in self.asteroids:
                asteroid.advance(delta_time)

            for bullet in self.bullets:
                bullet.advance()
            

        # TODO: Check for collisions
            for asteroid in self.asteroids:
                asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

            for bullet in self.bullets:
                bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)


    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """
        for asteroid in self.asteroids:
            too_close_ship = 30 + asteroid.radius
            if (abs(self.ship.center.x - asteroid.center.x) < too_close_ship and
                                abs(self.ship.center.y - asteroid.center.y) < too_close_ship): 
                self.ship.velocity = 0
                self.ship.alive = False

            for bullet in self.bullets:
            
                
                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:
                    too_close = 30 + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        asteroid.alive = False
                        if asteroid.size == "Big":
                            self.asteroids.append(Asteroid("Medium", asteroid.center.x, asteroid.center.y, bullet.angle + 45))
                            self.asteroids.append(Asteroid("Small", asteroid.center.x, asteroid.center.y, bullet.angle))
                            self.asteroids.append(Asteroid("Medium", asteroid.center.x, asteroid.center.y, bullet.angle - 45))
                        elif asteroid.size == "Medium":
                            self.asteroids.append(Asteroid("Small", asteroid.center.x, asteroid.center.y, bullet.angle + 45))
                            self.asteroids.append(Asteroid("Small", asteroid.center.x, asteroid.center.y, bullet.angle - 45))


                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def check_keys(self, delta_time):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += 3

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= 3

        if arcade.key.UP in self.held_keys:
            self.ship.dx -= math.cos(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            self.ship.dy -= math.sin(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            if random.randint(0,1) == 0: 
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE2)
            else:
                self.ship.texture = arcade.load_texture(SHIP_TEXTURE)

        if arcade.key.DOWN in self.held_keys:
            self.ship.dx += math.cos(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            self.ship.dy += math.sin(math.radians(self.ship.angle)) * SHIP_THRUST_AMOUNT
            # self.ship.advance()
            # self.ship.velocity -= SHIP_THRUST_AMOUNT
        
        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        self.held_keys.add(key)

        if key == arcade.key.SPACE:
            # TODO: Fire the bullet here!
            bullet = Bullet()
            bullet.fire(
                self.ship.center.x, 
                self.ship.center.y,
                self.ship.angle,
                self.ship.velocity)
                
            self.bullets.append(bullet)
        if key == arcade.key.ENTER:
            self.ship.center.x = SCREEN_WIDTH/2
            self.ship.center.y = SCREEN_HEIGHT/2

            del self.ship
            del self.bullets
            del self.asteroids

            self.ship = Ship()

            self.bullets = []
            self.asteroids = []
            
            for new_asteroid in range(INITIAL_ROCK_COUNT):
                x = random.uniform(0, SCREEN_WIDTH)
                y = random.uniform(0, SCREEN_HEIGHT)
                direction = random.uniform(0,360)
                new_asteroid = Asteroid("Big", x, y, direction)
                
                self.asteroids.append(new_asteroid)
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            
            self.ship.texture = arcade.load_texture(SHIP_TEXTURE)

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
                # self.bullets.remove(bullet)
                # self.score -= 1

        for asteroid in self.asteroids:
            asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
                # asteroid.relocate()
                # points = target.hit_points
                # self.targets.remove(target)
                # Removes a point for each target gone
                # self.score -= points * 2 
    def close_window():
        """
        Closes the current window, and then runs garbage collection. The garbage collection
        is necessary to prevent crashing when opening/closing windows rapidly (usually during
        unit tests).
        """
        global _window

        Game.close()

        # Have to do a garbage collection or Python will crash
        # if we do a lot of window open and closes. Like for
        # unit tests.
        gc.collect()


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()