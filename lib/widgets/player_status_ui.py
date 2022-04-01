import pygame

class Player_Status_UI:
    def __init__(self,screen):
        # setup 
        self.display_surface = screen 

        # health and sickness
        self.health_bar = pygame.image.load('./assets/images/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (309,23)
        self.sickness_bar = pygame.image.load('./assets/images/ui/sickness_bar.png').convert_alpha()
        self.sickness_bar_topleft = (309,60)
        self.bar_max_width = 344
        self.bar_height = 14

        # clock 
        self.clock = pygame.image.load('./assets/images/ui/clock.png').convert_alpha()
        self.clock_rect = self.clock.get_rect(topleft = (800,20))
        self.font = pygame.font.Font('./assets/fonts/ARCADEPI.ttf',30)

    def show_health(self,current,full):
        self.display_surface.blit(self.health_bar,(277,0))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)
    
    def show_sickness(self,current,full):
        self.display_surface.blit(self.sickness_bar,(277,37))
        current_sickness_ratio = current / full
        current_bar_width = self.bar_max_width * current_sickness_ratio
        sickness_bar_rect = pygame.Rect(self.sickness_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#4fbd65',sickness_bar_rect)

    def display_time(self,time):
        self.display_surface.blit(self.clock,self.clock_rect)
        time_surf = self.font.render(str(time),False,'#ffffff')
        time_rect = time_surf.get_rect(midleft = (self.clock_rect.right + 4,self.clock_rect.centery))
        self.display_surface.blit(time_surf,time_rect)