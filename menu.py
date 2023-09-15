# menu.py

import arcade
from arcade import gui

from constants import (
    INITIAL_ROCK_COUNT,
    PENALTY_PER_SHOT,
    BULLET_RADIUS
)


class Menu:
    def __init__(self, game):
        self.game = game
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

    def unpause(self, difficulty):
        self.pause = False
    
    def on_buttonclick(self, difficulty):
        # Store the selected difficulty
        self.game.difficulty = difficulty
        self.game.reset_objects()
        self.game.pause = False
        
        if self.game.difficulty == "Easy":
            
            self.game.bullet_radius = BULLET_RADIUS + 5
            self.game.penalty_per_shot = PENALTY_PER_SHOT - 30
            self.game.initial_rock_count = INITIAL_ROCK_COUNT
            
        if self.game.difficulty == "Medium":
             
            self.game.bullet_radius = BULLET_RADIUS + 2
            self.game.penalty_per_shot = PENALTY_PER_SHOT  - 10
            self.game.initial_rock_count = INITIAL_ROCK_COUNT + 3
            
        if self.game.difficulty == "Hard":
            
            self.game.bullet_radius = BULLET_RADIUS 
            self.game.penalty_per_shot = PENALTY_PER_SHOT
            self.game.initial_rock_count = INITIAL_ROCK_COUNT + 5
            
            
    def show_difficulty_selection_screen(self):
        
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        
        arcade.set_background_color(arcade.color.ARSENIC)
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
        quit_button.on_click = self.on_quit_buttonclick

        # Create a UIBoxLayout and add the buttons to it
        button_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)
        
        if self.game.difficulty != None:
            resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)            
            resume_button.on_click = lambda event: self.unpause(self.difficulty)
            button_box.add(resume_button)
        
        
        
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
        
            
    def on_quit_buttonclick(event, self):
        # Quit Game
        arcade.close_window()
    
    