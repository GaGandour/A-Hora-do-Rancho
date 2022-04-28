import pygame, sys, os
from math import sin, cos

sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))

from settings import *
from choice_button import Choice_Button
from back_button import Back_Button

from customized_text import Customized_Text
from ranch import Ranch

from food_list import FOOD_LIST

    
class Food_Choice:
    page_name = "food_choice"
         
    def __init__(self, screen, change_screen, level, add_food): #, start_function) 
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen
        self.start_function = change_screen
        self.add_food = add_food

        self.background = pygame.transform.scale(pygame.image.load('./assets/images/home_page/title_bg.png').convert(), (WIDTH, HEIGHT))
        self.title = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/title.png').convert_alpha())
        self.moving_bg = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/moving_bg.png').convert_alpha())

        food_index = level*2 - 2
        first_food = FOOD_LIST[food_index]
        sec_food = FOOD_LIST[food_index + 1]

        self.buttons = [
                Choice_Button(screen, (300, 320), first_food, lambda : self.move_to_phase(first_food, sec_food, 1)),
                Choice_Button(screen, (658, 320), sec_food, lambda: self.move_to_phase(first_food, sec_food, 2)),
                Customized_Text(screen, (484, 104), "Escolha sua comida preferida!", size = 36, color = '#221308'),
                Customized_Text(screen, (480, 100), "Escolha sua comida preferida!", size = 36, color = 'White')
            ]
        if level == 1:
            self.buttons.append(Back_Button(screen, (32, 32), lambda: change_screen("home page")))
    
    @staticmethod
    def set_preferences(food_class1, food_class2, preference):
        food_class1.set_preference(True if preference == 1 else False)
        food_class2.set_preference(False if preference == 1 else True)


    def move_to_phase(self, food_class1, food_class2, preference):
        self.set_preferences(food_class1, food_class2, preference)
        self.add_food(food_class1.food_name)
        self.add_food(food_class2.food_name)
        self.start_function(Ranch.page_name)


    def update(self):
        
        pygame.display.update()
        
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.moving_bg,(-250+50*cos(pygame.time.get_ticks()*0.0005),-200+50*sin(pygame.time.get_ticks()*0.0005)))
        
        if self.buttons:
            for button in self.buttons:
                button.update()
