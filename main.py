import pygame
from constants import *
from sys import exit

pygame.init() # Necessary to initialize pygame and the code will not work without it

# Have to create a display surface, the window the player sees. Stored as variable, usually screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets the size of the window the game runs in
clock = pygame.time.Clock() # Creates a clock instance which allows us to control framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # To write text we need a font. This selects a font and size
# Use a while True  loop to keep the game running, otherwise the game will close as soon as you open the program

background_surface = pygame.image.load('graphics/Sky.png').convert() # Used to load the backround .png image
ground_surface = pygame.image.load('graphics/ground.png').convert() # Same method loads the ground texture

text_surface = test_font.render('My game', False, 'Green') # Generates text:('text', anti-aliasing bool, color)
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # .convert() and .convert_alpha() are both used to improve performance
# .converrt_alpha() removes the checkered pattern behind an image. Sky and ground don't have that, so no alpha.
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300)) # Draws the player rectangle on the floor (300 px)
player_gravity = 0 # This will be overwritten later

while True:
    # Allow for the game to quit
    for event in pygame.event.get(): # get function automatically detects input
        if event.type == pygame.QUIT:
            pygame.quit() # If you press the close button, the game will successfully close down
            exit() # Runs sys.exit() to prevent the game logic from continuing to try to run
        
    # Input (still in while loop)    
        if event.type == pygame.KEYDOWN: # Detects if button is pressed
            if event.key == pygame.K_UP: # Detects if up arrow is pressed. Full button list here: https://www.pygame.org/docs/ref/key.html#key-constants-label
                player_gravity = -15
                player_rect.y -= 1


# Here we draw all our elements and update everything

    # screen.blit ('block image transfer') publishes a regular surface onto the display surface (see below)
    screen.blit(background_surface,(0, 0)) # Used 'identify' in the cli to find the size of the image
    screen.blit(ground_surface, (0, 300)) # Set the ground surface height to the end of the Sky image
    # Order here matters. Background surfaces first, foreground surfaces last
    pygame.draw.rect(screen, 'Pink', text_rect) # This highlights the text by displaying a rectangle behind it
    # ^Inputs are (surface to print on, color, position)
    screen.blit(text_surface, (text_rect)) # Prints the text using the loaded font
    
    snail_rect.x -= 4 # Moves the snail image to the left by 4 pixels each frame
    if snail_rect.right <= 0: snail_rect.left = 800 # If the right side of the snail leaves the screen, redraw it @ 800px
    screen.blit(snail_surface, (snail_rect)) # Draws the snail over the snail_rect whose position is dictated above
    
    #player
    if player_rect.bottom > 300: # If the player hits the ground too hard and goes below the floor...
        player_rect.bottom = 300 # ... then their y position is reset to 300. This creates a floor of 300 px.
    if player_rect.bottom < 300: # If the player is above the ground...
        player_rect.y += player_gravity # ... they move down by their current gravity value of pixels...
        player_gravity += 1 # ... and the value of gravity is increased. This is a basic approximation of physics (no terminal velocity).
    screen.blit(player_surface, (player_rect)) # When creating a rect you can define the initial position in the rect 


# To learn about mouse clicking, visit https://youtu.be/AY9MnQ4x3zk?si=0HqP7H9ExS0Q9Gjy&t=3998
    if player_rect.colliderect(snail_rect):
        print('collision')

    # keys = pygame.key.get_pressed()

    pygame.display.update() # updates the the screen display surface. Call it and forget about it
    clock.tick(60) # Sets the *maximum* framerate to 60 fps

# Displaying images:
    # Display surface: The game window itself. Window and background.
    # Regular surface: Essentially an image (imported sprite, plain color, or rendered text). Any number can be rendered
# The display surface is your canvas, the regular surfaces are images that you apply to the canvas to create art
# Regular surfaces must be drawn to the canvas to be shown, otherwise they are like a benched player



