import pygame
import constants
from sys import exit

pygame.init() # Necessary to initialize pygame and the code will not work without it

# Have to create a display surface, the window the player sees. Stored as variable, usually screen

screen = pygame.display.set_mode((800, 400)) # Sets the size of the window the game runs in
clock = pygame.time.Clock() # Creates a clock instance which allows us to control framerate
# Use a while True  loop to keep the game running, otherwise the game will close as soon as you open the program

test_surface = pygame.Surface((100, 200))
test_surface.fill("Red") 

while True:
    # Allow for the game to quit
    for event in pygame.event.get(): # get function automatically detects input
        if event.type == pygame.QUIT:
            pygame.quit() # If you press the close button, the game will successfully close down
            exit() # Runs sys.exit() to prevent the game logic from continuing to try to run

    # screen.blit ('block image transfer') publishes a regular surface onto the display surface (see below)
    screen.blit(test_surface,(350, 100))

    # Here we draw all our elements and update everything
    pygame.display.update() # updates the the screen display surface. Call it and forget about it
    clock.tick(60) # Sets the *maximum* framerate to 60 fps

# Displaying images:
    # Display surface: The game window itself. Window and background.
    # Regular surface: Essentially an image (imported sprite, plain color, or rendered text). Any number can be rendered
# The display surface is your canvas, the regular surfaces are images that you apply to the canvas to create art
# Regular surfaces must be drawn to the canvas to be shown, otherwise they are like a benched player



