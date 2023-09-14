# main.py

import arcade

from game.game import AsteroidsGame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

def main():
    window = AsteroidsGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()