import pygame, sys, os
sys.path.append(os.path.join(sys.path[0],'pages'))
sys.path.append(os.path.join(sys.path[0],'objects'))

from settings import *

import chinelao, lagarto
from ranch import Ranch
from home_page import Home_Page
from game_over import Game_Over
from food_choice import Food_Choice

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Hora do Rancho')
        self.level = 1
        self.screen_name = Home_Page.page_name
        self.food_names = []
        self.page = Home_Page(self.screen,self.change_screen)


    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.page.update()
            self.clock.tick(FPS)


    def change_screen(self, screen_name):
        self.screen_name = screen_name
        self.page = {
            Home_Page.page_name : Home_Page(self.screen, self.change_screen),
            Ranch.page_name : Ranch(self.screen, self.level, self.food_names, self.change_screen),
            Food_Choice.page_name : Food_Choice(self.screen,  self.change_screen, self.level, self.add_food),
            Game_Over.page_name : Game_Over(self.screen, lambda: self.change_screen(Home_Page.page_name))
        }.get(screen_name, Home_Page.page_name)
        #.get(screen_name, Ranch.page_name)


    def add_food(self, food_name):
        self.food_names.append(food_name)



if __name__ == '__main__':
    game = Game()
    game.run()