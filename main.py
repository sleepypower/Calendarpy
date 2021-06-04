"""

"""

import pygame
import initialize
import time
import globals


# initialize game engine
pygame.init()


clock_tick_rate = 60

# Open a window

BACKGROUND_SCREEN = initialize.set_pygame_and_screen(
    globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH)

# Set title to the window
pygame.display.set_caption("CALENDARPY")

clock = pygame.time.Clock()
BACKGROUND_IMAGE = pygame.image.load("background_image.jpg")
BACKGROUND_IMAGE = pygame.transform.smoothscale(
    BACKGROUND_IMAGE, (globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))

running = True
calendar_surface_size = (int(globals.SCREEN_HEIGHT * 0.85),
                         int(globals.SCREEN_WIDTH * 0.85))
s = pygame.Surface(calendar_surface_size)
s.set_alpha(128)                # alpha level
s.fill((255, 255, 255))           # this fills the entire surface

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    BACKGROUND_SCREEN.blit(BACKGROUND_IMAGE, [0, 0])
    BACKGROUND_SCREEN.blit(
        s, ((globals.SCREEN_HEIGHT - calendar_surface_size[0])/2, (globals.SCREEN_WIDTH - calendar_surface_size[1])/2))
    pygame.display.flip()
    clock.tick(clock_tick_rate)

pygame.quit()
