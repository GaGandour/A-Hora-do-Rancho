import pygame

from lib.settings import CLOCK_FONT

class Player_Status_UI:
    def __init__(self,screen):
        # setup 
        self.display_surface = screen 

        # health and sickness
        self.health_bar = pygame.transform.scale2x(pygame.image.load('./assets/images/ui/health_bar.png').convert_alpha())
        self.health_bar_topleft = (48,24)
        self.sickness_bar = pygame.transform.scale2x(pygame.image.load('./assets/images/ui/sick_bar.png').convert_alpha())
        self.sickness_bar_topleft = (464,24)
        self.bar_max_width = 344
        self.bar_height = 14

        # clock 
        self.clock = pygame.transform.scale2x(pygame.image.load('./assets/images/ui/clock.png').convert_alpha())
        self.clock_rect = self.clock.get_rect(topleft = (848,16))
        self.font = pygame.font.Font(CLOCK_FONT,22)

    def show_health(self,current,full):
        self.display_surface.blit(self.health_bar,(16,16))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)
    
    def show_sickness(self,current,full):
        self.display_surface.blit(self.sickness_bar,(432,16))
        current_sickness_ratio = current / full
        current_bar_width = self.bar_max_width * current_sickness_ratio
        sickness_bar_rect = pygame.Rect(self.sickness_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#4fbd65',sickness_bar_rect)

    def display_time(self,time):
        minute = 11 + int(time/60) 
        seconds = (time % 60)
        str_time = str(minute) + ':' + str(seconds).rjust(2,'0')
        self.display_surface.blit(self.clock,self.clock_rect)
        time_surf = self.font.render(str_time,False,'#ffffff')
        time_rect = time_surf.get_rect(center = (self.clock_rect.centerx,self.clock_rect.centery))
        self.display_surface.blit(time_surf,time_rect)