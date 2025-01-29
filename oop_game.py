import pygame, random, sys
from constants import *
from player import Player
from surfaces import Background

# Remaking the old code with OOP and tidying up the code tremendously

pygame.init()

player = Player()
background = Background()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game_active = False

while True:
    screen.fill((0, 0, 0))
    background.draw(screen)
    player.animate()
    player.draw(screen)
    keys = pygame.key.get_pressed()
    print(player.moving_left)
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN: # Checking for KEYDOWN avoids double jumping
            if event.key == pygame.K_UP and player.position[1] == FLOOR:
                player.jump()        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False    
    
    

    

    pygame.display.update()
    clock.tick(60)
