from ui_kit import *
from pygame import KEYDOWN, K_F4, K_LALT, K_RALT, K_ESCAPE, K_q, QUIT, K_SPACE, K_v, K_h, MOUSEBUTTONDOWN
import sys

class Button:
    def __init__(self, text, key=None):
        self.text = text
        self.key = key

class MainMenu:
    buttons = []

    def main_menu_setup(self):
        show_mouse()
        s().SCREEN.fill(WHITE)
        text_surf, text_rect = text_objects(self.game_name, s().MENU_TEXT)
        text_rect.center = (int(s().SCREEN_WIDTH / 2), int(s().SCREEN_HEIGHT / 4))
        s().SCREEN.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects(f'v{self.version}', s().SMALL_TEXT)
        text_rect.center = (int(s().SCREEN_WIDTH * 0.98), int(s().SCREEN_HEIGHT * 0.98))
        s().SCREEN.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects(f'Created by {self.authors}', s().LARGE_TEXT)
        text_rect.center = (int(s().SCREEN_WIDTH / 2), int(s().SCREEN_HEIGHT * 0.84))
        s().SCREEN.blit(text_surf, text_rect)
        pygame.display.update()

    def __init__(self, game_name, version, authors):
        self.game_name = game_name
        self.version = version
        self.authors = authors

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
