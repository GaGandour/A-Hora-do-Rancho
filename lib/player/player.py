from matplotlib import scale
from matplotlib.pyplot import sca
from math import sqrt
import pygame, sys
sys.path.append('./')
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = pygame.image.load('./assets/images/player/gabe-idle-run.png').convert_alpha()
        self.frames_right = []
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(0,0,24,24))))
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(24,0,24,24))))
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(48,0,24,24))))
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(72,0,24,24))))
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(96,0,24,24))))
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(120,0,24,24))))
        self.frames_right.append(pygame.transform.scale2x(self.spritesheet.subsurface(pygame.Rect(144,0,24,24))))
        
        self.frames_left = []
        for frame in self.frames_right:
            self.frames_left.append(pygame.transform.flip(frame,True,False))

        self.frames_index = 0
        self.image = self.frames_right[self.frames_index]
        
        self.x_spawn = WIDTH/2
        self.y_spawn = HEIGHT/2
        self.rect = self.image.get_rect(center = (self.x_spawn, self.y_spawn))

        self.direction =[0,0]
        self.ismoving = False
        self.speed = 3
        self.state = 'RIGHT'

        self.life = 100
        self.max_life = 100
        self.sickness = 0
        self.max_sickness = 100

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction[1] += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction[0] -= 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction[1] -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction[0] += 1
        
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0    
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def walk(self):
        if self.direction != [0,0]:
            self.ismoving = True
            if self.direction[0] * self.direction[1] == 0:
                self.rect.x += round(self.speed * self.direction[0])
                self.rect.y += round(self.speed * self.direction[1])
            else:
                self.rect.x += round(self.speed * 0.707 * self.direction[0])
                self.rect.y += round(self.speed * 0.707 * self.direction[1])

    def animation_state(self):
        if self.direction[0] > 0: self.state = 'RIGHT'
        elif self.direction[0] <0: self.state = 'LEFT'
        
        if self.ismoving:
            self.frames_index = (self.frames_index + 0.15) % len(self.frames_right)
        else: self.frames_index = 0

        if self.state == 'RIGHT':
            self.image = self.frames_right[int(self.frames_index)]
        else: self.image = self.frames_left[int(self.frames_index)]

    def update(self):
        self.life -= 0.1
        self.sickness += 0.1
        # if self.life <= 0 or self.sickness >= self.max_sickness:
        #     self.life = 0
        self.ismoving = False
        self.direction = [0,0]
        self.player_input()
        self.walk()
        self.animation_state()



