# main.py

import arcade

from main_menu import MainMenu
from game.game import AsteroidsGame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    window = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT, "Menu")
    arcade.run()
    

if __name__ == "__main__":
    main()