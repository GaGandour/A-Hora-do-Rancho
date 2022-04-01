import pygame, sys
sys.path.append('./')
from settings import *
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,change_health,change_sickness):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['down'][self.frame_index]
        self.rect = self.image.get_rect(center = (0.5 * WIDTH, 0.5 * HEIGHT))

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.ismoving = False
        self.stance = 'down'

        # health/sickness management
        self.change_health = change_health
        self.change_sickness = change_sickness

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
        if self.rect.bottom > HEIGHT-40:
            self.rect.bottom = HEIGHT-40
        if self.rect.left < 40:
            self.rect.left = 40
        if self.rect.top < 100:
            self.rect.top = 100    
        if self.rect.right > WIDTH-40:
            self.rect.right = WIDTH-40

    def get_stance(self):
        if self.direction.x > 0:
            self.stance = 'right'
        elif self.direction.x < 0:
            self.stance = 'left'
        elif self.direction.y > 0:
                self.stance = 'down'
        elif self.direction.y < 0:
            self.stance = 'up'

    def walk(self):
        if self.ismoving:
            if self.direction.x * self.direction.y == 0:
                self.rect.x += round(self.speed * self.direction.x)
                self.rect.y += round(self.speed * self.direction.y)
            else:
                self.rect.x += round(self.speed * 0.707 * self.direction.x)
                self.rect.y += round(self.speed * 0.707 * self.direction.y)

    def animation_state(self):
        animation = self.animations[self.stance]

        # loop frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        if self.ismoving:
            self.image = animation[int(self.frame_index)]
        else: self.image = animation[0]

    def decay_self(self): 
        self.change_health(-0.1)
        self.change_sickness(-0.05)

    def ate_good_food(self):
        self.change_health(+20)
    
    def ate_bad_food(self):
        self.change_sickness(+40)
        
    def update(self):
        self.decay_self()
        self.get_input()
        self.get_stance()
        self.walk()
        self.animation_state()

        