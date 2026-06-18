#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        from code.Const import WIN_WIDTH, WIN_HEIGHT

        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()

        if 'Level1Bg' in name:
            self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]



    @abstractmethod
    def move(self, ):
        pass

