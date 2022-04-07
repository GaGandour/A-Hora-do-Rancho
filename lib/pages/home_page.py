import pygame, sys, os
from food_choice import Food_Choice
from ranch import Ranch
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from menu_button import Menu_Button


class Home_Page:
    page_name = "home page"

    def __init__(self, screen, change_screen):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.bg_surface = pygame.Surface((WIDTH,HEIGHT))
        self.bg_surface.fill("#2e2e2e")
        self.screen = screen
        
        self.buttons = [
            Menu_Button(screen, (480, 270), "Play", lambda: change_screen(Ranch.page_name)),
        ]
        

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.bg_surface,(0,0))

        if pygame.mouse.get_pressed()[0] and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            self.start_function(Food_Choice.page_name)
            
            
        # for event in pygame.event.get():
        #         if event.type == pygame.MOUSEBUTTONDOWN :
                    
        #             if event and self.text_rect.collidepoint(event.pos): print('collision')   
                
                 
                  
        
        if self.buttons:
            for button in self.buttons:
                button.update()

