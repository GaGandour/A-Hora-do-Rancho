import pygame, sys, os
from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
from settings import *


class Game_Over:
    page_name = "game_over"

    def __init__(self, screen, level, start_function):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.level = level
        self.screen = screen
        ## implementar um componente de botao generico
        self.text_font = pygame.font.Font('./assets/images/ui/ARCADEPI.ttf',50)
        self.text_surf = self.text_font.render('Play', False, 'White')
        self.text_rect = self.text_surf.get_rect(center = (480,270))
        self.start_function = start_function

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.bg_surface,(0,0))
        self.screen.blit(self.text_surf, self.text_rect)

        if pygame.mouse.get_pressed()[0] and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            self.start_function(Ranch.page_name)
        