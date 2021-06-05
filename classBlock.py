import pygame
import globals

pygame.font.init()


class Calendar:

    def __init__(self) -> None:
        # Board surface
        self.surface_board_width = int(globals.SCREEN_WIDTH * 0.9)
        self.surface_board_height = int(globals.SCREEN_HEIGHT * 0.9)
        self.surface_board = pygame.Surface(
            (self.surface_board_width, self.surface_board_height))
        self.surface_board.set_alpha(128)

        # Schedule
        self.calendar_array = [[] for i in range(7)]

    def render(self):
        # for i in range(7):
        #     pygame.draw.rect(self.surface_board, (255, 255, 255), pygame.Rect(
        #         i * (self.surface_board_width / 7), 30, (self.surface_board_width / 7) - 100, 600))

        # Paint 
        globals.BACKGROUND_SCREEN.blit(self.surface_board, ((
            (globals.SCREEN_WIDTH - self.surface_board_width)/2), (globals.SCREEN_HEIGHT - self.surface_board_height)/2))
        self.surface_board.fill((100, 100, 100))

        


class ClassBlock:

    def __init__(self, class_name: str, starting_time: int, ending_time: int, surface) -> None:
        # Attributes
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.delta_time = ending_time - starting_time
        self.surface = surface

    def render(self,  day_index):
        s = pygame.Surface(globals.CALENDAR_SURFACE_SIZE)

        pygame.draw.rect(self.surface, (0, 0, 0),
                         pygame.Rect(30, 30, 600, 600))
