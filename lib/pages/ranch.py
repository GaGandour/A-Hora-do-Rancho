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
        
        # level attributes
        self.level = level
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 20)
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(game_over, pass_level, screen, self.foods, self.max_time, obstacles))

        
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

        self.screen.blit(self.map_sprite_always_on_top,(0,0))
        
        self.foods.draw(self.screen)
        self.foods.update()

        