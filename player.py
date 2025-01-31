import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    def __init__(self, x=100, y=FLOOR):
        super().__init__()
        self.position = [x, y]

        # Assigning all the images including two for a walk animation
        self.walk1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        self.walk2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.jumps = pygame.image.load("graphics/Player/jump.png").convert_alpha()
        self.stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        self.hitbox = False
        
        # Setting the two frames of walk animation as a list
        self.walk = [self.walk1, self.walk2]
        
        # creating a number to increment so the walk animations will cycle (might relocate later)
        self.walk_index = 0

        self.surf = self.walk1 # Starting surface to override later
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(bottomleft = (self.position)) # Rectangle to blit in draw

        self.gravity = 0
        self.moving_left = False
        self.moving_right = False
    
    def jump(self):
        self.gravity = -20

    def move_left(self):
        if self.position[0] > 0:
            self.position[0] -= 4
            self.moving_left = True
        else:
            self.moving_left = False

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.position[0] += 4
            self.walk_index += 0.2
            self.moving_right = True
        else:
            self.moving_right = False

    def animate(self):
        self.walk_index += 0.1
        self.gravity += 1
        self.position[1] += self.gravity
        if self.position[1] > FLOOR: self.position[1] = FLOOR # Makes the lowest fall height
        if int(self.walk_index) == 2: self.walk_index = 0 
        if self.position[1] < FLOOR:
            self.surf = self.jumps # If airborne plays the jump image
        elif self.position[0] == 0:
            self.surf = self.walk[int(self.walk_index)]
        elif self.moving_left: self.surf = self.stand
        else: self.surf = self.walk[int(self.walk_index)]
        self.rect.bottomleft = self.position
    
    def draw_hitbox(self):
        if self.hitbox: self.hitbox = False
        else: self.hitbox = True

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        if self.hitbox: pygame.draw.rect(screen,"Red", self.rect, 2)
        
    pygame.display.update()
    clock.tick(60)


