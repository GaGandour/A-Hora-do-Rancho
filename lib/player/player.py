import pygame, sys, os
sys.path.append('./')
sys.path.append(os.path.join(sys.path[0], 'widgets'))
sys.path.append(os.path.join(sys.path[0], 'objects'))
from settings import *
from support import import_folder
from player_status_ui import Player_Status_UI
from enum import Enum
from trigger_burguer import Trigger_Burguer

class Direction(Enum):
    down = "down"
    up = "up"
    left = "left"
    right = "right"


class Player(pygame.sprite.Sprite):
    def __init__(self, game_over, pass_level, screen, foods, max_time, pause_function, obstacles, start_special_ranch_function):
        super().__init__()
        self.animations = self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations[Direction.down][self.frame_index]
        self.rect = self.image.get_rect(center = (0.4 * WIDTH, 0.5 * HEIGHT))
        self.novision = pygame.transform.scale(pygame.image.load('./assets/images/player/no_vision.png').convert_alpha(), (2*WIDTH, 2*HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.game_over = game_over
        self.screen = screen
        self.foods = foods
        self.max_time = max_time
        self.pass_level = pass_level
        self.pause_function = pause_function
        self.start_special_ranch_function = start_special_ranch_function
        self.good_food_sound = pygame.mixer.Sound(GOOD_FOOD_SOUND)
        self.bad_food_sound = pygame.mixer.Sound(BAD_FOOD_SOUND)

        # player movement
        self.obstacles = obstacles
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3
        self.ismoving = False
        self.stance = Direction.down

        # health/sickness management
        self.max_health = 100
        self.cur_health = 100
        self.max_sickness = 100
        self.cur_sickness = 0

        # ui setup
        self.ui = Player_Status_UI(self.screen)
        self.start_time = int(pygame.time.get_ticks()/1000)
        self.liquid_time = 0
        self.current_time = 0


    def import_character_assets(self):
        # set paths and store sprites
        character_path = './assets/images/player/'
        animations = {
            Direction.down:[],
            Direction.left:[],
            Direction.right:[],
            Direction.up:[]
        }

        for animation in animations.keys():
            full_path = character_path + animation.value
            animations[animation] = import_folder(full_path)

        return animations


    def get_input(self):
        keys = pygame.key.get_pressed()
        
        # reset variabLes
        self.direction.update(0,0)
        self.ismoving = False
        
        # check player input
        if keys[pygame.K_ESCAPE]:
            self.pause_function()
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


    def get_stance(self):
        if self.direction.x > 0:
            self.stance = Direction.right
        elif self.direction.x < 0:
            self.stance = Direction.left
        elif self.direction.y > 0:
                self.stance = Direction.down
        elif self.direction.y < 0:
            self.stance = Direction.up


    def get_current_time(self):
        return self.current_time


    def walk(self):
        if self.ismoving:
            if self.direction.x * self.direction.y == 0:
                self.rect.x += round(self.speed * self.direction.x)
                self.rect.y += round(self.speed * self.direction.y)
            else:
                self.rect.x += round(self.speed * 0.707 * self.direction.x)
                self.rect.y += round(self.speed * 0.707 * self.direction.y)


    def constraint_walk(self):
        if self.ismoving:
            for rect in self.obstacles:
                if self.rect.colliderect(rect):
                    if 0 < self.rect.right - rect.left < self.speed+1:
                        self.rect.right = rect.left
                    if 0 < rect.right - self.rect.left < self.speed+1:
                        self.rect.left = rect.right
                    if 0 < self.rect.bottom - rect.top < self.speed+1:
                        self.rect.bottom = rect.top
                    if 0 < rect.bottom - self.rect.top < self.speed+1:
                        self.rect.top = rect.bottom


    def animation_state(self):
        animation = self.animations[self.stance]

        # loop frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 1
        
        if self.ismoving:
            self.image = animation[int(self.frame_index)]
        else: self.image = animation[0]

    
    def change_health(self,amount):
        self.cur_health += amount


    def change_sickness(self,amount):
        self.cur_sickness += amount


    def decay_self(self): 
        self.change_health(-0.1)
        self.change_sickness(-0.05)


    def ate_good_food(self):
        self.change_health(+20)
        self.good_food_sound.play()


    def ate_bad_food(self):
        self.change_sickness(+40)
        self.bad_food_sound.play()
        

    def check_food_collisions(self):
        food_collisions = pygame.sprite.spritecollide(self,self.foods,False)
        if food_collisions:
            # only check mask_collision when there are rect collisions
            # otherwise it can get laggy when there are lots of foods
            mask_collisions = pygame.sprite.spritecollide(self,food_collisions,False,pygame.sprite.collide_mask)
            for food in mask_collisions:
                if food.food_name == Trigger_Burguer.food_name:
                    self.ate_good_food()
                    self.start_special_ranch_function()
                elif food.is_good == True:
                    self.ate_good_food()
                else:
                    self.ate_bad_food()
                food.kill()
                

    def check_attributes(self):
        if self.cur_sickness < 0:
            self.cur_sickness = 0
        elif self.cur_sickness >= 100:
            self.cur_sickness = 100
            self.game_over()
        if self.cur_health > 100:
            self.cur_health = 100
        elif self.cur_health <= 0:
            self.cur_health = 0
            self.game_over()

    
    def show_ui(self, playing):
        self.ui.show_health(self.cur_health, self.max_health)
        self.ui.show_sickness(self.cur_sickness, self.max_sickness)
        self.ui.display_time(self.current_time)
        
        if playing:
            self.current_time = int(pygame.time.get_ticks()/1000) - self.start_time + self.liquid_time
            if (self.current_time > self.max_time):
                self.pass_level()
        else:
            self.start_time = int(pygame.time.get_ticks()/1000)
            self.liquid_time = self.current_time
        
        


    def remove_vision(self):
        self.screen.blit(self.novision,(self.rect.x-WIDTH+20,self.rect.y-HEIGHT+10))


    def update(self):
        self.decay_self()
        self.check_food_collisions()
        self.check_attributes()
    
        self.get_input()
        self.get_stance()
        self.walk()
        self.constraint_walk()
        self.animation_state()
        
