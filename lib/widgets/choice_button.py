import pygame

class Choice_Button:
    def __init__(self, screen, position, food_class, function):
        # setup 
        self.screen = screen
        self.function = function 
        size = 24
        color = '#221308'
        
        text_font = pygame.font.Font('./assets/fonts/ARCADEPI.ttf',size)
        self.text_surf = text_font.render(food_class.food_name, False, color)
        self.text_rect = self.text_surf.get_rect(center = (position[0], position[1] + 60))
        
        self.cardapio_image = pygame.transform.scale2x(pygame.image.load('./assets/images/ui/cardapio.png').convert_alpha()) 
        self.cardapio_rect = self.cardapio_image.get_rect(center = position)

        self.food_image = pygame.transform.scale(pygame.image.load(food_class.path).convert_alpha(), (90,90))
        self.food_rect = self.food_image.get_rect(center = (position[0], position[1] - 20))
        self.was_pressed = False


    def update(self):
        self.screen.blit(self.cardapio_image, self.cardapio_rect)
        self.screen.blit(self.food_image, self.food_rect)
        self.screen.blit(self.text_surf, self.text_rect)
            
        if (not pygame.mouse.get_pressed()[0]) and self.cardapio_rect.collidepoint(pygame.mouse.get_pos()):
            if self.was_pressed:
                self.function()
        
        if pygame.mouse.get_pressed()[0] and self.cardapio_rect.collidepoint(pygame.mouse.get_pos()):
            self.was_pressed = True
        else:
            self.was_pressed = False