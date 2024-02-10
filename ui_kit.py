import pygame
from state_manager import s
from pygame import gfxdraw
from functools import lru_cache
from constants import *


def text_objects(text, font, colour=BLACK):
    text_surface = font.render(text, True, colour)
    return text_surface, text_surface.get_rect()




def button(text, x, y, w, h, click, inactive_colour=BLUE, active_colour=LIGHT_BLUE, text_colour=WHITE, spacing: int=1):
    if spacing > 0:
        text = (' ' * spacing).join(text)
    mouse = pygame.mouse.get_pos()
    return_value = False
    if x < mouse[0] < x + w and y < mouse[1] < y + h:  # if mouse is hovering the button
        pygame.draw.rect(s().SCREEN, active_colour, (x, y, w, h))
        if click and pygame.time.get_ticks() > 100: return_value = True
    else: pygame.draw.rect(s().SCREEN, inactive_colour, (x, y, w, h))

    text_surf, text_rect = text_objects(text, s().SMALL_TEXT, colour=text_colour)
    text_rect.center = (int(x + w / 2), int(y + h / 2))
    s().SCREEN.blit(text_surf, text_rect)
    return return_value


def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)


def toggle_btn(text, x, y, w, h, click, text_colour=BLACK, enabled=True, draw_toggle=True, blit_text=True,
               enabled_color=LIGHT_BLUE, disabled_color=GREY):
    mouse = pygame.mouse.get_pos()
    # draw_toggle and blit_text are used to reduce redundant drawing and blitting (improves quality)
    rect_height = h // 2
    if rect_height % 2 == 0: rect_height += 1
    if enabled and draw_toggle:
        pygame.draw.rect(s().SCREEN, WHITE, (x + s().TOGGLE_WIDTH - h // 4, y, s().TOGGLE_ADJ + h, rect_height))
        pygame.draw.rect(s().SCREEN, enabled_color, (x + s().TOGGLE_WIDTH, y, s().TOGGLE_ADJ, rect_height))
        draw_circle(s().SCREEN, int(x + s().TOGGLE_WIDTH), y + h // 4, h // 4, enabled_color)
        draw_circle(s().SCREEN, int(x + s().TOGGLE_WIDTH + s().TOGGLE_ADJ), y + h // 4, h // 4, enabled_color)
        draw_circle(s().SCREEN, int(x + s().TOGGLE_WIDTH + s().TOGGLE_ADJ), y + h // 4, h // 5, WHITE)  # small inner circle
    elif draw_toggle:
        pygame.draw.rect(s().SCREEN, WHITE, (x + s().TOGGLE_WIDTH - h // 4, y, s().TOGGLE_ADJ + h, rect_height))
        pygame.draw.rect(s().SCREEN, disabled_color, (x + s().TOGGLE_WIDTH, y, s().TOGGLE_ADJ, rect_height))
        draw_circle(s().SCREEN, int(x + s().TOGGLE_WIDTH), y + h // 4, h // 4, disabled_color)
        draw_circle(s().SCREEN, int(x + s().TOGGLE_WIDTH + s().TOGGLE_ADJ), y + h // 4, h // 4, disabled_color)
        draw_circle(s().SCREEN, int(x + s().TOGGLE_WIDTH), y + h // 4, h // 5, WHITE)  # small inner circle
    if blit_text:
        text_surf, text_rect = text_objects(text, s().MEDIUM_TEXT, colour=text_colour)
        text_rect.topleft = (x, y)
        s().SCREEN.blit(text_surf, text_rect)
    return x < mouse[0] < x + w and y < mouse[1] < y + h and click and pygame.time.get_ticks() > 100


def hide_mouse():
    pygame.event.set_grab(False)
    pygame.mouse.set_visible(False)


def show_mouse():
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(True)
