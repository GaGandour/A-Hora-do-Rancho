import pygame, sys, os
from math import sin, cos

from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
from settings import *
from choice_button import Choice_Button


from food_list import FOOD_LIST


    
class Food_Choice:
    page_name = "food_choice"
         
    def __init__(self, screen, change_screen, level, add_food): #, start_function) 
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen
        text_font = pygame.font.Font(PIXELED_FONT,36)
        self.text_surf = text_font.render('Escolha sua comida preferida!', False, 'White')
        self.text_rect = self.text_surf.get_rect(center = (480,100))
        self.shadow_surf = text_font.render('Escolha sua comida preferida!', False, '#221308')
        self.shadow_rect = self.text_surf.get_rect(center = (484,104))
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
            ]
    
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
        self.screen.blit(self.shadow_surf, self.shadow_rect)
        self.screen.blit(self.text_surf, self.text_rect)
        
        
        if self.buttons:
            for button in self.buttons:
                button.update()
