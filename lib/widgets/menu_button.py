import pygame

class Menu_Button:
    def __init__(self, screen, position, text, function, size = 50, color = 'White'):
        # setup 
        self.screen = screen
        self.function = function 
        
        text_font = pygame.font.Font('./assets/fonts/ARCADEPI.ttf',size)
        self.text_surf = text_font.render(text, False, color)
        self.text_rect = self.text_surf.get_rect(center = position)
        self.was_pressed = False


    def update(self):
        self.screen.blit(self.text_surf, self.text_rect)

        if (not pygame.mouse.get_pressed()[0]) and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            if self.was_pressed:
                self.function()
        
        if pygame.mouse.get_pressed()[0] and self.text_rect.collidepoint(pygame.mouse.get_pos()):
            self.was_pressed = True
        else:
            self.was_pressed = False