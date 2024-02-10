# imports
import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
from pygame import gfxdraw, K_w, K_a, K_d, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_F4, K_p, K_RALT, K_LALT, K_SPACE, MOUSEBUTTONDOWN, QUIT, KEYUP, KEYDOWN, K_TAB, K_v, K_h, K_BACKSPACE, K_q, K_m, K_r
import pygame
from constants import *
# UI CONSTANTS
from ui_kit import text_objects, button, draw_circle, toggle_btn, show_mouse, hide_mouse
import sys
from state_manager import s

# + game related constants





def game():
    # Game Logic (get back to this later)
    pass


# Initialization
if platform.system() == 'Windows':
    from ctypes import windll
    windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center display
pygame.init()


# ICON = 'b64String'
# ICON = pygame.image.load(io.BytesIO(base64.b64decode(ICON)))
# pygame.display.set_icon(ICON)
pygame.display.set_caption('Game Name')
clock = pygame.time.Clock()
ticks = 0
main_menu()
