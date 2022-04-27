import sys, os

sys.path.append(os.path.join(sys.path[0],'pages'))

from settings import *
from ranch import Ranch
from main import Game

class Game_Test(Game):
    def __init__(self, initial_page_name, level = 1):
        super().__init__()
        self.level = level
        assert(initial_page_name != Ranch.page_name)
        self.change_screen(initial_page_name)