import pygame, sys, os
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from math import sin, cos
from back_button import Back_Button



class How_To_Play:
    page_name = "how to play"

    def __init__(self, screen, change_screen):
        self.background = pygame.transform.scale(pygame.image.load('./assets/images/home_page/title_bg.png').convert(), (WIDTH, HEIGHT))
        self.moving_bg = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/moving_bg.png').convert_alpha())
        self.how_to_play = pygame.image.load('./assets/images/home_page/howtoplay.png').convert_alpha()
        self.screen = screen

        self.buttons = [
            Back_Button(screen, (32, 32), lambda: change_screen("home page")),
        ]

    def update(self):
        pygame.display.update()

        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.moving_bg,(-250+50*cos(pygame.time.get_ticks()*0.0005),-200+50*sin(pygame.time.get_ticks()*0.0005)))
        self.screen.blit(self.how_to_play,(0,0))

        if self.buttons:
            for button in self.buttons:
                button.update()