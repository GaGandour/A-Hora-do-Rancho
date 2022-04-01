import pygame

class Menu_Button:
    def __init__(self,screen, position, text, function):
        # setup 
        self.screen = screen
        self.function = function 
        
        self.text_font = pygame.font.Font('./assets/fonts/ARCADEPI.ttf',50)
        self.text_surf = self.text_font.render(text, False, 'White')
        self.text_rect = self.text_surf.get_rect(center = position)


    def update(self):
        self.screen.blit(self.text_surf, self.text_rect)
        if pygame.mouse.get_pressed()[0] and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            self.function()