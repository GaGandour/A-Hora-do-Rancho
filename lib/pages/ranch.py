import pygame, sys, os
from random import choice

sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'player'))

from lib.player.player import Player
from settings import *
from food_list import *


class Ranch:
    page_name = "ranch"

    def __init__(self, screen, level, food_names, change_screen, pass_level, game_over):
        # general setup
        self.screen = screen
        self.change_screen = change_screen
        self.game_over = game_over
        self.max_time = 30
        
        # layout setup
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/soldier_ranch_16x16.png').convert(), (WIDTH, HEIGHT))
        
        # level attributes
        self.level = level
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 40)
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(game_over, pass_level, screen, self.foods, self.max_time))

        
    def get_food(self):
        food_dictionary = {}
        for food in FOOD_LIST:
            food_dictionary[food.food_name] = food

        return food_dictionary.get(choice(self.food_names), "")
        

    def update(self):
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == self.food_timer:
                    self.foods.add(self.get_food()())
        
        self.screen.blit(self.map_sprite,(0,0))
        
        self.player.draw(self.screen)
        self.player.update()
        
        self.foods.draw(self.screen)
        self.foods.update()
        