import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Enemy():
    def __init__(self, x, y):
        self.position = [x, y]
        self.surf = ""
        self.rect = ""


    def draw(self, screen):
        screen.blit(self.surf, self.rect)


class Snail(Enemy):
    def __init__(self, x, y=FLOOR):
        super().__init__(x, y)
        self.glide1 = pygame.image.load("graphics/snail/snail1.png")
        self.glide2 = pygame.image.load("graphics/snail/snail2.png")

        self.mask1 = pygame.mask.from_surface(self.glide1)
        self.mask2 = pygame.mask.from_surface(self.glide2)

        self.glide = [self.glide1, self.glide2]
        self.masks = [self.mask1, self.mask2]
        self.glide_index = 0
        
        self.surf = self.glide1
        self.rect = self.surf.get_rect(bottomleft = (self.position))

    def animate(self):
        self.glide_index += 0.05
        if int(self.glide_index) == 2: self.glide_index = 0
        self.surf = self.glide[int(self.glide_index)]
        self.mask = self.masks[int(self.glide_index)]


class Fly(Enemy):
    def __init__(self, x, y=100):
        super().__init__(x, y)
        self.fly1 = pygame.image.load("graphics/Fly/Fly1.png")
        self.fly2 = pygame.image.load("graphics/Fly/Fly2.png")

        self.mask1 = pygame.mask.from_surface(self.fly1)
        self.mask2 = pygame.mask.from_surface(self.fly2)

        self.fly = [self.fly1, self.fly2]
        self.masks = [self.mask1, self.mask2]
        self.fly_index = 0
        
        self.surf = self.fly1
        self.rect = self.surf.get_rect(bottomleft = (self.position))

    def animate(self):
        self.fly_index += 0.1
        if int(self.fly_index) == 2: self.fly_index = 0 
        self.surf = self.fly[int(self.fly_index)]
