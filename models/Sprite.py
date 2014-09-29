"""
Sprite

"""
import pygame
from math import floor

import models.Config as config

class Direction:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite, pos=(0,0)):
        super(Sprite, self).__init__()

        filename = r'%s\media\images\sprites\%s.png' % (config.PROJECT_ROOT, sprite)
        self.image = pygame.image.load(filename)

        self.pos = pos
        self.rect = self.image.get_rect()

        self._updateRect()

    def _updateRect(self):
        self.rect.x = self.pos[0] * config.TILE_SIZE

        # We want the bottom of the mob sprite to touch the bottom of the tile.
        # So we need to offset the rectangle by the height difference between the mob and tile.
        heightDifference = (config.MOB_SIZE[1] - config.TILE_SIZE)
        self.rect.y = (self.pos[1] * config.TILE_SIZE) - heightDifference

    def _getCoordinates(self, coordinates, direction):
        """
        Get a pair of coordinates that are one square [direction] of [coordinates]
        """
        if direction == Direction.UP:
            return (coordinates[0], coordinates[1]-1)

        elif direction == Direction.DOWN:
            return (coordinates[0], coordinates[1]+1)

        elif direction == Direction.LEFT:
            return (coordinates[0]-1, coordinates[1])

        elif direction == Direction.RIGHT:
            return (coordinates[0]+1, coordinates[1])

        else:
            raise ValueError("Unrecognized direction %s" % direction)

    def use_tool(self, tool):
        return False

    def interact(self, held_item):
        return False