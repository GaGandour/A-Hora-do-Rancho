import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

sys.path.append(os.path.join(sys.path[0],'pages'))


from home_page import Home_Page
from game_test import Game_Test

if __name__ == '__main__':
    game = Game_Test(Home_Page.page_name, mute=False)
    game.run()