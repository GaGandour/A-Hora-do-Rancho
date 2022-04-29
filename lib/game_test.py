from settings import *
from pages.ranch import Ranch
from main import Game
import pygame

class Game_Test(Game):
    def __init__(self, initial_page_name, level = 1, mute = True):
        super().__init__()
        self.level = level
        assert(initial_page_name != Ranch.page_name)
        self.change_screen(initial_page_name)
        if mute:
            pygame.mixer.music.set_volume(0)