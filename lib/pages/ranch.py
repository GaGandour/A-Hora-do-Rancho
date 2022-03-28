import pygame, sys, os
from random import choice

from chinelao import Chinelao
from lagarto import Lagarto
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'player'))
from lib.player.player import Player
from settings import *

class Ranch:
    page_name = "ranch"

    def __init__(self, screen, level, food_names):
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen
        self.food_names = food_names
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 100)

    def update(self):
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == self.food_timer:
                    self.foods.add(self.get_food())
        
        self.screen.blit(self.map_sprite,(0,0))
        
        self.player.draw(self.screen)
        self.player.update()
        self.foods.draw(self.screen)
        self.foods.update()

    def get_food(self):
        return {
            Chinelao.food_name : Chinelao(),
            Lagarto.food_name : Lagarto(),
        }.get(choice(self.food_names), Chinelao.food_name)









