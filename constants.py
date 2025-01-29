from PIL import Image

floor = Image.open("graphics/ground.png")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = (floor.height + 300)

FLOOR = (SCREEN_HEIGHT - floor.height)

