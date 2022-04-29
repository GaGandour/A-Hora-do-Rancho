import pygame

class Back_Button:
    def __init__(self, screen, position, function):
        # setup 
        self.screen = screen
        self.function = function 
        self.position = position
        
        self.button_bg_image = pygame.transform.scale(pygame.image.load('./assets/images/home_page/back_button.png').convert_alpha(), (30,30)) 
        self.button_bg_rect = self.button_bg_image.get_rect(center = position)

        self.was_pressed = False


    def move_button(self):
        self.button_bg_rect.center = (self.position[0], self.position[1] - 2)


    def move_button_back(self):
        self.button_bg_rect.center = self.position


    def update(self):
        self.screen.blit(self.button_bg_image, self.button_bg_rect)
            
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