import arcade
from game.game import AsteroidsGame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    window = AsteroidsGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()