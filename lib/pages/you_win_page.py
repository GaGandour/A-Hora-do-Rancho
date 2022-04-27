import pygame, sys, os
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from customized_text import Customized_Text
from menu_button import Menu_Button



class You_Win_Page:
    page_name = "You Win Page"

    def __init__(self, screen, go_back_to_home_function):
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.screen = screen
        
        self.buttons = [
            Customized_Text(screen, (WIDTH/2, 200), "YOU WIN!!!", size = 100, color='Green'),
            Menu_Button(screen, (WIDTH/2, 360), "Start Menu", go_back_to_home_function),
        ]
        

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.bg_surface,(0,0))                  
        
        if self.buttons:
            for button in self.buttons:
                button.update()

