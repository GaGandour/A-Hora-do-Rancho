import pygame, sys, os
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from menu_button import Menu_Button


class Game_Over:
    page_name = "game over"

    def __init__(self, screen, go_back_to_home_function):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.screen = screen
        
        self.buttons = [
            Menu_Button(screen, (WIDTH/2, 230), "Game Over!!!", None, size = 100),
            Menu_Button(screen, (WIDTH/2, 280), "Go To Start Menu", go_back_to_home_function, color='Red'),
        ]
        

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.bg_surface,(0,0))

        if self.buttons:
            for button in self.buttons:
                button.update()
