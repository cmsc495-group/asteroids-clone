import pygame

"""Define configuration of scene settings."""
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960
CLOCK = pygame.time.Clock()
FRAMERATE = 60
DT = 0
LIVES = 3
SCORE = 0

"""Configure behavior of player-fired projectiles."""
PROJECTILE_SPEED = 500
PROJECTILE_DAMAGE = 10

"""Create globally-accessible sprite groups."""
PLAYER_SPRITE = pygame.sprite.GroupSingle()
ASTEROID_SPRITES = pygame.sprite.Group()
PROJECTILE_SPRITES = pygame.sprite.Group()
