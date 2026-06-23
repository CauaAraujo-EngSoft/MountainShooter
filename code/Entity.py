#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.last_hit = 0
        from code.Const import WIN_WIDTH, WIN_HEIGHT

        self.anim_index = 0
        self.anim_timer = 0
        self.anim_speed = 10  # menor = mais rápido

        self.base_name = name

        self.frames = []
        self._load_frames()

        self.surf = self.frames[0]

        if 'Level1Bg' in name:
            self.frames = [
                pygame.transform.scale(frame, (WIN_WIDTH, WIN_HEIGHT))
                for frame in self.frames
            ]
            self.surf = self.frames[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    def _load_frames(self):
        i = 0

        while True:
            try:
                if i == 0:
                    img = pygame.image.load(f'./asset/{self.base_name}.png').convert_alpha()
                else:
                    img = pygame.image.load(f'./asset/{self.base_name}.{i}.png').convert_alpha()

                self.frames.append(img)
                i += 1

            except:
                break

    def update_animation(self):
        self.anim_timer += 1

        if self.anim_timer >= self.anim_speed:
            self.anim_timer = 0
            self.anim_index = (self.anim_index + 1) % len(self.frames)
            self.surf = self.frames[self.anim_index]

    @abstractmethod
    def move(self, ):
        pass

