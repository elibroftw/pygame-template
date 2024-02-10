from ui_kit import *
from pygame import KEYDOWN, K_F4, K_LALT, K_RALT, K_ESCAPE, K_q, QUIT, K_SPACE, K_v, K_h, MOUSEBUTTONDOWN
import sys
import pygame.display

pygame.display.

class Button:
    def __init__(self, text, key=None):
        self.text = text
        self.key = key

class Menu:
    layout = []
    # TODO: maybe just use properties of pygame.display

    def __init__(self, surface, w_width, w_height,
                 src_font_light, sec_font_bold, layout=None):
        if layout is not None:
            self.layout = layout
        self.surface = surface
        self.w_width = w_width
        self.w_height = w_height

        self.MENU_FONT = pygame.font.Font(src_font_light, int(110 / 1080 * w_height))
        self.SMALL_TEXT = pygame.font.Font(sec_font_bold, int(25 / 1440 * self.SCREEN_HEIGHT))

        self.BUTTON_WIDTH = int(self.SCREEN_WIDTH * 0.625 // 3)  # important
        self.BUTTON_HEIGHT = int(self.SCREEN_HEIGHT * 5 // 81)
        self.TOGGLE_WIDTH = int(self.BUTTON_WIDTH * 0.875)
        self.TOGGLE_ADJ = int(self.BUTTON_WIDTH * 0.075)


    def add_row(self, items):
        self.layout.append(items)

    def add_item(self, item):
        self.layout.append([item])

    def add_btn(self, btn=None, text=None, key=None):
        if btn is None:
            assert text is not None
            self.buttons.append(Button(text, key))
        else:
            self.buttons.append(btn)

    def show(self, clock):
        self.main_menu_setup()
        while True:
            click = False
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                alt_f4 = (event.type == KEYDOWN and (event.key == K_F4
                        and (pressed_keys[K_LALT] or pressed_keys[K_RALT])
                        or event.key == K_q or event.key == K_ESCAPE))
                if event.type == QUIT or alt_f4: sys.exit()
                elif event.type == KEYDOWN and event.key == K_SPACE: start_game = True
                elif event.type == KEYDOWN and (event.key == K_v or event.key == K_h): view_hs = True
                elif event.type == MOUSEBUTTONDOWN: click = True
            for btn in self.buttons:
                if button(btn.text, *s().button_layout_4[0], click):
                    return btn.text if btn.key is None else btn.key
            for i, row in self.layout:
                button_x_start = (self.w_width - self.button_width) // 2
                # self.button_x_start, self.SCREEN_HEIGHT * i // 13, self.BUTTON_WIDTH, self.BUTTON_HEIGHT
                pass
            pygame.display.update(s().button_layout_4)
            clock.tick(60)



def show(clock):
    start_game = view_hs = False
"""
if button('START GAME', *s().button_layout_4[0], click): start_game = True
elif button('VIEW HIGHSCORES', *s().button_layout_4[1], click) or view_hs:
    # view_high_scores()
    view_hs = False
    main_menu_setup()
elif button('SETTINGS', *s().button_layout_4[2], click):
    # settings_menu()
    main_menu_setup()
elif button('QUIT GAME', *s().button_layout_4[3], click):
    sys.exit()
if start_game:
    while start_game: start_game = game() == 'Restart'
    main_menu_setup()
"""
