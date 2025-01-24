import pygame
from constants import *
from sys import exit

pygame.init() # Necessary to initialize pygame and the code will not work without it

# Have to create a display surface, the window the player sees. Stored as variable, usually screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets the size of the window the game runs in
clock = pygame.time.Clock() # Creates a clock instance which allows us to control framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # To write text we need a font. This selects a font and size
# Use a while True  loop to keep the game running, otherwise the game will close as soon as you open the program

background_surface = pygame.image.load('graphics/Sky.png') # Used to load the backround .png image
ground_surface = pygame.image.load('graphics/ground.png') # Same method loads the ground texture
text_surface = test_font.render('My game', False, 'Green') # Generates text:('text', anti-aliasing bool, color)

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

while True:
    # Allow for the game to quit
    for event in pygame.event.get(): # get function automatically detects input
        if event.type == pygame.QUIT:
            pygame.quit() # If you press the close button, the game will successfully close down
            exit() # Runs sys.exit() to prevent the game logic from continuing to try to run

    # screen.blit ('block image transfer') publishes a regular surface onto the display surface (see below)
    screen.blit(background_surface,(0, 0)) # Used 'identify' in the cli to find the size of the image
    screen.blit(ground_surface, (0, 300)) # Set the ground surface height to the end of the Sky image
    # Order here matters. Big surfaces first, small surfaces last
    screen.blit(text_surface, (300, 50)) # Prints the text using the loaded font
    
    snail_x_pos -= 4
    screen.blit(snail_surface, (snail_x_pos, 264))
    if snail_x_pos < -72:
        snail_x_pos = 800

    # Here we draw all our elements and update everything
    pygame.display.update() # updates the the screen display surface. Call it and forget about it
    clock.tick(60) # Sets the *maximum* framerate to 60 fps

# Displaying images:
    # Display surface: The game window itself. Window and background.
    # Regular surface: Essentially an image (imported sprite, plain color, or rendered text). Any number can be rendered
# The display surface is your canvas, the regular surfaces are images that you apply to the canvas to create art
# Regular surfaces must be drawn to the canvas to be shown, otherwise they are like a benched player



