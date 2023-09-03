# constants.py

import arcade

# These are Global constants used throughout the game
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1080

# Ship
SHIP_TEXTURE = "assets/images/spaceship.png"
SHIP_TEXTURE_THRUST = "assets/images/spaceship2.png"
SHIP_TEXTURE_REVERSE = "assets/images/spaceship3.png"
SHIP_TEXTURE_LEFT_TURN = "assets/images/spaceshipLeft.png"
SHIP_TEXTURE_RIGHT_TURN= "assets/images/spaceshipRight.png"
SHIP_WIDTH = 100
SHIP_LENGTH = 100
SHIP_RADIUS = 30


SHIP_THRUST_AMOUNT = .05
SHIP_RETRO_THRUST_AMOUNT = .025
SHIP_TURN_AMOUNT = .02


# Bullet
BULLET_RADIUS = 10
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_COLOR = arcade.color.BRIGHT_GREEN


# Asteroids
INITIAL_ROCK_COUNT = 5

BIG_ROCK_TEXTURE = "assets/images/meteorGrey_big1.png"
BIG_ROCK_SPIN = .4
BIG_ROCK_SPEED = .5
BIG_ROCK_RADIUS = 30

MEDIUM_ROCK_TEXTURE = "assets/images/meteorGrey_medium1.png"
MEDIUM_ROCK_SPEED = 1.5
MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_TEXTURE = "assets/images/meteorGrey_small1.png"
SMALL_ROCK_SPEED = 7
SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2



# Stars
NUMBER_OF_BACKGROUND_STARS = 400
NUMBER_OF_STARS_1 = 200
NUMBER_OF_STARS_2 = 100

BASE_COLOR = [
    (255, 255, 255),  # White
]

#Speed
STARS_1_SPEED = .00025
STARS_2_SPEED = .00005

#Size
STAR_MIN_SIZE = .5
STAR_MAX_SIZE = STAR_MIN_SIZE * 1.3
STARS_1_MIN_SIZE = STAR_MIN_SIZE*1.5
STARS_2_MAX_SIZE = STAR_MAX_SIZE*2
STARS_2_MIN_SIZE = STAR_MIN_SIZE*2
STARS_2_MAX_SIZE = STAR_MAX_SIZE*4

COLOR_VARIATION = 50

# Music
# pygame.mixer.init()
# mixer.music.load('assets/sounds/adagio_for_strings_tiesto.wav')
# mixer.music.play(-1)