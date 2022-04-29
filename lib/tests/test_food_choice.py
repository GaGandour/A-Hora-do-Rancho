from pages.food_choice import Food_Choice
from game_test import Game_Test

if __name__ == '__main__':
    game = Game_Test(Food_Choice.page_name, level = 3, mute=False)
    game.run()