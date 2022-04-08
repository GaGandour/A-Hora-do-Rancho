import pygame, sys, os
from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
from settings import *
from menu_button import Menu_Button

from food_list import FOOD_LIST


    
class Food_Choice:
    page_name = "food_choice"
         
    def __init__(self, screen, change_screen,level, add_food): #, start_function) 
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.text_font = pygame.font.Font('./assets/fonts/ARCADEPI.ttf',50)
        self.text_surf = self.text_font.render('Escolha sua comida preferida!', False, 'White')
        self.text_rect = self.text_surf.get_rect(center = (480,70))
        self.start_function = change_screen
        self.add_food = add_food

        self.food_index = level*2 - 2
        self.first_food_pair = FOOD_LIST[self.food_index]
        self.sec_food_pair = FOOD_LIST[self.food_index + 1]

        self.buttons = [
                Menu_Button(screen, (280, 320), self.first_food_pair[0], lambda : self.move_to_phase( self.first_food_pair[1], self.sec_food_pair[1], 1)),
                Menu_Button(screen, (680, 320), self.sec_food_pair[0], lambda: self.move_to_phase(self.first_food_pair[1], self.sec_food_pair[1], 2)),
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
        
        self.screen.blit(self.bg_surface,(0,0))
        self.screen.blit(self.text_surf, self.text_rect)
        
        if self.buttons:
            for button in self.buttons:
                button.update()
