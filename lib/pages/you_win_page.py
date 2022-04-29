import pygame, sys, os
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from customized_text import Customized_Text
from menu_button import Menu_Button
from math import sin, cos


class You_Win_Page:
    page_name = "You Win Page"

    def __init__(self, screen, go_back_to_home_function):
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.screen = screen
        self.background = pygame.transform.scale(pygame.image.load('./assets/images/home_page/title_bg.png').convert(), (WIDTH, HEIGHT))
        self.moving_bg = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/moving_bg.png').convert_alpha())
        
        self.buttons = [
            Customized_Text(screen, (WIDTH/2+4, 190+4), "YOU WIN!!!", size = 100, color='Black'),
            Customized_Text(screen, (WIDTH/2, 190), "YOU WIN!!!", size = 100, color='Green'),
            Menu_Button(screen, (WIDTH/2, 350), "Back to Menu", go_back_to_home_function),
        ]
        

    def update(self):
        pygame.display.update()
        
        
        self.screen.blit(self.bg_surface,(0,0))                  
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.moving_bg,(-250+50*cos(pygame.time.get_ticks()*0.0005),-200+50*sin(pygame.time.get_ticks()*0.0005)))
        if self.buttons:
            for button in self.buttons:
                button.update()

