from food import Food
import pygame
from settings import *
from random import choice
from math import sqrt

class Lagarto(Food):
    food_name = "lagarto"
    is_good = True

    def __init__(self):
        super().__init__()
        temp_image = pygame.image.load('./assets/images/beef.png').convert_alpha()
        self.image = pygame.transform.scale(temp_image, (30,30))
        
        (self.x_spawn, self.y_spawn, self.x_speed, self.y_speed) = choice([
            (-10,-10, 4, 4),
            (WIDTH+10,-10, -4, 4),
            (-10,HEIGHT+10, 4, -4),
            (WIDTH+10,HEIGHT+10, -4, -4),
            (WIDTH/3,-10, 0, 4),
            (WIDTH/3,HEIGHT+10, 0, 4),
            (2*WIDTH/3,-10, 0, 4),
            (2*WIDTH/3,HEIGHT+10, 0, -4),
            (-10,HEIGHT/3, 4, 0),
            (WIDTH+10,HEIGHT/3, -4, 0),
            (-10,2*HEIGHT/3, 4, 0),
            (WIDTH+10,2*HEIGHT/3, -4, 0),
            (WIDTH/2,HEIGHT+10, 0, -4),
            (WIDTH/2,-10, 0, 4),
            (WIDTH+10,HEIGHT/2, -4, 0),
            (-10,HEIGHT/2, 4, 0),
        ])

        if self.x_speed != 0 and self.y_speed != 0:
            self.x_speed = round(self.x_speed/sqrt(2))
            self.y_speed = round(self.y_speed/sqrt(2))

        self.rect = self.image.get_rect(topleft = (self.x_spawn, self.y_spawn))

    def update(self):
        super().update()
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    