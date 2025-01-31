import pygame, random, sys
from constants import *
from player import Player
from backgrounds import *
from fonts import *
from enemies import Snail, Fly

# Remaking the old code with OOP and tidying up the code tremendously

pygame.init()

# Basic parameters
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player()
snail = Snail(500,)
fly = Fly(300, 250)
background = Background()
game_active = True
end = GameOver()
time = 0
enemies = [snail, fly]

# Functions
def detect_collision(enemy):
    global game_active
    if pygame.sprite.collide_mask(player, enemy) != None:
        game_active = False
    

def start_screen(): # Delete this
    pass

# Logic loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if game_active:
        # Drawing everything on screen
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
        
        # Movement keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        
        if event.type == pygame.KEYDOWN: # Checking for KEYDOWN avoids double jumping
            if event.key == pygame.K_UP and player.position[1] == FLOOR:
                player.jump()       

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_RIGHT:
                player.moving_right = False   

    else:
        screen.fill((94,129,162))
        screen.blit(end.game_over_surf, end.game_over_rect)
        screen.blit(end.player_surf, end.player_rect)
        screen.blit(end.try_again_surf,end.try_again_rect)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            player.position = [100, FLOOR]
            game_active = True
    pygame.display.update()
    clock.tick(60)
 