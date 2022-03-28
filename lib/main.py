import pygame, sys, os
sys.path.append(os.path.join(sys.path[0],'pages'))
sys.path.append(os.path.join(sys.path[0],'objects'))

from settings import *

import chinelao, lagarto
from ranch import Ranch
from home_page import Home_Page

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Hora do Rancho')
        self.level = 0
        self.screen_name = Home_Page.page_name
        self.food_names = [chinelao.Chinelao.food_name, lagarto.Lagarto.food_name]

    def run(self):
        self.page = Home_Page(self.screen, self.level,self.change_screen)
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
            Ranch.page_name : Ranch(self.screen, self.level, self.food_names),
            Home_Page.page_name : Home_Page(self.screen, self.level, self.change_screen),
        }.get(screen_name, Home_Page.page_name)

    def add_food(self, food_name):
        self.food_names.append(food_name)


if __name__ == '__main__':
    game = Game()
    game.run()