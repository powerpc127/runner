import pygame
from constants import *
from random import randint

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = [x, y]
        self.surf = ""
        self.rect = ""
        self.mask = ""
        self.index = 0
        self.jumped = False


class Snail(Enemy):
    def __init__(self, x=(SCREEN_WIDTH + randint(1, 100)), y=FLOOR):
        super().__init__(x, y)
        self.glide1 = pygame.image.load("graphics/snail/snail1.png")
        self.glide2 = pygame.image.load("graphics/snail/snail2.png")

        self.glide = [self.glide1, self.glide2]
        
        self.surf = self.glide1
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(bottomleft = (self.position))

    def animate(self):
        self.index += 0.05
        if int(self.index) == 2: self.index = 0
        self.surf = self.glide[int(self.index)]

    def draw(self, screen):
            screen.blit(self.surf, self.rect)

class Fly(Enemy):
    def __init__(self, x=(SCREEN_WIDTH + randint(1, 100)), y=250):
        super().__init__(x, y)
        self.fly1 = pygame.image.load("graphics/Fly/Fly1.png")
        self.fly2 = pygame.image.load("graphics/Fly/Fly2.png")

        self.fly = [self.fly1, self.fly2]
        
        self.surf = self.fly1
        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(bottomleft = (self.position))

    def animate(self):
        self.index += 0.1
        if int(self.index) == 2: self.index = 0 
        self.surf = self.fly[int(self.index)]
    
    def draw(self, screen):
        screen.blit(self.surf, self.rect)
