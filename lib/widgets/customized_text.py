import pygame
from math import sin
from settings import PIXELED_FONT

class Customized_Text:
    def __init__(self, screen, position, text, size = 50, color = 'White', rotation = 0, function = lambda : None, pulse = False):
        # setup 
        self.screen = screen
        self.function = function
        
        text_font = pygame.font.Font(PIXELED_FONT,size)
        self.text_surf = text_font.render(text, False, color)
        self.text_surf = pygame.transform.rotate(self.text_surf, rotation)
        self.text_rect = self.text_surf.get_rect(center = position)
        self.was_pressed = False
        self.pulse = pulse
        self.position = position
        self.color = color
        self.rotation = rotation
        self.size = size
        self.text = text


    def update(self):
        if self.pulse:
            text_font = pygame.font.Font(PIXELED_FONT ,25)
            self.text_surf = text_font.render(self.text, False, self.color)
            scale_factor = (1 + 0.2 * sin(pygame.time.get_ticks()*0.003))
            self.text_surf = pygame.transform.scale(self.text_surf, (int(self.text_surf.get_width() * scale_factor), int(self.text_surf.get_height() * scale_factor)))
            self.text_surf = pygame.transform.rotate(self.text_surf, self.rotation)
            
            self.text_rect = self.text_surf.get_rect(center = self.position)
            
        self.screen.blit(self.text_surf, self.text_rect)

        if (not pygame.mouse.get_pressed()[0]) and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            if self.was_pressed:
                self.function()
        
        if pygame.mouse.get_pressed()[0] and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            self.was_pressed = True
        else:
            self.was_pressed = False