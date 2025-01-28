import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.position = (x, y)

        # Assigning all the images including two for a walk animation
        self.walk1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        self.walk2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.jumps = pygame.image.load("graphics/Player/jump.png").convert_alpha()
        self.stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        
        # Setting the two frames of walk animation as a list
        self.walk = [self.walk1, self.walk2]
        
        # creating a number to increment so the walk animations will cycle (might relocate later)
        self.walk_index = 0

        self.surf = self.walk1 # Starting surface to override later
        self.rect = self.surf.get_rect(bottomleft = (x, y)) # Rectangle to blit in draw

        self.gravity = 0
        if self.y < 300:
            self.gravity += 1
            self.y += self.gravity
        else:
            self.y = 300

    #def update():

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def jump(self):
        self.gravity = -20
        self.y = 299
        if self.y < 300:
            self.surf = self.jumps
        print(self.gravity)

    def animate(self):
        self.walk_index += 0.1
        if int(self.walk_index) == 2: self.walk_index = 0
        self.surf = self.walk[int(self.walk_index)]
        
    pygame.display.update()
    clock.tick(60)
    #def collide():