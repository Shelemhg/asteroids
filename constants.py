# constants.py

# Global constants used throughout the game
import arcade

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Asteroids"


########################
#       S H I P        #
########################
SHIP_TEXTURE = "assets/images/spaceship.png"
SHIP_TEXTURE_THRUST = "assets/images/spaceship2.png"
SHIP_TEXTURE_REVERSE = "assets/images/spaceship3.png"
SHIP_TEXTURE_LEFT_TURN = "assets/images/spaceshipLeft.png"
SHIP_TEXTURE_RIGHT_TURN= "assets/images/spaceshipRight.png"
SHIP_WIDTH = 100
SHIP_LENGTH = 100
SHIP_RADIUS = 27


SHIP_THRUST_AMOUNT = .05
SHIP_RETRO_THRUST_AMOUNT = .025
SHIP_TURN_AMOUNT = .09
# SHIP_THRUST_AMOUNT = .015
# SHIP_RETRO_THRUST_AMOUNT = .005
# SHIP_TURN_AMOUNT = .03

LEFT_LIMIT = SCREEN_WIDTH/4
RIGHT_LIMIT = SCREEN_WIDTH - SCREEN_WIDTH/4
BOTTOM_LIMIT = SCREEN_HEIGHT/4
TOP_LIMIT = SCREEN_HEIGHT - SCREEN_HEIGHT/4



########################
#      B U L L E T     #
########################
BULLET_SPEED = 40
BULLET_RADIUS = 10
BULLET_LIFE = 60
BULLET_COLOR = arcade.color.SPRING_BUD
ENERGY = 100
ENERGY_COST_PER_SHOT = 5
ENERGY_INCREASE = 15



###########################
#    A S T E R O I D S    #
###########################
INITIAL_ROCK_COUNT = 5

BIG_ROCK_TEXTURE = "assets/images/meteorGrey_big1.png"
BIG_ROCK_SPEED = .5
BIG_ROCK_SPIN = .4
BIG_ROCK_RADIUS = 45

MEDIUM_ROCK_TEXTURE = "assets/images/meteorGrey_medium1.png"
MEDIUM_ROCK_SPEED = .7
MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 27

SMALL_ROCK_TEXTURE = "assets/images/meteorGrey_small1.png"
SMALL_ROCK_SPEED = 2
SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 15

#  POINTS SYSTEM
LARGE_ROCK_POINTS = 100
MEDIUM_ROCK_POINTS = 150
SMALL_ROCK_POINTS = 200
PENALTY_PER_SHOT = 50



########################
#      S T A R S      #
#######################
NUMBER_OF_BACKGROUND_STARS = 1000
NUMBER_OF_STARS_1 = 300
NUMBER_OF_STARS_2 = 100
NUMBER_OF_GALAXIES = 7


UPDATE_INTERVAL_ALL_STARS = 1
UPDATE_INTERVAL_VISIBLE_STARS = 10


BASE_COLOR = [
    (255, 255, 255),  # White
]

#Speed
# STARS_1_SPEED = .05
# STARS_2_SPEED = .01
STARS_1_SPEED = .025
STARS_2_SPEED = .005

#Size
STAR_MIN_SIZE = 1.2
STAR_MAX_SIZE = STAR_MIN_SIZE * 1.3
STARS_1_MIN_SIZE = STAR_MIN_SIZE * 1.2
STARS_1_MAX_SIZE = STAR_MAX_SIZE * 1.5
STARS_2_MIN_SIZE = STAR_MIN_SIZE * 1.5
STARS_2_MAX_SIZE = STAR_MAX_SIZE * 2

COLOR_VARIATION = 50



########################
#      M U S I C       #
########################
MAIN_ENGINE_SOUND = 'assets/sounds/engine2.wav'
MAIN_ENGINE_SOUND_VOLUME = .4
SHOOTING_SOUND = 'assets/sounds/laser_shot.wav'
SHOOTING_SOUND_VOLUME = .3

EXPLOSION_SOUND = 'assets/sounds/explosion2.wav'
EXPLOSION_SOUND_VOLUME = .4
MEDIUM_EXPLOSION_SOUND = 'assets/sounds/explosion.wav'
MEDIUM_EXPLOSION_SOUND_VOLUME = .4

SMALL_EXPLOSION_SOUND = 'assets/sounds/explosion.wav'
SMALL_EXPLOSION_SOUND_VOLUME = .3

BACKGROUND_MUSIC = 'assets/sounds/adagio_for_strings_tiesto.wav'
BACKGROUND_MUSIC_VOLUME = .5

ENERGY_SOUND = 'assets/sounds/energy.wav'
ENERGY_SOUND_VOLUME = .2


# BACKGROUND_MUSIC_VOLUME = 0