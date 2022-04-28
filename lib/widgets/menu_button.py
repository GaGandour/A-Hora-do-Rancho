import pygame

from lib.settings import PIXELED_FONT

class Menu_Button:
    def __init__(self, screen, position, text, function):
        # setup 
        self.screen = screen
        self.function = function 
        size = 32
        color = '#221308'
        
        text_font = pygame.font.Font(PIXELED_FONT,size)
        self.text_surf = text_font.render(str(text), False, color)
        self.text_rect = self.text_surf.get_rect(center = (position[0], position[1]))
        
        self.button_bg_image = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/menu_button.png').convert_alpha()) 
        self.button_bg_rect = self.button_bg_image.get_rect(center = position)

        self.was_pressed = False


    def update(self):
        self.screen.blit(self.button_bg_image, self.button_bg_rect)
        self.screen.blit(self.text_surf, self.text_rect)
            
        if (not pygame.mouse.get_pressed()[0]) and self.button_bg_rect.collidepoint(pygame.mouse.get_pos()):
            if self.was_pressed:
                self.function()
        
        if pygame.mouse.get_pressed()[0] and self.button_bg_rect.collidepoint(pygame.mouse.get_pos()):
            self.was_pressed = True
        else:
            self.was_pressed = False