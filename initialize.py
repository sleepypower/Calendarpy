"""
This program initializes the screen
"""

import pygame

def set_pygame_and_screen(ScreenHeight = 600, ScreenWidth = 600):
    """
    Sets the screen
    """

    #SCREEN setup
    SCREEN_COLOR = (40, 40, 40)

    SCREEN = pygame.display.set_mode((ScreenHeight, ScreenWidth)) #Create Screen
    SCREEN.fill(SCREEN_COLOR)
    return SCREEN
