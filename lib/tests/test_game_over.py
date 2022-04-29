from lib.pages.game_over import Game_Over
from lib.game_test import Game_Test

if __name__ == '__main__':
    game = Game_Test(Game_Over.page_name)
    game.run()