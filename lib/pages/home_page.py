import pygame, sys, os
from food_choice import Food_Choice
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from new_menu_button import New_Menu_Button
from math import sin, cos



class Home_Page:
    page_name = "home page"

    def __init__(self, screen, change_screen):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.background = pygame.transform.scale(pygame.image.load('./assets/images/home_page/title_bg.png').convert(), (WIDTH, HEIGHT))
        self.title = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/title.png').convert_alpha())
        self.moving_bg = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/moving_bg.png').convert_alpha())
        self.screen = screen
        
        self.buttons = [
            New_Menu_Button(screen, (480, 264), "Play", lambda: change_screen(Food_Choice.page_name)),
            New_Menu_Button(screen, (480, 412), "How To Play", lambda: change_screen(Food_Choice.page_name)),
        ]

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.moving_bg,(-250+50*cos(pygame.time.get_ticks()*0.0005),-200+50*sin(pygame.time.get_ticks()*0.0005)))
        self.screen.blit(self.title,(152,46))
        
        if self.buttons:
            for button in self.buttons:
                button.update()

