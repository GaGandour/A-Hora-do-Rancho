import pygame, sys, os

sys.path.append(os.path.join(sys.path[0],'pages'))

from settings import *


from ranch import Ranch
from home_page import Home_Page
from food_choice import Food_Choice
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Hora do Rancho')
        self.level = 0
        self.screen_name = Home_Page.page_name

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
            Ranch.page_name : Ranch(self.screen, self.level),
            Home_Page.page_name : Home_Page(self.screen, self.level, self.change_screen),
            Food_Choice.page_name : Food_Choice(self.screen, self.level, self.change_screen)
        }.get(screen_name, Ranch.page_name)


if __name__ == '__main__':
    game = Game()
    game.run()