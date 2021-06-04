"""

"""

import pygame
import initialize
import time


# initialize game engine
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1200

clock_tick_rate = 20

# Open a window

screen = initialize.set_pygame_and_screen(SCREEN_HEIGHT, SCREEN_WIDTH)

# Set title to the window
pygame.display.set_caption("CALENDARPY")

clock = pygame.time.Clock()
BACKGROUND_IMAGE = pygame.image.load("background_image.jpg")
BACKGROUND_IMAGE = pygame.transform.smoothscale(
    BACKGROUND_IMAGE, (SCREEN_HEIGHT, SCREEN_WIDTH))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(BACKGROUND_IMAGE, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)

pygame.quit()
