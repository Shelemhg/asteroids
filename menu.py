# menu.py

import arcade
from arcade import gui

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    INITIAL_ROCK_COUNT,
    PENALTY_PER_SHOT,
    BULLET_RADIUS
)


class Menu:
    
    def __init__(self, game):
        """
        Initialize a Menu object.

        Args:
            game (AsteroidGame): Game object from the main game logic
        """
        self.game = game
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()


    def unpause(self, difficulty):
        
        # Switch the state of the game to unpaused
        self.game.pause = False
    
    
    def on_buttonclick(self, difficulty):
        
        # Store the selected difficulty after a button is clicked
        self.game.difficulty = difficulty
        self.game.reset_objects()
        self.game.pause = False
        
        # Define the variables related to the selected difficulty
        if self.game.difficulty == "Easy":
            
            # Increase the size of the bullet to hit asteroids easier
            self.game.bullet_radius = BULLET_RADIUS + 5
            # Decrease the cost in points for every shot
            self.game.penalty_per_shot = PENALTY_PER_SHOT - 30
            # Set the number of large rocks on spawns
            self.game.initial_rock_count = INITIAL_ROCK_COUNT
            
        if self.game.difficulty == "Medium":
             
            # Define a smaller size for the bullets to hit asteroids harder
            self.game.bullet_radius = BULLET_RADIUS + 1
            # Decrease the cost in points for every shot
            self.game.penalty_per_shot = PENALTY_PER_SHOT  - 10
            # Set the number of large rocks on spawns
            self.game.initial_rock_count = INITIAL_ROCK_COUNT + 3
            
        if self.game.difficulty == "Hard":
            
            # Define a smaller size for the bullets to hit asteroids harder
            self.game.bullet_radius = BULLET_RADIUS -2
            # Set the cost in points for every shot
            self.game.penalty_per_shot = PENALTY_PER_SHOT
            # Set the number of large rocks on spawns
            self.game.initial_rock_count = INITIAL_ROCK_COUNT + 5
            
            
    def show_difficulty_selection_screen(self):
        
        # Instanciate objects for the creation of the UI
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        
        arcade.set_background_color(arcade.color.ARSENIC)
            
        # Create the buttons
        easy_button = arcade.gui.UIFlatButton(
                        text="Easy",
                        width=200,
                        style={
                            "bg_color": arcade.color.AO,  # Background color
                            "hover_bg_color": arcade.color.GREEN,  # Background color on hover
                            "font_color": arcade.color.WHITE,  # Text color
                            "border_color": arcade.color.BLACK,  # Border color
                            "border_width": 4,  # Border width
                            "font_size": 20,  # Text font size
                        }
                    )
        medium_button = arcade.gui.UIFlatButton(                        
                        text="Medium",
                        width=200,
                        style={
                            "bg_color": arcade.color.AMBER,  # Background color
                            "hover_bg_color": arcade.color.GREEN,  # Background color on hover
                            "font_color": arcade.color.WHITE,  # Text color
                            "border_color": arcade.color.BLACK,  # Border color
                            "border_width": 4,  # Border width
                            "font_size": 20,  # Text font size
                        }
                    )
        hard_button = arcade.gui.UIFlatButton(                        
                        text="Hard",
                        width=200,
                        style={
                            "bg_color": arcade.color.SAE,  # Background color
                            "hover_bg_color": arcade.color.GREEN,  # Background color on hover
                            "font_color": arcade.color.WHITE,  # Text color
                            "border_color": arcade.color.BLACK,  # Border color
                            "border_width": 4,  # Border width
                            "font_size": 20,  # Text font size
                        }
                    )
        quit_button = arcade.gui.UIFlatButton(
                        text="Quit",
                        width=200,
                        style={
                            "bg_color": arcade.color.ARSENIC,  # Background color
                            "hover_bg_color": arcade.color.AO,  # Background color on hover
                            "font_color": arcade.color.WHITE,  # Text color
                            "border_color": arcade.color.BLACK,  # Border color
                            "border_width": 4,  # Border width
                            "font_size": 20,  # Text font size
                        }
                    )

        # Assign lambda functions to handle the button click events with different arguments
        easy_button.on_click = lambda event: self.on_buttonclick("Easy")
        medium_button.on_click = lambda event: self.on_buttonclick("Medium")
        hard_button.on_click = lambda event: self.on_buttonclick("Hard")
        quit_button.on_click = self.on_quit_buttonclick

        # Create a UIBoxLayout and add the buttons to it
        button_box = arcade.gui.UIBoxLayout(vertical=True, space_between=20)
        
        if self.game.difficulty != None:
            resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)            
            resume_button.on_click = lambda event: self.unpause(self.game.difficulty)
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
    
    def draw_points(self):
        arcade.draw_text("Press ESC to Show Menu", SCREEN_WIDTH // 8, 40, arcade.color.WHITE, font_size=20, anchor_x="left")
        arcade.draw_text("Press ENTER to Restart", SCREEN_WIDTH - SCREEN_WIDTH // 8, 40, arcade.color.WHITE, font_size=20, anchor_x="right")
        
        # Draw final score
        arcade.draw_text("FINAL SCORE: " + str(self.game.score), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, arcade.color.GREEN, font_size=25, anchor_x="center")
        
        # Check if current score is the highest so far
        if self.game.score > self.game.highest_score:
            self.game.highest_score = self.game.score
            
        # Draw highest score
        arcade.draw_text("Highest Score: " + str(self.game.highest_score), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, arcade.color.WHITE, font_size=25, anchor_x="center")
        
    def draw_game_over_screen(self):
        
        # Draw the Game Over text
        arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        self.draw_points()
        
    
    def draw_win_screen(self):
        # Draw the Game Over text
        arcade.draw_text("Mission Acomplished!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        self.draw_points()