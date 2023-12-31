# game/game.py
"""
My version of the classic Asteroids game
Copyright: shelemhg 2023
"""

import arcade
import math
import pygame
import random

from arcade import gui
from menu import Menu
from objects.asteroid import Asteroid
from objects.bullet import Bullet
from objects.ship import Ship
from objects.star import Star
from objects.galaxy import Galaxy


from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SHIP_THRUST_AMOUNT,
    SHIP_RETRO_THRUST_AMOUNT,
    SHIP_TEXTURE,
    SHIP_TEXTURE_THRUST,
    SHIP_TEXTURE_REVERSE,
    SHIP_TURN_AMOUNT,
    SHIP_TEXTURE_LEFT_TURN,
    SHIP_TEXTURE_RIGHT_TURN,
    SHIP_RADIUS,
    ENERGY_SOUND,
    ENERGY_SOUND_VOLUME,    
    LARGE_ROCK_POINTS,
    ENERGY,
    ENERGY_INCREASE,    
    MEDIUM_ROCK_POINTS,
    INITIAL_ROCK_COUNT,
    NUMBER_OF_BACKGROUND_STARS,
    NUMBER_OF_STARS_1,
    NUMBER_OF_STARS_2,
    NUMBER_OF_GALAXIES,
    SMALL_ROCK_POINTS,
    PENALTY_PER_SHOT,
    MAIN_ENGINE_SOUND,
    MAIN_ENGINE_SOUND_VOLUME,
    BACKGROUND_MUSIC,
    BACKGROUND_MUSIC_VOLUME,    
    SHOOTING_SOUND,
    SHOOTING_SOUND_VOLUME,
    EXPLOSION_SOUND,
    EXPLOSION_SOUND_VOLUME,
    MEDIUM_EXPLOSION_SOUND,
    MEDIUM_EXPLOSION_SOUND_VOLUME,
    SMALL_EXPLOSION_SOUND,
    SMALL_EXPLOSION_SOUND_VOLUME,
    BULLET_RADIUS
)


class AsteroidsGame(arcade.Window):
    """
    Main game class for the Asteroids game.

    Attributes:    
        ship (Ship): The player's spaceship.
        held_keys (set): Store held keys.
        bullets (list): Store active bullets.
        asteroids (list): Store active asteroids.
        stars (arcade.SpriteList): Store stars.
        background_stars (arcade.SpriteList): Store background stars.
    """
    
    def __init__(self, width, height, screen_title, difficulty):
        """
        Initialize the game window and other game-related objects.

        Args:
            width (int): The width of the game window.
            height (int): The height of the game window.
        """
        
        super().__init__(width, height, screen_title)
        
        # Pause the game at the start to show Menu first
        self.pause = True
        
        # Initialize a variable to store the selected difficulty
        self.difficulty = difficulty
        
        # Initialize values
        self.bullet_radius = BULLET_RADIUS
        self.penalty_per_shot = PENALTY_PER_SHOT
        self.initial_rock_count = INITIAL_ROCK_COUNT
        
        # Create a Menu instance
        self.menu = Menu(self)
        
        # Show the difficulty selection screen
        self.menu.show_menu_screen()
        
        # Load all different textures and get them ready for later use
        self.ship_texture = arcade.load_texture(SHIP_TEXTURE)
        self.thrust_texture = arcade.load_texture(SHIP_TEXTURE_THRUST)
        self.reverse_texture = arcade.load_texture(SHIP_TEXTURE_REVERSE)
        self.left_turn_texture = arcade.load_texture(SHIP_TEXTURE_LEFT_TURN)
        self.right_turn_texture = arcade.load_texture(SHIP_TEXTURE_RIGHT_TURN)
        
        # Initialize objects        
        self.ship = Ship()
        self.held_keys = set()
        self.bullets = []     # List to contain all the Bullet objects
        self.asteroids = []     # List to contain all the Asteroid objects
        
        self.score = 0     # points counter
        self.highest_score = 0        
        self.energy = ENERGY     # energy for shots
        self.level = None
        self.energy_cost_per_shot = None
        self.max_energy = ENERGY
               
        self.energy_increase = ENERGY_INCREASE
        

        # Initialize Stars
        self.stars = arcade.SpriteList()
        self.background_stars = arcade.SpriteList()     #  We separate this ones as they will not move or update their position   
        self.galaxies = arcade.SpriteList()
        
        # Generate stars for each layer
        self.generate_stars(self.background_stars, NUMBER_OF_BACKGROUND_STARS, 0)      
        self.generate_stars(self.stars, NUMBER_OF_STARS_1, 1)
        self.generate_stars(self.stars, NUMBER_OF_STARS_2, 2)
        self.generate_galaxies(self.galaxies , NUMBER_OF_GALAXIES)

        # Initialize a random position for all asteroids and save them in their corresponding list
        for new_asteroid in range(self.initial_rock_count):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            new_asteroid = Asteroid("Big", x, y, 0)
            self.asteroids.append(new_asteroid)
            
            
        # SOUND settings
        pygame.mixer.init()
        pygame.mixer.set_num_channels(7)
        self.background_music_channel = pygame.mixer.Channel(0)     # Background music
        self.main_engine_music_channel = pygame.mixer.Channel(1)    # Sound when moving forward
        self.shooting_music_channel = pygame.mixer.Channel(2)    # Sound when activating thrusters
        self.channel3 = pygame.mixer.Channel(3)    # Explosion Big Rocks
        self.channel4 = pygame.mixer.Channel(4)     # Explosion Medium Rocks
        self.channel5 = pygame.mixer.Channel(5)     # Explosion Small Rocks
        self.channel6 = pygame.mixer.Channel(6)     # Explosion Small Rocks
        # Start playing background music
        self.background_music_channel.play(pygame.mixer.Sound(BACKGROUND_MUSIC))
        self.background_music_channel.set_volume(BACKGROUND_MUSIC_VOLUME)  

        
          
    def generate_stars(self, stars_list, num_stars, type):
        """
        Receives a list for storage, the number and type of stars to save in it. Then it generates a random location on screen for each star and then it adds it to the list of stars.

        Args:
            s h e l e m h g 2023
            stars_list (List[Star]): The list of stars to draw.
            num_stars (int): Number of stars to generate
            type (int): Type of stars to generate: Background = 0, Layer1 = 1, Layer2 = 2      
        """
        for _ in range(num_stars):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            star = Star(x, y, type)
            stars_list.append(star)


    def generate_galaxies(self, galaxies_list, num_galaxies):
        """
        Receives a list for storage and the number of galaxies to save in it. Then it generates a random location on screen for each galaxy and then it adds it to the list of galaxies.
        
        Args:
            stars_list (List[Star]): The list of stars to draw.
            num_stars (int): Number of stars to generate
            type (int): Type of stars to generate: Background = 0, Layer1 = 1, Layer2 = 2
        """
        for _ in range(num_galaxies):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            galaxy = Galaxy(x, y)
            galaxies_list.append(galaxy)
    
    
    def on_draw(self):
        """
        Arcade framework will automatically call this method  to render the objects 
        from back to front in the same order of the code.

        """
        arcade.start_render() 
        
        # If game is not paused, render all the objects: stars, ship, asteroids, bullets
        if self.pause is False:
            
            arcade.set_background_color(arcade.color.BLACK)
            # Draw stars per layer, first background, then the rest of the layers
            self.background_stars.draw()
            self.stars.draw()
            self.galaxies.draw()

            # Draw ship, asteroids, and bullets
            self.ship.draw()
            
            # If there is no more asteroids left, draw the win screen
            if not self.asteroids:
                
                self.menu.draw_win_screen()
                
            else:
                
                for asteroid in self.asteroids:
                    asteroid.draw()
                
            for bullet in self.bullets:
                bullet.draw()
            
            # If the ship is not alive, draw the "Game Over" text and instructions to continue.
            if not self.ship.alive:
                self.menu.draw_game_over_screen()
            else:
                # Draw current score
                arcade.draw_text("Points: " + str(self.score), 80, 20, arcade.color.WHITE, font_size=15, anchor_x="center")
                
                
                self.draw_energy_bar(self.energy)
        
        # If the game is paused, draw the menu UI
        else:
            arcade.start_render()
            self.menu.uimanager.draw()
            
            
    def draw_energy_bar(self, energy):
        
        if energy > (ENERGY * .75):
            energy_color =  arcade.color.BRIGHT_GREEN
        elif energy > (ENERGY * .50):
            energy_color =  arcade.color.CYBER_YELLOW
        elif energy > (ENERGY * .25):
            energy_color =  arcade.color.DARK_ORANGE
        else:
            energy_color =  arcade.color.ELECTRIC_CRIMSON
        
        # Draw energy left on screen
        arcade.draw_text("Energy: " + str(round(self.energy)) + "%", SCREEN_WIDTH  - ENERGY , 60, energy_color, font_size=15, anchor_x="center")

        arcade.draw_rectangle_filled(SCREEN_WIDTH - 50 -  self.max_energy , 40, self.max_energy*2, 10, arcade.color.SILVER_CHALICE)
        
        arcade.draw_rectangle_filled(SCREEN_WIDTH + 50 -  self.max_energy - energy , 40, energy*2, 10, energy_color)
        
        
        

    def update(self, delta_time):
        """
        Update all the objects in game every frame.
        Function called automatically by Arcade framework.

        Args:
            delta_time (float): The time elapsed since the last update.
        """
        # If game is not paused
        if self.pause is False:
            
            # If the ship is still alive (hasn't been hit) then keep updating all the objects positions
            if self.ship.alive:

                self.check_keys(delta_time)
                self.check_collisions(delta_time)
                self.ship.advance()
                self.ship.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
                
                # Update the position of all the Asteroids                  
                for asteroid in self.asteroids:
                
                    asteroid.advance()
                    asteroid.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
                    
                # Update the position of all the Bullets
                for bullet in self.bullets:

                    bullet.advance()
                    bullet.bullet_is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

                # Update the position of the far_stars
                
                for star in self.stars:
                    star.advance()
                    star.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)   
                    
                for galaxy in self.galaxies:
                    galaxy.advance()
                    galaxy.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)               
      

    def check_collisions(self, delta_time):
        """
        For each asteroid it checks if they are too close from the ship and also checks if any bullet is too close from the asteroid as well.
        
        Updates scores and removes items who have been hit.
        
        Args:
            delta_time (float): The time elapsed since the last update.

        """
        # If game is not paused
        if self.pause is False:
            
            for asteroid in self.asteroids:
                
                # Check if the ship is too close from an asteroid, if so, stop the game and kill the spaceship.
                if (abs(self.ship.position.x - asteroid.position.x) - SHIP_RADIUS < asteroid.radius and
                        abs(self.ship.position.y - asteroid.position.y)  - SHIP_RADIUS < asteroid.radius):
                    
                    # If asteroid is a small energy one
                    if asteroid.size == "Small":
                        asteroid.alive = False
                        
                        
                        # Check if there is room in the energy tank for an increase
                        if self.energy < self.max_energy:
                            
                            # Increase the energy
                            self.energy += self.energy_increase
                            # Play energy increase sound
                            self.channel6.play(pygame.mixer.Sound(ENERGY_SOUND))          
                            self.channel6.set_volume(ENERGY_SOUND_VOLUME)
                            
                        # If the energy is greater than the max, put it back to only 100%
                        if self.energy > self.max_energy:
                            self.energy = self.max_energy
                            
                    else:
                        self.ship.velocity = pygame.Vector2(0, 0)
                        self.ship.alive = False
                    

                for bullet in self.bullets:
                    # Make sure they are both alive before checking for a collision
                    if bullet.alive and asteroid.alive:

                        too_close = asteroid.radius + bullet.radius
                        # If the position in X is greater than too_close then kill both the bullet and the asteroid
                        if (abs(bullet.position.x - asteroid.position.x) < too_close and
                                abs(bullet.position.y - asteroid.position.y) < too_close):
                            
                            bullet.alive = False
                            asteroid.alive = False
                            
                            # Split of big asteroids into smaller ones upon impact of bullet
                            if asteroid.size == "Big":
                                
                                self.asteroids.append(Asteroid("Medium", asteroid.position.x, asteroid.position.y, bullet.direction + 45))
                                self.asteroids.append(Asteroid("Small", asteroid.position.x, asteroid.position.y, bullet.direction))
                                self.asteroids.append(Asteroid("Medium", asteroid.position.x, asteroid.position.y, bullet.direction - 45))
                                # Add corresponding points
                                self.score += LARGE_ROCK_POINTS
                                
                                # Play explosion sound
                                self.channel3.play(pygame.mixer.Sound(EXPLOSION_SOUND))          
                                self.channel3.set_volume(EXPLOSION_SOUND_VOLUME)

                            elif asteroid.size == "Medium":

                                self.asteroids.append(Asteroid("Small", asteroid.position.x, asteroid.position.y, bullet.direction + 45))
                                self.asteroids.append(Asteroid("Small", asteroid.position.x, asteroid.position.y, bullet.direction - 45))
                                
                                # Add corresponding points
                                self.score += MEDIUM_ROCK_POINTS
                                
                                # Play explosion sound
                                self.channel4.play(pygame.mixer.Sound(MEDIUM_EXPLOSION_SOUND))          
                                self.channel4.set_volume(MEDIUM_EXPLOSION_SOUND_VOLUME)
                            
                            else:
                                self.score += SMALL_ROCK_POINTS
                                
                                # Play explosion sound
                                self.channel5.play(pygame.mixer.Sound(SMALL_EXPLOSION_SOUND))          
                                self.channel5.set_volume(SMALL_EXPLOSION_SOUND_VOLUME)
                                
                                
            self.cleanup_dead_objects()


    def cleanup_dead_objects(self):
        """
        Checks if all bullets and asteroids are not "Alive" in order to remove them
        from the list to avoid future updates and renders. 

        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)


    def check_keys(self, delta_time):

        """
        Checks for keys pressed and then updates the ship, asteroids and stars accordingly.
        
        Args:
            delta_time (float): The time elapsed since the last update.
        """
        # If game is not paused
        if self.pause is False:
            
            #   U P    K E Y
            if arcade.key.UP in self.held_keys:
                
                # Calculate the magnitude of each component (x and y) from its current angle
                ship_dx = math.cos(math.radians(self.ship.texture_orientation))
                ship_dy = math.sin(math.radians(self.ship.texture_orientation))
                
                # Accelerate!!
                # Increase the ships velocity vector according to its current orientation and Thust
                self.ship.velocity -= pygame.Vector2(round(ship_dx * SHIP_THRUST_AMOUNT, 2), round(ship_dy * SHIP_THRUST_AMOUNT, 2))
                
                for asteroid in self.asteroids:
                    asteroid.velocity += pygame.Vector2(ship_dx * SHIP_THRUST_AMOUNT, ship_dy * SHIP_THRUST_AMOUNT)

                # Update movement of stars
                for star in self.stars:
                    star.velocity = -self.ship.velocity * star.speed
                
                for galaxy in self.galaxies:
                    galaxy.velocity = -self.ship.velocity * galaxy.speed
                    
                # Switch randomly the regular and the action texture
                if random.randint(0, 1) == 0:
                    self.ship.texture = self.thrust_texture
                else:
                    self.ship.texture = self.ship_texture
                    
                    
                # Play Sound if the main engine music channel is not busy (not playing)
                if not self.main_engine_music_channel.get_busy():
                    
                    self.main_engine_music_channel.play(pygame.mixer.Sound(MAIN_ENGINE_SOUND))
                    self.main_engine_music_channel.set_volume(MAIN_ENGINE_SOUND_VOLUME)
                    
            #    D O W N    K E Y
            #########################
            if arcade.key.DOWN in self.held_keys:
                
                # Calculate the magnitude of each component (x and y) from its current angle
                ship_dx = math.cos(math.radians(self.ship.texture_orientation))
                ship_dy = math.sin(math.radians(self.ship.texture_orientation))
                
                # Reverse!
                # Increase the ships velocity vector according to its corresponding component (x or y) and Thust            
                self.ship.velocity += pygame.Vector2(round(ship_dx * SHIP_RETRO_THRUST_AMOUNT, 2), round(ship_dy * SHIP_RETRO_THRUST_AMOUNT, 2))
                
                for asteroid in self.asteroids:
                    asteroid.velocity -= pygame.Vector2(round(ship_dx * SHIP_RETRO_THRUST_AMOUNT, 2), round(ship_dy * SHIP_RETRO_THRUST_AMOUNT, 2))

                # Calculate the movement of stars oposite to the ship one, in order to create the paralax effect
                for star in self.stars:
                    star.velocity = -self.ship.velocity * star.speed
                    
                for galaxy in self.galaxies:
                    galaxy.velocity = -self.ship.velocity * galaxy.speed

                # Switch randomly the regular and the action texture
                if random.randint(0, 1) == 0:
                    self.ship.texture = self.reverse_texture
                else:
                    self.ship.texture = self.ship_texture

            #    L E F T    K E Y
            #########################
            if arcade.key.LEFT in self.held_keys:
                
                self.ship.angular_velocity += SHIP_TURN_AMOUNT

                # Switch randomly the regular and the action texture
                if random.randint(0, 1) == 0:
                    self.ship.texture = self.left_turn_texture
                else:
                    self.ship.texture = self.ship_texture

            #    R I G H T    K E Y
            #########################
            if arcade.key.RIGHT in self.held_keys:
                
                self.ship.angular_velocity -= SHIP_TURN_AMOUNT

                # Switch randomly the regular and the action texture
                if random.randint(0, 1) == 0:
                    self.ship.texture = self.right_turn_texture
                else:
                    self.ship.texture = self.ship_texture


    def on_key_press(self, key, delta_time):
        """
        Function called by the Arcade framework every time a keyboard key is pressed.
        Inside the function, specific actions will be performed if specific keys 
        were pressed (SPACE - Fire bullet, ENTER - Restart Game, ESCAPE - Exit game)

        Args:
            key ()
            delta_time (float): The time elapsed since the last update.
        """
        # If game is not paused, render all the objects: stars, ship, asteroids, bullets
        if self.pause is False:
            
            self.held_keys.add(key)
            
            # Hit SPACE to shoot a bullet
            #########################
            if key == arcade.key.SPACE:
                
                # If ship is alive create a bullet and fire it
                if self.ship.alive:
                    
                    # If there is still energy left
                    if self.energy > 0:
                        
                        # Spend energy
                        self.energy -= round(self.energy_cost_per_shot)
                        
                        # Do not show energy bellow 0
                        if self.energy < 0:
                            self.energy = 0
                        
                        bullet = Bullet(self.bullet_radius)
                        bullet.fire(self.ship.position.x, self.ship.position.y, self.ship.texture_orientation, self.ship.velocity)
                        self.bullets.append(bullet)
                        
                        # Count number of shots for later score calculations
                        self.ship.shots += 1
                                                
                        # Play laser sound
                        self.shooting_music_channel.play(pygame.mixer.Sound(SHOOTING_SOUND))       
                        self.shooting_music_channel.set_volume(SHOOTING_SOUND_VOLUME)
                    
            # Hit ENTER to RESET GAME
            #########################
            if key == arcade.key.ENTER:

                self.reset_objects()
                    
            # Hit ESCAPE to quit the game
            #########################
            if key == arcade.key.ESCAPE:
                # Quit Game
                # arcade.close_window()
                self.pause = True
                self.menu.show_menu_screen()
                # window = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")
                # arcade.run()

    
    def reset_objects(self):
        """
        Resets the values of all objects, either when the game is restarted after hitting ENTER or after selecting a new level
        
        """
        
        # Delete all objects
        del self.ship
        del self.bullets
        del self.asteroids
        
        # Create new ones and reset score
        self.ship = Ship()
        self.bullets = []
        self.asteroids = []
        self.score = 0
        self.energy = ENERGY
        
        # Reset speed of all stars
        for star in self.stars:
            star.velocity = pygame.Vector2(0,0)
            
        for galaxy in self.galaxies:
            galaxy.velocity = pygame.Vector2(0,0)
        
        # Create new large asteroids
        for new_asteroid in range(self.initial_rock_count):
            # Define new random locations
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            new_asteroid = Asteroid("Big", x, y, random.uniform(0, 360))
            self.asteroids.append(new_asteroid)


    def on_key_release(self, key, delta_time):
        """
        Function called by the Arcade framework every time a keyboard key is released.
        Inside the function, specific actions will be performed if specific keys 
        were released.

        Args:
            key ()
            delta_time (float): The time elapsed since the last update.
        """
        
        if key in self.held_keys:

            self.held_keys.remove(key)
            self.ship.texture = arcade.load_texture(SHIP_TEXTURE)