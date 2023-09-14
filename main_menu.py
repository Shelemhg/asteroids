# main_menu.py

import arcade
from arcade import gui
from game.game import AsteroidsGame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class MainMenu(arcade.Window):
    
    def __init__(self, width, height, screen_title):
        super().__init__(width, height, screen_title)
        arcade.set_background_color(arcade.color.ASH_GREY)
  
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
  
        # Create the buttons
        easy_button = arcade.gui.UIFlatButton(text="Easy", width=200)
        medium_button = arcade.gui.UIFlatButton(text="Medium", width=200)
        hard_button = arcade.gui.UIFlatButton(text="Hard", width=200)
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
  
        # Assign lambda functions to handle the button click events with different arguments
        easy_button.on_click = lambda event: self.on_buttonclick("Easy")
        medium_button.on_click = lambda event: self.on_buttonclick("Medium")
        hard_button.on_click = lambda event: self.on_buttonclick("Hard")
        quit_button.on_click = lambda event:self.on_quit_buttonclick
  
        # Create a UIBoxLayout and add the buttons to it
        button_box = arcade.gui.UIBoxLayout(vertical=True, space_between =20)
        button_box.add(easy_button)
        button_box.add(medium_button)
        button_box.add(hard_button)
        button_box.add(quit_button)
  
        # Add the button box to the UI manager using UIAnchorWidget
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=button_box
            )
        )

  
    def on_buttonclick(self, difficulty):
        
        arcade.close_window()
        window = AsteroidsGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, difficulty)
        arcade.run()
    
    
    def on_quit_buttonclick(event):
        # Quit Game
        arcade.close_window()
        
  
    def on_draw(self):
        arcade.start_render()
        self.uimanager.draw()