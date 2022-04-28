import pygame, sys, os
from food_choice import Food_Choice
from how_to_play import How_To_Play
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'objects'))
sys.path.append(os.path.join(sys.path[0], 'widgets'))
from settings import *
from menu_button import Menu_Button
from customized_text import Customized_Text
from math import sin, cos
from random import choice


class Home_Page:
    page_name = "home page"

    def __init__(self, screen, change_screen):
        #self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/scenery.jpg').convert(), (WIDTH, HEIGHT))
        self.background = pygame.transform.scale(pygame.image.load('./assets/images/home_page/title_bg.png').convert(), (WIDTH, HEIGHT))
        self.title = pygame.transform.scale(pygame.image.load('./assets/images/home_page/title.png').convert_alpha(), (662,124))
        self.moving_bg = pygame.transform.scale2x(pygame.image.load('./assets/images/home_page/moving_bg.png').convert_alpha())
        self.screen = screen

        random_text = choice([
            'Almoço grátis!',
            'Só iguaria!',
            'Melhor lugar para comer!',
            '9 a cada 10 estudantes recomendam!',
            'Uhuuuuu!!!',
            'Trouxe o crachá?',
            '"Moqueca de novo???"',
        ])
        
        self.buttons = [
            Menu_Button(screen, (480, 274), "Play", lambda: change_screen(Food_Choice.page_name)),
            Menu_Button(screen, (480, 422), "How To Play", lambda: change_screen(How_To_Play.page_name)),
            Customized_Text(screen, (752, 192), random_text, size=20, color='#221308', rotation=20, pulse=True),
            Customized_Text(screen, (750, 190), random_text, size=20, color='Yellow', rotation=20, pulse=True),
        ]

    def update(self):
        pygame.display.update()
        
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.moving_bg,(-250+50*cos(pygame.time.get_ticks()*0.0005),-200+50*sin(pygame.time.get_ticks()*0.0005)))
        self.screen.blit(self.title,(152,56))
        
        if self.buttons:
            for button in self.buttons:
                button.update()

