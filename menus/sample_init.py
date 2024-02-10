from menus import main_menu
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

# ICON = 'b64String'
# ICON = pygame.image.load(io.BytesIO(base64.b64decode(ICON)))
# pygame.display.set_icon(ICON)
pygame.display.set_caption('Game Name')
clock = pygame.time.Clock()
ticks = 0

def start_game():
    # def __init__(self, game_name, version, authors):
    main_menu = main_menu.MainMenu('Game Name', 'v0.0.1', 'Author')
    
    main_menu.show()

start_game()
