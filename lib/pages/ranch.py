import pygame, sys, os
from random import choice


from chinelao import Chinelao
from lagarto import Lagarto
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'player'))
from lib.player.player import Player
from settings import *
from ui import UI

class Ranch:
    page_name = "ranch"

    def __init__(self, screen, level, food_names, change_screen):
        # general setup
        self.screen = screen
        self.change_screen = change_screen
        
        # layout setup
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/modified_scenery.png').convert(), (WIDTH, HEIGHT))
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.change_health,self.change_sickness))

        # level attributes
        self.level = level
        self.max_health = 100
        self.cur_health = 100
        self.max_sickness = 100
        self.cur_sickness = 0
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_timer, 100)

        # ui setup
        self.ui = UI(self.screen)
        self.start_time = int(pygame.time.get_ticks()/500)

    def get_food(self):
        return {
            Chinelao.food_name : Chinelao(),
            Lagarto.food_name : Lagarto(),
        }.get(choice(self.food_names), Chinelao.food_name)
    
    def check_food_collisions(self):
        food_collisions = pygame.sprite.spritecollide(self.player.sprite,self.foods,False)
        if food_collisions:
           for food in food_collisions:
                if food.is_good == True:
                    self.player.sprite.ate_good_food()
                else: self.player.sprite.ate_bad_food()
                food.kill()
    
    def change_health(self,amount):
        self.cur_health += amount
    
    def change_sickness(self,amount):
        self.cur_sickness += amount

    def check_attributes(self):
        if self.cur_sickness < 0:
            self.cur_sickness = 0
        elif self.cur_sickness >= 100:
            self.cur_sickness = 100
            self.change_screen("home_page") # game over
        if self.cur_health > 100:
            self.cur_health = 100
        elif self.cur_health <= 0:
            self.cur_health = 0
            self.change_screen("home_page") # game over

    def update(self):
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == self.food_timer:
                    self.foods.add(self.get_food())
        
        self.screen.blit(self.map_sprite,(0,0))
        
        self.ui.show_health(self.cur_health,self.max_health)
        self.ui.show_sickness(self.cur_sickness,self.max_sickness)
        self.ui.display_time(int(pygame.time.get_ticks()/500) - self.start_time)

        self.player.draw(self.screen)
        self.player.update()
        
        self.foods.draw(self.screen)
        self.foods.update()
        
        self.check_food_collisions()

        self.check_attributes()

        






