import os
import platform
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'
import pygame

# Initialization
if platform.system() == 'Windows':
    from ctypes import windll
    windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # center display
pygame.init()
