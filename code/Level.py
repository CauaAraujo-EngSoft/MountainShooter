#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, EVENT_COIN, COLOR_DARK_GREEN, \
    COLOR_DARK_BLUE, COLOR_GOLD
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000 # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.coins = 0

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        pygame.time.set_timer(
            EVENT_COIN,
            random.randint(5000, 15000)
        )


    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                ent.update_animation()
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "MENU"

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_COIN:
                    self.entity_list.append(
                        EntityFactory.get_entity('Coin')
                    )

                    pygame.time.set_timer(
                        EVENT_COIN,
                        random.randint(5000, 15000)
                    )

            # printed text
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            #texto da vida
            for ent in self.entity_list:

                if ent.name == 'Player1':
                    self.level_text(
                        14,
                        f'P1: {ent.health}',
                        COLOR_DARK_GREEN,
                        (10, 5)
                    )

                    self.draw_health_bar(
                        ent.health,
                        200,
                        80,
                        8
                    )

                if ent.name == 'Player2':
                    self.level_text(
                        14,
                        f'P2: {ent.health}',
                        COLOR_DARK_BLUE,
                        (10, 25)
                    )

                    self.draw_health_bar(
                        ent.health,
                        200,
                        80,
                        28
                    )

            #texto da coin
            self.level_text(
                14,
                f'Diamantes: {self.coins}/20',
                COLOR_GOLD,
                (10, 45)
            )

            if self.coins >= 20:
                self.victory_screen()
                return

            pygame.display.flip()
            #Collision
            self.coins = EntityMediator.verify_collision(
                entity_list=self.entity_list,
                coins=self.coins
            )
            EntityMediator.verify_health(entity_list=self.entity_list)

            player1_alive = False

            for ent in self.entity_list:
                if ent.name == 'Player1':
                    player1_alive = True

            if not player1_alive:
                self.game_over_screen()

                return

            pass

    def draw_health_bar(self, health, max_health, x, y):
        largura = 100
        altura = 10

        vida_atual = (health / max_health) * largura

        pygame.draw.rect(
            self.window,
            (255, 0, 0),
            (x, y, largura, altura)
        )

        pygame.draw.rect(
            self.window,
            (0, 255, 0),
            (x, y, vida_atual, altura)
        )

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def victory_screen(self):

        while True:

            bg = pygame.image.load('./asset/MenuBg.png').convert_alpha()
            self.window.blit(bg, (0, 0))

            self.level_text(
                30,
                "PARABENS!",
                COLOR_GOLD,
                (180, 80)
            )

            self.level_text(
                20,
                "Voce coletou 20 diamantes!",
                COLOR_WHITE,
                (130, 140)
            )

            self.level_text(
                18,
                "Pressione ENTER para voltar ao menu",
                COLOR_WHITE,
                (90, 220)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return

    def game_over_screen(self):

        while True:

            bg = pygame.image.load('./asset/MenuBg.png').convert_alpha()
            self.window.blit(bg, (0, 0))

            self.level_text(
                30,
                "GAME OVER",
                COLOR_WHITE,
                (170, 80)
            )

            self.level_text(
                20,
                "Voce foi derrotado!",
                COLOR_WHITE,
                (160, 140)
            )

            self.level_text(
                18,
                "Pressione ENTER para voltar ao menu",
                COLOR_WHITE,
                (90, 220)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return