import pygame, sys, os
sys.path.append(os.path.join(sys.path[0],'pages'))
sys.path.append(os.path.join(sys.path[0],'objects'))
# from playsound import playsound

from settings import *

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
        self.ranch_time_music = './assets/music/Ranch_Time.wav'
        self.menu_theme_music = './assets/music/Menu_Theme.wav'
        self.play_music(self.menu_theme_music)

    
    def play_music(self, file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(loops=-1)


    def stop_music(self):
        pygame.mixer.music.stop()


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
            Ranch.page_name : Ranch(self.screen, self.level, self.food_names, self.go_to_home_page, self.pass_level, self.game_over),
            Food_Choice.page_name : Food_Choice(self.screen,  self.change_screen, self.level, self.add_food),
            Game_Over.page_name : Game_Over(self.screen, lambda: self.change_screen(Home_Page.page_name))
        }.get(screen_name, Home_Page.page_name)
        if screen_name == Ranch.page_name and self.level == 1:
            self.play_music(self.ranch_time_music)
        if screen_name == Game_Over.page_name:
            self.stop_music()
        if screen_name == Home_Page.page_name:
            self.play_music(self.menu_theme_music) 


    def pass_level(self):
        self.level += 1
        self.change_screen(Food_Choice.page_name)


    def game_over(self):
        self.change_screen(Game_Over.page_name)
        self.level = 1
        self.food_names = []


    def go_to_home_page(self):
        self.change_screen(Home_Page.page_name)
        self.level = 1
        self.food_names = []


    def add_food(self, food_name):
        self.food_names.append(food_name)



if __name__ == '__main__':
    game = Game()
    game.run()