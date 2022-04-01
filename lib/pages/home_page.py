import pygame, sys, os
from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from menu_button import Menu_Button


class Home_Page:
    page_name = "home_page"

    def __init__(self, screen, level, change_screen):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.level = level
        self.screen = screen
        
        self.buttons = [
            Menu_Button(screen, (480, 270), "Play", lambda: change_screen(Ranch.page_name)),
        ]
        

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.bg_surface,(0,0))

        if self.buttons:
            for button in self.buttons:
                button.update()

