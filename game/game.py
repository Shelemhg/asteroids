# game/game.py

import arcade
import math
import pygame
import random


from objects.asteroid import Asteroid
from objects.bullet import Bullet
from objects.ship import Ship
from objects.star import Star


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
    INITIAL_ROCK_COUNT,
    NUMBER_OF_BACKGROUND_STARS,
    NUMBER_OF_STARS_1,
    NUMBER_OF_STARS_2,
    UPDATE_INTERVAL_ALL_STARS,
    UPDATE_INTERVAL_VISIBLE_STARS,
    LARGE_ROCK_POINTS,
    MEDIUM_ROCK_POINTS,
    SMALL_ROCK_POINTS,
    PENALTY_PER_SHOT,
    MAIN_ENGINE_SOUND,
    MAIN_ENGINE_SOUND_VOLUME,
    SHOOTING_SOUND,
    SHOOTING_SOUND_VOLUME,
    BACKGROUND_MUSIC,
    BACKGROUND_MUSIC_VOLUME,
    EXPLOSION_SOUND,
    EXPLOSION_SOUND_VOLUME,
    MEDIUM_EXPLOSION_SOUND,
    MEDIUM_EXPLOSION_SOUND_VOLUME
)


class AsteroidsGame(arcade.Window):
    """
    Main game class for the Asteroids game.

    Attributes:
        held_keys (set): A set to store held keys.
        ship (Ship): The player's spaceship.
        bullets (list): A list to store active bullets.
        asteroids (list): A list to store active asteroids.
        stars (arcade.SpriteList): A list to store stars.
        background_stars (arcade.SpriteList): A list to store background stars.
        frame_count (int): A counter to track frames.
    """
    def __init__(self, width, height):
        """
        Initialize the game window and other game-related objects.

        Args:
            width (int): The width of the game window.
            height (int): The height of the game window.
        """
        super().__init__(width, height)        
        self.score = 0     # points counter
        self.highest_score = 0
        # self.set_update_rate(1/120)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        # Load all different textures and get them ready for later use
        self.ship_texture = arcade.load_texture(SHIP_TEXTURE)
        self.thrust_texture = arcade.load_texture(SHIP_TEXTURE_THRUST)
        self.reverse_texture = arcade.load_texture(SHIP_TEXTURE_REVERSE)
        self.left_turn_texture = arcade.load_texture(SHIP_TEXTURE_LEFT_TURN)
        self.right_turn_texture = arcade.load_texture(SHIP_TEXTURE_RIGHT_TURN)
        # Initialize objects
        self.held_keys = set()
        self.ship = Ship()
        self.bullets = []     # List to contain all the Bullet objects
        self.asteroids = []     # List to contain all the Asteroid objects
        
        # SOUND settings
        pygame.mixer.init()
        pygame.mixer.set_num_channels(6)
        self.background_music_channel = pygame.mixer.Channel(0)
        self.main_engine_music_channel = pygame.mixer.Channel(1)
        self.shooting_music_channel = pygame.mixer.Channel(2)
        self.channel3 = pygame.mixer.Channel(3)
        self.channel4 = pygame.mixer.Channel(4)
        self.channel5 = pygame.mixer.Channel(5)        
        # Start playing background music
        self.background_music_channel.play(pygame.mixer.Sound(BACKGROUND_MUSIC))
        self.background_music_channel.set_volume(BACKGROUND_MUSIC_VOLUME)  

        # Initialize Stars
        # self.stars = []
        self.stars = arcade.SpriteList()
        self.background_stars = arcade.SpriteList()     #  We separate this ones as they will not move or update their position   
        
        self.frame_count = 0
        
         # Generate stars for each layer
        self.generate_stars(self.background_stars, NUMBER_OF_BACKGROUND_STARS, 0)      
        self.generate_stars(self.stars, NUMBER_OF_STARS_1, 1)
        self.generate_stars(self.stars, NUMBER_OF_STARS_2, 2)


        # Initialize a random position for all asteroids and save them in their corresponding list
        for new_asteroid in range(INITIAL_ROCK_COUNT):
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            new_asteroid = Asteroid("Big", x, y, 0)
            self.asteroids.append(new_asteroid)

            
    def generate_stars(self, stars_list, num_stars, type):
        """
        Receives a list for storage, the number of stars and the tyope to then generate
        a random location on screen and add to the list a Star object with the corresponding
        size and coordinates.

        Args:
            stars_list (List[Star]): The list of stars to draw.
            num_stars (int): Number of stars to generate
            type (int): Type of stars to generate: Background = 0, Layer1 = 1, Layer2 = 2
        """
        for _ in range(num_stars):
            x = round(random.uniform(0, SCREEN_WIDTH), 2)
            y = round(random.uniform(0, SCREEN_HEIGHT), 2)
            star = Star(x, y, type)
            stars_list.append(star)

    
    def on_draw(self):
        """
        Arcade framework will automatically call this method  to render the objects 
        from back to front in the same order of the code.

        """
        arcade.start_render() 
         
        # Draw stars
        self.draw_stars(self.background_stars)  # Draw your background stars
        self.draw_stars(self.stars)     # Draw the other layer of stars
        

                

        # Draw ship, asteroids, and bullets
        self.ship.draw()
        
        for asteroid in self.asteroids:
            asteroid.draw()
            
        for bullet in self.bullets:
            bullet.draw()
            

        
        # If the ship is not alive, draw the "Game Over" text and instructions to continue.
        if not self.ship.alive:
            self.draw_end_screen()
        else:
            # Draw current score
            arcade.draw_text("Points: " + str(self.score), SCREEN_WIDTH - 80, 20, arcade.color.WHITE, font_size=15, anchor_x="center")
            
            
            
    
    def draw_stars(self, stars_list):
        """
        Draw stars from the specified list.

        Args:
            stars_list (List[Star]): The list of stars to draw.
        """
        for star in stars_list:
            star.draw()


    def update(self, delta_time):
        """
        Update the game state.

        Args:
            delta_time (float): The time elapsed since the last update.
        """
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
            self.frame_count += 1
            
            for star in self.stars:
                star.advance()
                star.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT)                 
      

    def check_collisions(self, delta_time):
        """
        Checks to see if bullets or asteroids are too close from other objects which will mean a collition has happened.
        Updates scores and removes dead items.
        
        Args:
            delta_time (float): The time elapsed since the last update.

        """
        for asteroid in self.asteroids:
            # Check if the ship is too close from an asteroid, if so, stop the game and kill the spaceship.
            if (abs(self.ship.position.x - asteroid.position.x) - SHIP_RADIUS < asteroid.radius and
                    abs(self.ship.position.y - asteroid.position.y)  - SHIP_RADIUS < asteroid.radius):
                
                self.ship.velocity = pygame.Vector2(0, 0)
                self.ship.alive = False
                

            for bullet in self.bullets:
                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:

                    too_close = asteroid.radius
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
                            
        self.cleanup_dead_objects()


    def cleanup_dead_objects(self):
        """
        Checks if all bullets and asteroids are not "Alive" in order to remove them
        from the list to avoid future updates and renders. 

        Args:
            stars_list (List[Star]): The list of stars to draw.
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)


    def check_keys(self, delta_time):

        """
        Checks for key presses and update the ship, asteroids and stars accordingly.
        
        Args:
            delta_time (float): The time elapsed since the last update.
        """
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

            # Switch randomly the regular and the action texture
            if random.randint(0, 1) == 0:
                self.ship.texture = self.reverse_texture
            else:
                self.ship.texture = self.ship_texture

        #    L E F T    K E Y
        if arcade.key.LEFT in self.held_keys:
            
            self.ship.angular_velocity += SHIP_TURN_AMOUNT

            # Switch randomly the regular and the action texture
            if random.randint(0, 1) == 0:
                self.ship.texture = self.left_turn_texture
            else:
                self.ship.texture = self.ship_texture

        #    R I G H T    K E Y
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
        self.held_keys.add(key)
        
        # Hit SPACE to shoot a bullet
        if key == arcade.key.SPACE:
            # If ship is alive create a bullet and fire it
            if self.ship.alive:
                bullet = Bullet()
                bullet.fire(self.ship.position.x, self.ship.position.y, self.ship.texture_orientation, self.ship.velocity)
                self.bullets.append(bullet)
                # Count number of shots for later score calculations
                self.ship.shots += 1
                # Substract points per shot
                self.score -= PENALTY_PER_SHOT
                
                # Play laser sound
                self.shooting_music_channel.play(pygame.mixer.Sound(SHOOTING_SOUND))       
                self.shooting_music_channel.set_volume(SHOOTING_SOUND_VOLUME)
                
        # Hit ENTER to RESET GAME
        if key == arcade.key.ENTER:

            self.ship.position.x = SCREEN_WIDTH / 2
            self.ship.position.y = SCREEN_HEIGHT / 2
            # Delete all objects
            del self.ship
            del self.bullets
            del self.asteroids
            # Create new ones and reset score
            self.ship = Ship()
            self.bullets = []
            self.asteroids = []
            self.score = 0
            
            # Reset speed of all stars
            for star in self.stars:
                star.velocity = pygame.Vector2(0,0)
            # Create new large asteroids
            for new_asteroid in range(INITIAL_ROCK_COUNT):
                # Define new random locations
                x = random.uniform(0, SCREEN_WIDTH)
                y = random.uniform(0, SCREEN_HEIGHT)
                new_asteroid = Asteroid("Big", x, y, random.uniform(0, 360))
                self.asteroids.append(new_asteroid)
                
        # Hit ESCAPE to quit the game
        if key == arcade.key.ESCAPE:
            # Quit Game
            arcade.close_window()


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
            
            
    
    def draw_end_screen(self):
        # Draw the Game Over text
        arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Press ESC to Exit", SCREEN_WIDTH // 8, 40, arcade.color.WHITE, font_size=20, anchor_x="left")
        arcade.draw_text("Press ENTER to Restart", SCREEN_WIDTH - SCREEN_WIDTH // 8, 40, arcade.color.WHITE, font_size=20, anchor_x="right")
        
        # Draw final score
        arcade.draw_text("FINAL SCORE: " + str(self.score), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, arcade.color.GREEN, font_size=25, anchor_x="center")
        # Check if current score is the highest so far
        if self.score > self.highest_score:
            self.highest_score = self.score
            
        # Draw highest score
        arcade.draw_text("Highest Score: " + str(self.highest_score), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, arcade.color.WHITE, font_size=25, anchor_x="center")
        
        
        
        