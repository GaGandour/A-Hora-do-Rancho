from food import Food
import pygame
from settings import *
from random import choice

class Trigger_Burguer(Food):
    food_name = "rancho especial"
    path = "./assets/images/food/burguer.jpg"
    is_good = True

    def __init__(self):
        super().__init__()
        temp_image = pygame.image.load(Trigger_Burguer.path).convert_alpha()
        self.image = pygame.transform.scale(temp_image, (30,30))
        self.mask = pygame.mask.from_surface(self.image)

        self.x_speed = self.y_speed = 0

        (self.x_spawn, self.y_spawn) = choice([
            (45,45),
            (WIDTH-45,45),
            (45,HEIGHT-45),
            (WIDTH-45,HEIGHT-45),
            (WIDTH/3,45),
            (WIDTH/3,HEIGHT-45),
            (2*WIDTH/3,45),
            (2*WIDTH/3,HEIGHT-45),
        ])

        self.rect = self.image.get_rect(topleft = (self.x_spawn, self.y_spawn))


    def update(self):
        super().update()