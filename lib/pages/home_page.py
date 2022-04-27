import pygame, sys, os
from food_choice import Food_Choice
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from menu_button import Menu_Button



class Home_Page:
    page_name = "home page"

    def __init__(self, screen, change_screen):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.bg_surface = pygame.transform.scale(pygame.image.load('./assets/images/home_page/titlescreen.jpg').convert(), (WIDTH, HEIGHT))
        self.screen = screen
        
        self.buttons = [
            Menu_Button(screen, (480, 220), "Play", lambda: change_screen(Food_Choice.page_name)),
            Menu_Button(screen, (480, 320), "How To Play", lambda: change_screen(Food_Choice.page_name)),
        ]
        

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.bg_surface,(0,0))                  
        
        if self.buttons:
            for button in self.buttons:
                button.update()

