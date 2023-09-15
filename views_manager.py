# views_manager.py

import arcade
from main_menu import MainMenu
from game.game import AsteroidsGame



class MainMenuView(arcade.View):
    
    def __init__(self):
        self.main_menu_view = MainMenu(self)
        # self.game_view = AsteroidsGame(self)
        self.current_view = self.main_menu_view
        self.current_view.on_show()
        # Assign lambda functions to handle the button click events with different arguments
        self.main_menu_view.easy_button.on_click = lambda event: self.on_buttonclick("Easy")
        self.main_menu_view.medium_button.on_click = lambda event: self.on_buttonclick("Medium")
        self.main_menu_view.hard_button.on_click = lambda event: self.on_buttonclick("Hard")
        self.main_menu_view.quit_button.on_click = lambda event:self.on_quit_buttonclick

    def show_game_view(self):
        # self.current_view = self.game_view
        # self.current_view.on_show()
        self.current_view = AsteroidsGame(self)
        self.current_view.on_show()
    
    def show_main_menu_view(self):
        self.current_view = self.main_menu_view
        self.current_view.on_show()
    
    def on_draw(self):
        self.current_view.on_draw()
    
    
    def on_buttonclick(self, difficulty):
        self.current_view = AsteroidsGame(difficulty)
        self.current_view.on_show()
        print("Hola primos")
    
    def on_quit_buttonclick(event):
        # Quit Game
        arcade.close_window()

class AsteroidsGameView(arcade.View):
    def __init__(self):
        super().__init__()
        # Create an instance of the AsteroidsGame class from game/game.py
        self.asteroids_game = AsteroidsGame(self)

    def on_show(self):
        # Initialize the game logic when the view is shown
        self.asteroids_game.setup()

    def on_draw(self):
        # Call the on_draw method of the AsteroidsGame class
        self.asteroids_game.on_draw()

    def on_update(self, delta_time):
        # Call the update method of the AsteroidsGame class
        self.asteroids_game.update(delta_time)

    def on_key_press(self, key, modifiers):
        # # Call the on_key_press method of the AsteroidsGame class
        # self.asteroids_game.on_key_press(key, modifiers)
        if key == arcade.key.ESCAPE:
            # Switch back to ViewsManager and then to MainMenuView
            views_manager = self.window.show_view(ViewsManager())
            views_manager.show_main_menu_view()

    def on_key_release(self, key, modifiers):
        # Call the on_key_release method of the AsteroidsGame class
        self.asteroids_game.on_key_release(key, modifiers)



class ViewsManager(arcade.View):
    # Method automatically called
    def __init__(self):
        super().__init__()
    
    # Function ran when the view is shown for the first time
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.GREEN)
        self.window.show_view(MainMenu())
    
    
    def on_draw(self):
        arcade.start_render()
        
    
