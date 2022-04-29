from lib.pages.you_win_page import You_Win_Page
from lib.game_test import Game_Test

if __name__ == '__main__':
    game = Game_Test(You_Win_Page.page_name)
    game.run()