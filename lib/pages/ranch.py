import pygame
from random import choice, randint

from player.player import Player
from widgets.menu_button import Menu_Button
from widgets.customized_text import Customized_Text
from objects.trigger_burguer import Trigger_Burguer
from objects.burguer import Burguer

from settings import *
from food_list import *


class Ranch:
    page_name = "ranch"

    def __init__(self, screen, level, food_names, go_to_home_page, pass_level, game_over):
        # general setup
        self.screen = screen
        self.go_to_home_page = go_to_home_page
        self.game_over = game_over
        self.max_time = 30
        self.playing = True
        self.is_special_ranch = False
        self.there_is_burguer = False
        self.special_ranch_start_time = 0
        self.blackout_start_time = randint(7,18)
        self.is_blind = False
        
        # layout setup
        self.map_sprite = pygame.transform.scale(pygame.image.load('./assets/maps/soldier_ranch_16x16.png').convert(), (WIDTH, HEIGHT))
        self.map_sprite_always_on_top = pygame.transform.scale(pygame.image.load('./assets/maps/soldier_ranch_16x16_always_on_top.png').convert_alpha(), (WIDTH, HEIGHT))
        obstacles = []
        # add borders
        obstacles.append(pygame.Rect(0,0,960,74))
        obstacles.append(pygame.Rect(0,0,30,540))
        obstacles.append(pygame.Rect(930,0,30,540))
        obstacles.append(pygame.Rect(0,528,960,12))
        # add buffets
        obstacles.append(pygame.Rect(162,74,124,30))
        for i in range(3):
            obstacles.append(pygame.Rect(162,222+96*i,124,10))
        # add tables
        obstacles.append(pygame.Rect(388,74,26,124))
        for i in range(4):
            obstacles.append(pygame.Rect(484+96*i,74,26,124))
            obstacles.append(pygame.Rect(484+96*i,286,26,40))
            obstacles.append(pygame.Rect(484+96*i,414,26,114))
        
        self.pause_surface = pygame.Surface((WIDTH,HEIGHT))  # the size of your rect
        self.pause_surface.fill("#2e2e2e")  # this fills the entire surface
        self.pause_surface.set_alpha(156)   # alpha level

        # level attributes
        self.level = level
        
        # foods
        self.food_names = food_names
        self.foods = pygame.sprite.Group()
        self.food_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.food_event, millis = 24 - 3*level)
        self.special_ranch_event = pygame.USEREVENT + 2
        pygame.time.set_timer(self.special_ranch_event, 400)
        
        # player
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(game_over, pass_level, screen, self.foods, self.max_time, self.pause, obstacles, self.start_special_ranch))

        # pause ui
        self.pause_buttons = [
            Menu_Button(screen, (480, 200), "Resume", function = lambda: self.pause()),
            Menu_Button(screen, (480, 360), "Back To Menu", function = lambda: self.go_to_home_page()),
        ]
        
        self.blind_text = Customized_Text(screen, (480, 500), "Power's out!!!")
    

    def get_food(self):
        food_dictionary = {}
        for food in FOOD_LIST:
            food_dictionary[food.food_name] = food

        return food_dictionary.get(choice(self.food_names), "")
        

    def pause(self):
        self.playing = not self.playing


    def start_special_ranch(self):
        self.is_special_ranch = True
        self.special_ranch_start_time = self.player.sprite.get_current_time()


    def stop_special_ranch(self):
        self.is_special_ranch = False
        self.there_is_burguer = False

    
    def blackout(self):
        self.is_blind = True
        pygame.mixer.Sound(BLACKOUT_SOUND).play()
        pygame.mixer.music.set_volume(0.2)

    
    def unblackout(self):
        self.is_blind = False
        pygame.mixer.music.set_volume(1)


    def update(self):
        pygame.display.update()
        if self.playing:
            for event in pygame.event.get():
                    if event.type == self.food_event:
                        if not self.is_special_ranch:
                            self.foods.add(self.get_food()())
                        else:
                            self.foods.add(Burguer())

                    if event.type == self.special_ranch_event and not self.is_special_ranch and not self.there_is_burguer and self.level >= 2:
                        self.foods.add(Trigger_Burguer())
                        self.there_is_burguer = True

                    if self.blackout_start_time == self.player.sprite.get_current_time() and not self.is_blind and self.level >= 3:
                        self.blackout()

            if self.is_special_ranch:
                if self.player.sprite.get_current_time() - self.special_ranch_start_time > 5:
                    self.stop_special_ranch()

            if self.is_blind:
                if self.player.sprite.get_current_time() - self.blackout_start_time > 10:
                    self.unblackout()

            self.screen.blit(self.map_sprite,(0,0))
        
            self.player.draw(self.screen)
            self.player.update()
            
            self.screen.blit(self.map_sprite_always_on_top,(0,0))

            self.foods.draw(self.screen)
            self.foods.update()
            
            if self.is_blind:
                self.player.sprite.remove_vision()

            self.player.sprite.show_ui(True)
        else:
            self.screen.blit(self.map_sprite,(0,0))

            self.player.draw(self.screen)
            self.player.sprite.show_ui(False)

            self.screen.blit(self.map_sprite_always_on_top,(0,0))

            self.foods.draw(self.screen)

            if self.is_blind:
                self.player.sprite.remove_vision()
                
            self.screen.blit(self.pause_surface, (0,0))

            if self.pause_buttons:
                for button in self.pause_buttons:
                    button.update()
        
        if self.is_blind:
            self.blind_text.update()