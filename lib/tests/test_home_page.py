from lib.pages.home_page import Home_Page
from lib.game_test import Game_Test

if __name__ == '__main__':
    game = Game_Test(Home_Page.page_name, mute=True)
    game.run()