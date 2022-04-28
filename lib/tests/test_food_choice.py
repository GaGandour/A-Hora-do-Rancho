import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

sys.path.append(os.path.join(sys.path[0],'pages'))


from food_choice import Food_Choice
from game_test import Game_Test

if __name__ == '__main__':
    game = Game_Test(Food_Choice.page_name)
    game.run()