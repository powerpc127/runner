import pygame, random, sys
from constants import *
from player import Player
from surfaces import Background
from enemies import Snail, Fly

# Remaking the old code with OOP and tidying up the code tremendously

pygame.init()

player = Player()
snail = Snail(500,)
fly = Fly(300, 250)
background = Background()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game_active = True
enemies = [snail, fly]

def detect_collision(enemy):
    global game_active
    if pygame.sprite.collide_mask(player, enemy) != None:
        print("Ending!")
        game_active = False



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if game_active:
        print("Active")
        screen.fill((0, 0, 0))
        background.draw(screen)
        player.animate()
        for enemy in enemies:
            enemy.animate()
            enemy.draw(screen)
        player.draw(screen)
        
        # Collisions
        for enemy in enemies:
            detect_collision(enemy)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        
            if event.type == pygame.KEYDOWN: # Checking for KEYDOWN avoids double jumping
                if event.key == pygame.K_UP and player.position[1] == FLOOR:
                    player.jump()        
                if event.key == pygame.K_q:
                    player.draw_hitbox()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.moving_left = False
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False   
    else:
        screen.fill((0, 0, 0))
    pygame.display.update()
    clock.tick(60)
