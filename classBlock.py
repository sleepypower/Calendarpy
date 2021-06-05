import pygame
import globals

pygame.font.init()


class Calendar:

    def __init__(self) -> None:
        pass

class ClassBlock:

    def __init__(self, class_name: str, starting_time: int, ending_time: int) -> None:
        delta_time = ending_time - starting_time
        s = pygame.Surface((globals.CALENDAR_SURFACE_SIZE,
                            globals.CALENDAR_SURFACE_SIZE))
        s.set_alpha(128)
        s.fill((255, 255, 255))

    