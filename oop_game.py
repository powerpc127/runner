import pygame
from constants import *
from random import *
import sys
from player import Player

# Remaking the old code with OOP and tidying up the code tremendously

pygame.init()

player = Player(100, 100)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game_active = False

while True:
    screen.fill((0, 0, 0))
    player.animate()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.jump()


    player.draw(screen)

    pygame.display.update()
    clock.tick(60)
