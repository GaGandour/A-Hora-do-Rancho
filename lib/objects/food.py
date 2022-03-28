import pygame, sys
sys.path.append('./')
from settings import *
# mm adicionando comentário
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
    def update(self):
        self.destroy()

    def destroy(self):
        if self.rect.x < -20 or self.rect.x > WIDTH + 20 or self.rect.y < -20 or self.rect.y > HEIGHT + 20:
            self.kill()
