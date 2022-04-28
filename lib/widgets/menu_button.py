import pygame

from lib.settings import PIXELED_FONT

class Menu_Button:
    def __init__(self, screen, position, text, function):
        # setup 
        self.screen = screen
        self.function = function 
        size = 32
        color = '#221308'
        self.position = position
        
        text_font = pygame.font.Font(PIXELED_FONT,size)
        self.text_surf = text_font.render(str(text), False, color)
        self.text_rect = self.text_surf.get_rect(center = position)
        
        self.button_bg_image = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/menu_button.png').convert_alpha()) 
        self.button_bg_rect = self.button_bg_image.get_rect(center = position)

        self.was_pressed = False


    def move_button(self):
        self.button_bg_rect.center = (self.position[0], self.position[1] - 5)
        self.text_rect.center = (self.position[0], self.position[1] - 5)


    def move_button_back(self):
        self.button_bg_rect.center = self.position
        self.text_rect.center = self.position


    def update(self):
        self.screen.blit(self.button_bg_image, self.button_bg_rect)
        self.screen.blit(self.text_surf, self.text_rect)
            
        if (not pygame.mouse.get_pressed()[0]) and self.button_bg_rect.collidepoint(pygame.mouse.get_pos()):
            if self.was_pressed: # was released
                self.function()
        
        if self.button_bg_rect.collidepoint(pygame.mouse.get_pos()): # is hovering
            self.move_button()
            if pygame.mouse.get_pressed()[0]: # was pressed
                self.was_pressed = True
                self.move_button_back()
            else:
                self.was_pressed = False
        else:
            self.move_button_back()
            self.was_pressed = False