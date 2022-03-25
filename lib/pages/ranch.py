import pygame, sys, os
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
from food import Food
sys.path.append(os.path.join(sys.path[0], 'player'))
from lib.player.player import Player
from settings import *

class Ranch:
    page_name = "ranch"

    def __init__(self, screen, level):
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen

        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 300)

    def update(self):
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == self.food_timer:
                    self.foods.add(Food(CHINELAO_NAME))
        
        self.screen.blit(self.map_sprite,(0,0))
        
        self.player.draw(self.screen)
        self.player.update()
        self.foods.draw(self.screen)
        self.foods.update()









