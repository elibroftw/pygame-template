from state_manager import s

def game():
    # some code here
    while True:
        if not pygame.mouse.get_focused():
            if pause_menu(player) == 'Main Menu': return 'Main Menu'
        for event in pygame.event.get():
            pressed_keys = pygame.key.get_pressed()
            alt_f4 = (event.type == KEYDOWN and event.key == K_F4
                      and (pressed_keys[K_LALT] or pressed_keys[K_RALT]))
            if event.type == QUIT or alt_f4: sys.exit()
            if event.type == KEYDOWN:
                # handle keydown events here
                # pause if Esc / P was pressed.
                # elif on the assumption there's an if statement
                elif event.key == K_ESCAPE and not pressed_keys[K_p] or event.key == K_p and not pressed_keys[K_ESCAPE]:
                    if pause_menu(player) == 'Main Menu': return 'Main Menu'
        # other game loop code


def pause_menu_setup(background):
    SCREEN.blit(background, (0, 0))
    background = SCREEN.copy()
    text_surf, text_rect = text_objects('Pause Menu', MENU_TEXT, colour=WHITE)
    text_rect.center = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 4))
    SCREEN.blit(text_surf, text_rect)
    pygame.display.update()
    return background


def pause_menu(player):
    show_mouse()
    paused = True
    facing_left = player.facing_right  # store the pre-pause value in case player doesn't hold a right/left key down
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA, 32)
    # background.fill((255, 255, 255, 160))  # for white pause menu
    background.fill((*MATTE_BLACK, 160))     # darken the background
    background = pause_menu_setup(background)
    while paused:
        click = False
        pks = pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            alt_f4 = (event.type == KEYDOWN and event.key == K_F4
                      and (pressed_keys[K_LALT] or pressed_keys[K_RALT]))
            if event.type == QUIT or alt_f4: sys.exit()
            elif event.type == KEYDOWN:
                right_key = event.key == K_RIGHT and not pks[K_d] or event.key == K_d and not pks[K_RIGHT]
                left_key = event.key == K_LEFT and not pks[K_a] or event.key == K_a and not pks[K_LEFT]
                if right_key: player.go_right()
                elif left_key: player.go_left()
                elif event.key in (pygame.K_ESCAPE, pygame.K_p): paused = False
                elif event.key == K_m: return 'Main Menu'
                elif event.key == K_SPACE: return 'Resume'
                elif event.key == K_q: sys.exit()
            elif event.type == MOUSEBUTTONDOWN: click = True
            elif event.type == KEYUP:
                if event.key in (K_d, K_RIGHT, K_a, K_LEFT):
                    player.stop(pygame.key.get_pressed())
                    player.facing_right = facing_left
        if button('R E S U M E', *button_layout_4[0], click): return 'Resume'
        elif button('M A I N  M E N U', *button_layout_4[1], click): return 'Main Menu'
        elif button('S E T T I N G S', *button_layout_4[2], click):
            settings_menu()
            pause_menu_setup(background)
        elif button('Q U I T  G A M E', *button_layout_4[3], click): sys.exit()
        pygame.display.update(button_layout_4)
        clock.tick(60)
    return 'Resume'
