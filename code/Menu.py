#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, COLOR_GOLD, COLOR_DARK_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        state = "story"
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text_outline(60, "OCEAN", (0, 120, 255), (0, 0, 0), (WIN_WIDTH / 2, 70))
            self.menu_text_outline(60, "ADVENTURE", (0, 120, 255), (0, 0, 0), (WIN_WIDTH / 2, 140))

            self.menu_text_story(12, "Uma Tartaruga, um Polvo e muitas aventuras..", COLOR_WHITE, (0, 0, 0),
                                 ((WIN_WIDTH / 2) - 100, 200))

            self.menu_text_story(12, "A Tartaruga navega com as setas direcionais.", COLOR_WHITE, (0, 0, 0),
                                 ((WIN_WIDTH / 2) - 100, 220))

            self.menu_text_story(12, "A Lula navega com as teclas W, A, S e D.", COLOR_WHITE, (0, 0, 0),
                                 ((WIN_WIDTH / 2) - 100, 240))

            self.menu_text_story(12, "Pressione ESC para voltar ao menu", COLOR_WHITE, (0, 0, 0),
                                 ((WIN_WIDTH / 2) - 100, 260))

            self.menu_text_story(12, "Não se esqueça... evite o perigo", COLOR_WHITE, (0, 0, 0),
                                 ((WIN_WIDTH / 2) - 100, 280))


            for i in range(len(MENU_OPTION)):
                    if i == menu_option:
                        self.menu_text(20, MENU_OPTION[i], COLOR_GOLD, ((WIN_WIDTH / 2) + 160, 200 + 25 * i))
                    else:
                        self.menu_text(20, MENU_OPTION[i], COLOR_DARK_BLUE, ((WIN_WIDTH / 2) + 160, 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_text_story(self, text_size, text, text_color, outline_color, pos):
        font = pygame.font.SysFont("Arial", text_size, bold=True)

        # borda preta (contorno)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            surf = font.render(text, True, outline_color)
            rect = surf.get_rect(center=(pos[0] + dx, pos[1] + dy))
            self.window.blit(surf, rect)

        # texto principal
        surf = font.render(text, True, text_color)
        rect = surf.get_rect(center=pos)
        self.window.blit(surf, rect)

    def menu_text_outline(self, text_size, text, text_color, outline_color, pos):
        font = pygame.font.SysFont("Arial Black", text_size, bold=True)

        # contorno (desenha várias vezes em volta)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            surf = font.render(text, True, outline_color)
            rect = surf.get_rect(center=(pos[0] + dx, pos[1] + dy))
            self.window.blit(surf, rect)

        # texto principal
        surf = font.render(text, True, text_color)
        rect = surf.get_rect(center=pos)
        self.window.blit(surf, rect)