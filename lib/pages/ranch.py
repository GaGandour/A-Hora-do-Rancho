from turtle import Screen
import pygame, sys, os
from random import choice

sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'player'))
sys.path.append(os.path.join(sys.path[0], 'pages'))

from lib.player.player import Player
from lib.widgets.menu_button import Menu_Button
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
        self.play = True
        
        # layout setup
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/soldier_ranch_16x16.png').convert(), (WIDTH, HEIGHT))
        self.pause_surface = pygame.Surface((WIDTH,HEIGHT))  # the size of your rect
        self.pause_surface.fill("#2e2e2e")  # this fills the entire surface
        self.pause_surface.set_alpha(156)                # alpha level

        # level attributes
        self.level = level
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 40)
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(game_over, pass_level, screen, self.foods, self.max_time, self.pause))

        # pause ui
        self.buttons = [
            Menu_Button(screen, (480, 220), "Resume", lambda: self.pause()),
            Menu_Button(screen, (480, 320), "Go Back To Menu", lambda: self.go_to_home_page()),
        ]
    

        
    def get_food(self):
        food_dictionary = {}
        for food in FOOD_LIST:
            food_dictionary[food.food_name] = food

        return food_dictionary.get(choice(self.food_names), "")
        

    def pause(self):
        self.play = not self.play


    def update(self):
        pygame.display.update()
        if self.play:
            for event in pygame.event.get():
                    if event.type == self.food_timer:
                        self.foods.add(self.get_food()())
        
            self.screen.blit(self.map_sprite,(0,0))
        
            self.player.draw(self.screen)
            self.player.update()
        
            self.foods.draw(self.screen)
            self.foods.update()
        else:
            self.screen.blit(self.map_sprite,(0,0))
            self.player.draw(self.screen)
            self.foods.draw(self.screen)
            self.screen.blit(self.pause_surface, (0,0))

            if self.buttons:
                for button in self.buttons:
                    button.update()
        