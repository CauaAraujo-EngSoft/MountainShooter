import pygame

from code.Coin import Coin
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        pass

    @staticmethod
    def verify_collision(entity_list: list[Entity], coins):

        coins_collected = coins

        for i in range(len(entity_list)):

            ent1 = entity_list[i]

            EntityMediator.__verify_collision_window(ent1)

            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                coins_collected += EntityMediator.__verify_collision_entity(ent1, ent2)
                coins_collected += EntityMediator.__verify_collision_entity(ent2, ent1)

        return coins_collected

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):

        if isinstance(ent1, Player) and isinstance(ent2, Enemy):

            if ent1.rect.colliderect(ent2.rect):

                current_time = pygame.time.get_ticks()

                if current_time - ent1.last_hit >= 1000:
                    ent1.health -= 20
                    ent1.last_hit = current_time

        if isinstance(ent1, Player) and isinstance(ent2, Coin):

            if ent1.rect.colliderect(ent2.rect):
                ent2.health = 0
                return 1

        return 0