from objects.food import Food
import pygame
from math import sqrt

class Costelinha(Food):
    food_name = "Costelinha"
    path = "./assets/images/food/ribs.png"
    is_good = False

    def __init__(self):
        super().__init__()
        temp_image = pygame.image.load(Costelinha.path).convert_alpha()
        self.image = pygame.transform.scale(temp_image, (30,30))
        self.mask = pygame.mask.from_surface(self.image)

        if self.x_speed != 0 and self.y_speed != 0:
            self.x_speed = round(self.x_speed/sqrt(2))
            self.y_speed = round(self.y_speed/sqrt(2))

        self.rect = self.image.get_rect(topleft = (self.x_spawn, self.y_spawn))


    def update(self):
        super().update()
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed