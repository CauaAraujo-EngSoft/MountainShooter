# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)
COLOR_DARK_GREEN = (0, 100, 0)
COLOR_DARK_BLUE = (0, 0, 139)
COLOR_DARK_BLUE_TITLE = (0, 40, 120)
COLOR_GOLD = (255, 215, 0)

# E
EVENT_COIN = pygame.USEREVENT + 2
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level1Bg7': 7,
    'Level1Bg8': 8,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
    'Coin': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level1Bg8': 999,
    'Player1': 200,
    'Player2': 200,
    'Enemy1': 50,
    'Enemy2': 60,
    'Coin': 1,
}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 2500

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
WATER_TOP_LIMIT = 140
WATER_BOTTOM_LIMIT = WIN_HEIGHT - 20
