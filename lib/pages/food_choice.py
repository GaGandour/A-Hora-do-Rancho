import pygame, sys, os
from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
from settings import *


class Food_Choice:
    page_name = "food_choice"
    
    def __init__(self, screen, level, start_function):
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.level = level
        self.screen = screen
        self.text_font = pygame.font.Font(None,50)
        self.text_surf = self.text_font.render('Escolha sua comida preferida!', False, 'Black')
        self.text_rect = self.text_surf.get_rect(center = (480,70))
        self.start_function = start_function

    def update(self):
        
        pygame.display.update()
        
        self.screen.blit(self.map_sprite,(0,0))
        self.screen.blit(self.text_surf, self.text_rect)