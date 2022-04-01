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

    def __init__(self, screen, level, food_names, change_screen):
        # general setup
        self.screen = screen
        self.change_screen = change_screen
        
        # layout setup
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/rancho_dos_soldados.png').convert(), (WIDTH, HEIGHT))
        
        # level attributes
        self.level = level
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 100)
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(change_screen, screen, self.foods))

        
    def get_food(self):
        return {
            Chinelao.food_name : Chinelao(),
            Lagarto.food_name : Lagarto(),
        }.get(choice(self.food_names), Chinelao.food_name)
    

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
        