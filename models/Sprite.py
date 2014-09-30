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
    def __init__(self, sprite, pos, height=config.TILE_SIZE, width=config.TILE_SIZE, speed=config.ANIM_MEDIUM, collision=False):
        super(Sprite, self).__init__()

        self.pos = pos
        self.height = height
        self.width = width
        self.collision=collision

        self._animIndex = None
        self._animSpeed = speed
        self._animTimer = speed

        filename = r'%s\media\images\sprites\%s.png' % (config.PROJECT_ROOT, sprite)
        self._spritesheet = pygame.image.load(filename)
        self._loadSprites()

        self._updateImage()
        self.rect = self.image.get_rect()
        self._updateRect()

    def _loadSprites(self):
        # Figure out the height and width of the spritesheet (in sprites)
        spritesheetRect = self._spritesheet.get_rect()
        sheetWidthInTiles = floor(spritesheetRect.width / self.width)
        sheetHeightInTiles = floor(spritesheetRect.height / self.height)

        # Each row in the spritesheet represents a different animation.
        # For now, each animation in a spritesheet must have the same number of frames. (TODO?)
        self._animations = []
        for y in range(0, sheetHeightInTiles):
            animation = []
            for x in range(0, sheetWidthInTiles):
                rect = pygame.Rect(x*self.width, y*self.height, self.width, self.height)
                sprite = self._spritesheet.subsurface(rect)
                animation.append(sprite)
            self._animations.append(animation)

    def _updateImage(self):
        self._animation = self._animations[0]

        if self._animIndex is None:
            self._animIndex = -1


        self._animTimer-=1
        if self._animTimer <= 0:
            self._animIndex = (self._animIndex + 1) % len(self._animation)
            self._animTimer = self._animSpeed

        self.image = self._animation[self._animIndex]

    def update(self):
        self._updateImage()

    def _updateRect(self):
        self.rect.x = self.pos[0] * config.TILE_SIZE

        # We want the bottom of the sprite to touch the bottom of the tile.
        # So we need to offset the rectangle by the height difference between the sprite and tile.
        heightDifference = (self.height - config.TILE_SIZE)
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

    def useTool(self, tool):
        return False

    def interact(self, heldItem):
        return False