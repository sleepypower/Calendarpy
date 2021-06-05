"""
This program initializes the screen
"""

import pygame

def set_pygame_and_screen(ScreenWidth = 600, ScreenHeight = 600):
    """
    Sets the screen
    """

    #SCREEN setup
    SCREEN_COLOR = (40, 40, 40)

    SCREEN = pygame.display.set_mode((ScreenWidth, ScreenHeight)) #Create Screen
    SCREEN.fill(SCREEN_COLOR)
    return SCREEN
