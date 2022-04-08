import pygame, sys, os
from choice_button import Choice_Button
from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
from settings import *
from choice_button import Choice_Button

from food_list import FOOD_LIST


    
class Food_Choice:
    page_name = "food_choice"
         
    def __init__(self, screen, change_screen,level, add_food): #, start_function) 
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        text_font = pygame.font.Font('./assets/fonts/ARCADEPI.ttf',45)
        self.text_surf = text_font.render('Escolha sua comida preferida!', False, 'White')
        self.text_rect = self.text_surf.get_rect(center = (480,70))
        self.start_function = change_screen
        self.add_food = add_food

        food_index = level*2 - 2
        first_food = FOOD_LIST[food_index]
        sec_food = FOOD_LIST[food_index + 1]

        self.buttons = [
                Choice_Button(screen, (330, 266), first_food, lambda : self.move_to_phase(first_food, sec_food, 1)),
                Choice_Button(screen, (628, 266), sec_food, lambda: self.move_to_phase(first_food, sec_food, 2)),
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
