import pygame, sys, os
from random import choice

sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'player'))
sys.path.append(os.path.join(sys.path[0], 'pages'))

from lib.player.player import Player
from lib.widgets.menu_button import Menu_Button
from lib.objects.trigger_burguer import Trigger_Burguer
from lib.objects.burguer import Burguer

from settings import *
from food_list import *


class Ranch:
    page_name = "ranch"

    def __init__(self, screen, level, food_names, go_to_home_page, pass_level, game_over):
        # general setup
        self.screen = screen
        self.go_to_home_page = go_to_home_page
        self.game_over = game_over
        self.max_time = 30
        self.playing = True
        self.is_special_ranch = False
        self.there_is_burguer = False
        self.special_ranch_start_time = 0
        
        # layout setup
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/soldier_ranch_16x16.png').convert(), (WIDTH, HEIGHT))
        self.map_sprite_always_on_top = pygame.transform.scale(pygame.image.load('./assets/maps/soldier_ranch_16x16_always_on_top.png').convert_alpha(), (WIDTH, HEIGHT))
        obstacles = []
        # add borders
        obstacles.append(pygame.Rect(0,0,960,74))
        obstacles.append(pygame.Rect(0,0,30,540))
        obstacles.append(pygame.Rect(930,0,30,540))
        obstacles.append(pygame.Rect(0,528,960,12))
        # add buffets
        obstacles.append(pygame.Rect(162,74,124,30))
        for i in range(3):
            obstacles.append(pygame.Rect(162,222+96*i,124,10))
        # add tables
        obstacles.append(pygame.Rect(388,74,26,124))
        for i in range(4):
            obstacles.append(pygame.Rect(484+96*i,74,26,124))
            obstacles.append(pygame.Rect(484+96*i,286,26,40))
            obstacles.append(pygame.Rect(484+96*i,414,26,114))
        
        self.pause_surface = pygame.Surface((WIDTH,HEIGHT))  # the size of your rect
        self.pause_surface.fill("#2e2e2e")  # this fills the entire surface
        self.pause_surface.set_alpha(156)                # alpha level

        # level attributes
        self.level = level
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 24 - 3*level)
        self.special_ranch = pygame.USEREVENT + 2
        pygame.time.set_timer(self.special_ranch, 400)
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(game_over, pass_level, screen, self.foods, self.max_time, self.pause, obstacles, self.start_special_ranch))

        # pause ui
        self.buttons = [
            Menu_Button(screen, (480, 200), "Resume", function = lambda: self.pause()),
            Menu_Button(screen, (480, 360), "Back To Menu", function = lambda: self.go_to_home_page()),
        ]
    

        
    def get_food(self):
        food_dictionary = {}
        for food in FOOD_LIST:
            food_dictionary[food.food_name] = food

        return food_dictionary.get(choice(self.food_names), "")
        

    def pause(self):
        self.playing = not self.playing


    def start_special_ranch(self):
        self.is_special_ranch = True
        self.special_ranch_start_time = self.player.sprite.get_current_time()


    def stop_special_ranch(self):
        self.is_special_ranch = False
        self.there_is_burguer = False


    def update(self):
        pygame.display.update()
        if self.playing:
            for event in pygame.event.get():
                    if event.type == self.food_timer:
                        if not self.is_special_ranch:
                            self.foods.add(self.get_food()())
                        else:
                            self.foods.add(Burguer())

                    if event.type == self.special_ranch and not self.is_special_ranch and not self.there_is_burguer and self.level >= 3:
                        self.foods.add(Trigger_Burguer())
                        self.there_is_burguer = True

            if self.is_special_ranch:
                if self.player.sprite.get_current_time() - self.special_ranch_start_time > 5:
                    self.stop_special_ranch()

            self.screen.blit(self.map_sprite,(0,0))
        
            self.player.draw(self.screen)
            self.player.update()

            self.screen.blit(self.map_sprite_always_on_top,(0,0))

            self.foods.draw(self.screen)
            self.foods.update()
        else:
            self.screen.blit(self.map_sprite,(0,0))

            self.player.draw(self.screen)
            self.player.sprite.show_ui(False)

            self.screen.blit(self.map_sprite_always_on_top,(0,0))

            self.foods.draw(self.screen)

            self.screen.blit(self.pause_surface, (0,0))

            if self.buttons:
                for button in self.buttons:
                    button.update()
        