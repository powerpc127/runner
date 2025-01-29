import pygame
from constants import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Background():
    def __init__(self):
        self.sky_surf = pygame.image.load("graphics/Sky.png")
        self.ground_surf = pygame.image.load("graphics/ground.png")
        self.sky_rect = self.sky_surf.get_rect(topleft = (0, 0))
        self.ground_rect = self.ground_surf.get_rect(bottomleft = (0, SCREEN_HEIGHT))

    def draw(self, screen):
        screen.blit(self.sky_surf, self.sky_rect)
        screen.blit(self.ground_surf, self.ground_rect)
