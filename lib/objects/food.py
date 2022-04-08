import pygame, sys, abc
sys.path.append('./')
from settings import *
from random import choice

class Food(pygame.sprite.Sprite, abc.ABC):
    def __init__(self):
        super().__init__()
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
    

    @abc.abstractmethod
    def update(self):
        self.destroy()

    
    def destroy(self):
        if self.rect.x < -20 or self.rect.x > WIDTH + 20 or self.rect.y < -20 or self.rect.y > HEIGHT + 20:
            self.kill()

    
    @classmethod
    def set_preference(cls, good):
        cls.is_good = good