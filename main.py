import pygame
from constants import *
from sys import exit
from random import randint

def display_time(): # A function to measure the length of time the player has been alive. We call this later to make it visible
    current_time = pygame.time.get_ticks() - start_time # Sets the time. Start_time is defined below as the time since I ran the code
    time_seconds = float(current_time/1000) # Converts milliseconds to seconds
    time_surf = test_font.render(f"{time_seconds:.2f}", False, (64 ,64 ,64)) # Makes a surface for the timer
    time_rect = time_surf.get_rect(center = (400,100)) # Applies it^ to a rectangle centered horizontally
    screen.blit(time_surf, time_rect) # Prints to the screen
    return time_seconds

def obstacle_movement(obstacle_list):
    global score
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)
            if obstacle_rect.bottom == 210: screen.blit(fly_surf, obstacle_rect)
            if obstacle_rect.x <= -72:
                del obstacle_list[0]
                score += 1
        return obstacle_list
    else:
        return []

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump # Jump conditions
    else:
        player_index += 0.1
        if int(player_index) >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

    #play walking animation if player on floor
    #display jump surface when player not on floor

pygame.init() # Necessary to initialize pygame and the code will not work without it

# Have to create a display surface, the window the player sees. Stored as variable, usually screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets the size of the window the game runs in
clock = pygame.time.Clock() # Creates a clock instance which allows us to control framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # To write text we need a font. This selects a font and size
small_font = pygame.font.Font("font/Pixeltype.ttf", 30) # The same font but smaller, used in game over screen

game_active = False # This determines if the game is running or there's a game over
score = 0 # Sets the starting score. Needs to be done before making score_surf so the value is defined for the f string
start_time = 0
time = 0 # Both of these ^ reset the timer for restarting the game 
obstacle_rect_list = []

# active surfaces
background_surf = pygame.image.load('graphics/Sky.png').convert() # Used to load the backround .png image
ground_surf = pygame.image.load('graphics/ground.png').convert() # Same method loads the ground texture
text_surf = test_font.render('Jump the Snail', False, 'Green') # Generates text:('text', anti-aliasing bool, color)
text_rect = text_surf.get_rect(center = (400, 50)) # Appiles the text to a rectangle for easy positioning

# inactive surfaces
game_over_surf_1 = test_font.render("Game Over", False, (0, 200, 200)) # Sets text for a game over
game_over_rect_1 = game_over_surf_1.get_rect(center = (400, 100)) # Applies a rectangle that's centered vertically
game_over_surf_2 = small_font.render("Press Space to Try Again", False, (0, 200, 200))
game_over_rect_2 = game_over_surf_2.get_rect(center = (400, 300))
new_game_surf_1 = test_font.render("Welcome to Jump the Snail", False, (0, 200, 200)) # Sets text for a game over
new_game_rect_1 = game_over_surf_1.get_rect(midleft = (210, 100)) # Applies a rectangle that's centered vertically
new_game_surf_2 = small_font.render("Press Space to Start", False, (0, 200, 200))
new_game_rect_2 = game_over_surf_2.get_rect(midleft = (305, 300))

# Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # .convert() and .convert_alpha() are both used to improve performance
# .converrt_alpha() removes the checkered pattern behind an image. Sky and ground don't have that, so no alpha.
fly_surf = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()

# player images
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha() # This and ^that line represent a walking animation
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300)) # Draws the player rectangle on the floor (300 px)
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_index = 0
player_gravity = 0 # This will be overwritten later
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0,2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# timer
obstacle_timer = pygame.USEREVENT + 1 # Userevent is a self defined event. However pygame uses userevent[0]
# for its own mechanics. Therefore we set obstacle_timer to userevent+1
pygame.time.set_timer(obstacle_timer, 1500) # Defining the event to make something operate a timer

# Use a while True  loop to keep the game running, otherwise the game will close as soon as you open the program

while True:
    # Allow for the game to quit
    for event in pygame.event.get(): # get function automatically detects input
        if event.type == pygame.QUIT:
            pygame.quit() # If you press the close button, the game will successfully close down
            exit() # Runs sys.exit() to prevent the game logic from continuing to try to run
        
    # Input (still in while loop)   
        if game_active: 
            if event.type == pygame.KEYDOWN: # Detects if button is pressed. Full button list here: https://www.pygame.org/docs/ref/key.html#key-constants-label
                if event.key == pygame.K_UP and player_rect.bottom >= 300: # Detects if up arrow is pressed and if we are on the ground
                    player_gravity = -20
                    player_rect.y -= 1 # This changes our height by 1 so that we don't meet the criteria for being on the floor and can move
            
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))

        else: # Cancels out the 'if game_active' line above to account for a game over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Detects if a key is pressed and if it's space
                score = 0 # Resets the score counter
                game_active = True # Restarts the game
                start_time = pygame.time.get_ticks()



# Here we draw all our elements and update everything in an if statement
    if game_active:
        # screen.blit ('block image transfer') publishes a regular surface onto the display surface (see below)
        screen.blit(background_surf,(0, 0)) # Used 'identify' in the cli to find the size of the image
        screen.blit(ground_surf, (0, 300)) # Set the ground surface height to the end of the Sky image
        # Order here matters. Background surfaces first, foreground surfaces last
        time = f"{display_time():.2f}" # Stores the maximum value of time as a variable to call on the game over screen
        
        pygame.draw.rect(screen, 'Yellow', text_rect) # This highlights the text by displaying a rectangle behind it
        # ^Inputs are (surface to print on, color, position)
        screen.blit(text_surf, (text_rect)) # Prints the text using the loaded font
        
        display_time() # Prints a timer to the screen

        #player
        player_rect.y += player_gravity # The player will move down by their current gravity value of pixels...
        player_gravity += 1 # ... and the value of gravity is increased. This is a basic approximation of physics (no terminal velocity).
        if player_rect.bottom >= 300: # If the player hits the ground too hard and goes below the floor...
            player_rect.bottom = 300 # ... then their y position is reset to 300. This creates a floor of 300 px.
        player_animation() # Runs the logic that determines what player_surf below will be
        screen.blit(player_surf, (player_rect)) # When creating a rect you can define the initial position in the rect
        score_surf = small_font.render(f"Score: {score}", False, "Black")
        score_rect = score_surf.get_rect(left = 650, top = 25)
        screen.blit(score_surf, score_rect)

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

# To learn about mouse clicking, visit https://youtu.be/AY9MnQ4x3zk?si=0HqP7H9ExS0Q9Gjy&t=3998, also @ 1:42:00

        # collision
        for obstacle_rect in obstacle_rect_list:
            if player_rect.colliderect(obstacle_rect):
                obstacle_rect_list = []   
                game_active = False

    else: # Sets the game over conditions
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        if time != 0:
            screen.blit(game_over_surf_1, game_over_rect_1)
            screen.blit(game_over_surf_2, game_over_rect_2)
            game_over_score_surf = test_font.render(f"Score: {score}", False, (0, 200, 200))
            game_over_score_rect = game_over_score_surf.get_rect(midleft = (100, 133))
            game_over_time_surf = test_font.render(f"Time: {time}", False, (0, 200, 200))
            game_over_time_rect = game_over_time_surf.get_rect(midright = (700, 133))
            screen.blit(game_over_score_surf, game_over_score_rect)
            screen.blit(game_over_time_surf, game_over_time_rect)
        else:
            screen.blit(new_game_surf_1, new_game_rect_1)
            screen.blit(new_game_surf_2, new_game_rect_2)
        
    pygame.display.update() # updates the the screen display surface. Call it and forget about it
    clock.tick(60) # Sets the *maximum* framerate to 60 fps
   

# Displaying images:
    # Display surface: The game window itself. Window and background.
    # Regular surface: Essentially an image (imported sprite, plain color, or rendered text). Any number can be rendered
# The display surface is your canvas, the regular surfaces are images that you apply to the canvas to create art
# Regular surfaces must be drawn to the canvas to be shown, otherwise they are like a benched player



