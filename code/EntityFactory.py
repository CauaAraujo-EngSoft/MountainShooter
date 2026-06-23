#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT, WATER_TOP_LIMIT
from code.Enemy import Enemy
from code.Player import Player
from code.Coin import Coin

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(9):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WATER_TOP_LIMIT + 50))

            case 'Player2':
                return Player('Player2', (10, WATER_TOP_LIMIT + 90))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(WATER_TOP_LIMIT, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(WATER_TOP_LIMIT, WIN_HEIGHT - 40)))

            case 'Coin':
                return Coin(
                    'Coin',
                    (WIN_WIDTH + 10, random.randint(WATER_TOP_LIMIT, WIN_HEIGHT - 40))
                )