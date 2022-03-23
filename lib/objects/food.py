from matplotlib import scale
from matplotlib.pyplot import sca
import pygame, sys
sys.path.append('./')
from settings import *

class Food(pygame.sprite.Sprite):
    def __init__(self, food):
        super().__init__()
        self.food = food
        if food == CHINELAO_NAME:
            temp_image = pygame.image.load('./assets/images/pork.png').convert_alpha()
            self.image = pygame.transform.scale(temp_image, (30,30))
        else:
            self.image = pygame.image.load('./assets/images/pork.png')
            



        self.x_spawn = 10
        self.y_spawn = 10
        self.rect = self.image.get_rect(topleft = (self.x_spawn, self.y_spawn))

    def update(self):
        self.rect.x += 2
        self.rect.y += 2
        self.destroy()

    def destroy(self):
        if self.rect.x < -100 or self.rect.x > WIDTH + 10 or self.rect.y < -10 or self.rect.y > HEIGHT + 10:
            self.kill()



