import pygame
from constants import *
from fonts import *
from player import Player
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()

class Background():
    def __init__(self):
        self.sky_surf = pygame.image.load("graphics/Sky.png")
        self.ground_surf = pygame.image.load("graphics/ground.png")
        self.sky_rect = self.sky_surf.get_rect(topleft = (0, 0))
        self.ground_rect = self.ground_surf.get_rect(bottomleft = (0, SCREEN_HEIGHT))

    def draw(self, screen):
        screen.blit(self.sky_surf, self.sky_rect)
        screen.blit(self.ground_surf, self.ground_rect)

class GameOver():
    def __init__(self):
        self.game_over_surf = header_font.render("Game Over", False, (0, 200, 200))
        self.game_over_rect = self.game_over_surf.get_rect(center = ((.5 * SCREEN_WIDTH), ((1/4)*SCREEN_HEIGHT)))
        
        self.player_surf = pygame.transform.rotozoom(player.stand, 0,2)
        self.player_rect = self.player_surf.get_rect(center = (400, ((1/2) * SCREEN_HEIGHT)))

        self.try_again_surf = small_font.render("Press return to try again!", False, (0, 200, 200))
        self.try_again_rect = self.try_again_surf.get_rect(center = ((0.5*SCREEN_WIDTH),((3/4)*SCREEN_HEIGHT)))
