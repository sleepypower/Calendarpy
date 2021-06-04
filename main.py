"""

"""

import pygame
import initialize
import time

pygame.init() #preparar el módulo de juego
clock = pygame.time.Clock()

#Crear la superficie y ventana que la contiene
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1200
SCREEN_COLOR = (40, 40, 40)

SCREEN = initialize.set_pygame_and_screen(SCREEN_HEIGHT, SCREEN_WIDTH)

last_move = pygame.time.get_ticks()

frame = 0

while True:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pass
        
    SCREEN.fill(SCREEN_COLOR)


    pygame.display.flip()
    clock.tick(1)