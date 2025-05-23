from pathlib import Path
import pygame
from . import globals

"""Load asset file paths at import"""
sprite_path = Path("assets", "art", "projectiles", "laserBullet.png")
upgrade_path = Path("assets", "art", "projectiles", "laserBulletUp.png")

"""Class to handle projectiles fired from Player object."""
class Projectile(pygame.sprite.Sprite):
    """Initialize with sprite properties and initial custom gameplay settings."""
    def __init__(self, pos, heading, upgraded=False):
        super().__init__()
        self.ttl = 2500
        self.sprite_scaling = 0.4
        #Update sprite image for damage boost projectiles
        if upgraded:
            self.large_image = pygame.image.load(upgrade_path).convert_alpha()
        else:
            self.large_image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale_by(self.large_image, self.sprite_scaling)
        self.start_img = self.image
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(pos)
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = globals.PROJECTILE_SPEED
        self.heading = heading
        self.vel = pygame.math.Vector2.from_polar((self.speed, heading))
        self.time_alive = 0

    """Called on every frame, update state and position."""
    def update(self):
        self.time_alive += globals.CLOCK.get_time()
        if self.time_alive > self.ttl:
            self.kill()
            return
        self.rotate()
        self.pos += self.vel * globals.DT
        self.rect.center = self.pos
        self.mask = pygame.mask.from_surface(self.image)

    """Rotate sprite in the direction of velocity."""
    def rotate(self):
        self.image = pygame.transform.rotozoom(self.start_img, -self.heading - 90, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
