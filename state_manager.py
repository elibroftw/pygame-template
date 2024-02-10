import pygame
from constants import *
from functools import lru_cache


# do not initialize manually, use get_state instead!
class State:
    def __init__(self):
        # TODO: use __slots__
        self.SCREEN_WIDTH = int(pygame.display.Info().current_w)
        self.SCREEN_HEIGHT = int(pygame.display.Info().current_h)
        if FULLSCREEN:
            self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT = int(0.75 * self.SCREEN_WIDTH), int(0.75 * self.SCREEN_HEIGHT)
            self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.BUTTON_WIDTH = int(self.SCREEN_WIDTH * 0.625 // 3)  # important
        self.BUTTON_HEIGHT = int(self.SCREEN_HEIGHT * 5 // 81)
        self.TOGGLE_WIDTH = int(self.BUTTON_WIDTH * 0.875)
        self.TOGGLE_ADJ = int(self.BUTTON_WIDTH * 0.075)
        self.SMALL_TEXT = pygame.font.Font(FONT_BOLD, int(25 / 1440 * self.SCREEN_HEIGHT))

        self.LARGE_TEXT = pygame.font.Font(FONT_REG, int(40 / 1080 * self.SCREEN_HEIGHT))
        self.MEDIUM_TEXT = pygame.font.Font(FONT_LIGHT, int(35 / 1440 * self.SCREEN_HEIGHT))
        # client defined run time constants
        self.HUD_TEXT = pygame.font.Font(FONT_REG, int(40 / 1440 * self.SCREEN_HEIGHT))
        self.SCORE_ANCHOR = self.SCREEN_WIDTH - 8, -5
        self.button_x_start = (self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2
        self.button_layout_4 = [(self.button_x_start, self.SCREEN_HEIGHT * i // 13, self.BUTTON_WIDTH, self.BUTTON_HEIGHT) for i in range(5, 9)]


@lru_cache(1)
def get_state():
    return State()


def s():
    return get_state()
