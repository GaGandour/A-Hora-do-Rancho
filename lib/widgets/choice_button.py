import pygame

from lib.settings import PIXELED_FONT

class Choice_Button:
    def __init__(self, screen, position, food_class, function):
        # setup 
        self.screen = screen
        self.function = function 
        size = 24
        color = '#221308'
        self.position = position
        self.text_position = (position[0], position[1] + 60)
        self.food_position = (position[0], position[1] - 20)
        
        text_font = pygame.font.Font(PIXELED_FONT,size)
        self.text_surf = text_font.render(food_class.food_name, False, color)
        self.text_rect = self.text_surf.get_rect(center = self.text_position)
        
        self.cardapio_image = pygame.transform.scale2x(pygame.image.load('./assets/images/ui/cardapio.png').convert_alpha()) 
        self.cardapio_rect = self.cardapio_image.get_rect(center = position)

        self.food_image = pygame.transform.scale(pygame.image.load(food_class.path).convert_alpha(), (90,90))
        self.food_rect = self.food_image.get_rect(center = self.food_position)
        self.was_pressed = False


    def move_button(self):
        self.text_rect.center = (self.text_position[0], self.text_position[1] - 5)
        self.food_rect.center = (self.food_position[0], self.food_position[1] - 5)
        self.cardapio_rect.center = (self.position[0], self.position[1] - 5)      


    def move_button_back(self):
        self.text_rect.center = self.text_position
        self.food_rect.center = self.food_position
        self.cardapio_rect.center = self.position


    def update(self):
        self.screen.blit(self.cardapio_image, self.cardapio_rect)
        self.screen.blit(self.food_image, self.food_rect)
        self.screen.blit(self.text_surf, self.text_rect)
            
        if (not pygame.mouse.get_pressed()[0]) and self.cardapio_rect.collidepoint(pygame.mouse.get_pos()):
            if self.was_pressed: # was released
                self.function()
        
        if self.cardapio_rect.collidepoint(pygame.mouse.get_pos()): # is hovering
            self.move_button()
            if pygame.mouse.get_pressed()[0]: # was pressed
                self.was_pressed = True
                self.move_button_back()
            else:
                self.was_pressed = False
        else:
            self.move_button_back()
            self.was_pressed = False