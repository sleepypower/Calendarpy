"""

"""

import pygame
import initialize
import time
import globals
import classBlock

# initialize game engine
pygame.init()

# Font
pygame.font.init()


clock_tick_rate = 60

# Set title to the window
pygame.display.set_caption("CALENDARPY")

clock = pygame.time.Clock()
BACKGROUND_IMAGE = pygame.image.load("background_image.jpg")
BACKGROUND_IMAGE = pygame.transform.smoothscale(
    BACKGROUND_IMAGE, (globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))

running = True


#clase1 = classBlock.ClassBlock("matematicas", 1, 2, )
calendario = classBlock.Calendar()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    globals.BACKGROUND_SCREEN.blit(BACKGROUND_IMAGE, [0, 0])
    #clase1.render()
    calendario.render()
    pygame.display.flip()
    clock.tick(clock_tick_rate)

pygame.quit()
