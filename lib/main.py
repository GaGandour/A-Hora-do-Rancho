import pygame, sys, os
sys.path.append(os.path.join(sys.path[0],'pages'))

from settings import *
from ranch import Ranch

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Hora do Rancho')
        self.level = 0
        self.screen_name = "start menu"
        self.page = Ranch(self.screen, self.level)

    def run(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.page.update()
            self.clock.tick(FPS)

    def change_screen(self, screen_name):
        self.screen_name = screen_name
        self.page = {
            Ranch.page_name : Ranch()
        }.get(screen_name, Ranch.page_name)


if __name__ == '__main__':
    game = Game()
    game.run()