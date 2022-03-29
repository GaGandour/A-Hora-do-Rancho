import pygame, sys
sys.path.append('./')
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['down'][self.frame_index]
        self.rect = self.image.get_rect(center = (0.5 * WIDTH, 0.5 * HEIGHT))

        # ui setup
        self.screen = screen

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3
        self.ismoving = False
        self.status = 'down'

        # player health and sickness
        self.alive = True
        self.life = 100
        self.sick = 0
        self.max_life = 100
        self.max_sick = 100
        self.length_of_bars = 0.5 * WIDTH
        self.ratio_life_to_bar = self.length_of_bars / self.max_life
        self.ratio_sick_to_bar = self.length_of_bars / self.max_sick
        self.life_rect = pygame.Rect(0.25*WIDTH,25,self.length_of_bars,20)
        self.sick_rect = pygame.Rect(0.25*WIDTH,50,self.length_of_bars,20)

    def import_character_assets(self):
        # set paths and store sprites
        character_path = './assets/images/player/'
        self.animations = {'down':[],'left':[],'right':[],'up':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        # reset variabLes
        self.direction.update(0,0)
        self.ismoving = False
        
        # check player input
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x -= 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x += 1
        
        # check final movement
        if self.direction != (0,0):
            self.ismoving = True

        # constrain to ranch
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0    
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def get_status(self):
        if self.direction.x > 0:
            self.status = 'right'
        elif self.direction.x < 0:
            self.status = 'left'
        elif self.direction.y > 0:
                self.status = 'down'
        elif self.direction.y < 0:
            self.status = 'up'

    def walk(self):
        if self.ismoving:
            if self.direction.x * self.direction.y == 0:
                self.rect.x += round(self.speed * self.direction.x)
                self.rect.y += round(self.speed * self.direction.y)
            else:
                self.rect.x += round(self.speed * 0.707 * self.direction.x)
                self.rect.y += round(self.speed * 0.707 * self.direction.y)

    def animation_state(self):
        animation = self.animations[self.status]

        # loop frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        if self.ismoving:
            self.image = animation[int(self.frame_index)]
        else: self.image = animation[0]

    def draw_ui(self):
        # draw health
        pygame.draw.rect(self.screen,(255,0,0),(0.25*WIDTH,25,self.ratio_life_to_bar*self.life,20))
        pygame.draw.rect(self.screen,(255,255,255),self.life_rect,4)
        # draw sickness
        pygame.draw.rect(self.screen,(0,255,0),(0.25*WIDTH,50,self.ratio_sick_to_bar*self.sick,20))
        pygame.draw.rect(self.screen,(255,255,255),self.sick_rect,4)

    def check_health(self): 
        self.life -= 0.1
        self.sick += 0.1
        if self.life <= 0:
            self.live = 0
            self.alive = False
        if self.sick >= self.max_sick:
            self.sick = self.max_sick
            self.alive = False
    
    def update(self):
        self.check_health()
        self.draw_ui()
        self.get_input()
        self.get_status()
        self.walk()
        self.animation_state()

        