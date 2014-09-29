"""
Mob

"""
import pygame
from math import floor

import models.Config as config

class Direction:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Mob(pygame.sprite.Sprite):
    def __init__(self, sprite, pos=(0,0)):
        super(Mob, self).__init__()

        filename = r'%s\media\images\mobs\%s.png' % (config.PROJECT_ROOT, sprite)
        self._spritesheet = pygame.image.load(filename)
        self._loadSprites()

        self._direction = Direction.DOWN
        self._animation = self._animations[1]
        self.image = self._animation[0]

        self.walkTimer=config.WALK_TIMER
        
        self.pos = pos
        self.rect = self.image.get_rect()
        self._updateRect()
        self._updateImage()

    def _loadSprites(self):
        # Figure out the height and width of the spritesheet (in sprites)
        spritesheetRect = self._spritesheet.get_rect()
        sheetWidthInTiles = floor(spritesheetRect.width / config.MOB_SIZE[0])
        sheetHeightInTiles = floor(spritesheetRect.height / config.MOB_SIZE[1])


        # Each row in the spritesheet represents a different animation.
        # For now, each animation in a spritesheet must have the same number of frames. (TODO?)
        self._animations = []
        for y in range(0, sheetHeightInTiles):
            animation = []
            for x in range(0, sheetWidthInTiles):
                rect = pygame.Rect(x*config.MOB_SIZE[0], y*config.MOB_SIZE[1], config.MOB_SIZE[0], config.MOB_SIZE[1])
                sprite = self._spritesheet.subsurface(rect)
                animation.append(sprite)
            self._animations.append(animation)

    def _updateImage(self):
        # Never eat shredded wheat. 
        if self._direction == Direction.UP:
            self._animation = self._animations[0]

        elif self._direction == Direction.RIGHT:
            self._animation = self._animations[1]

        elif self._direction == Direction.DOWN:
            self._animation = self._animations[2]

        elif self._direction == Direction.LEFT:
            self._animation = self._animations[3]

        self.image = self._animation[0]


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

    def update(self):
        if self.walkTimer > 0:
            self.walkTimer-=1

    def move(self, current_map, direction):
        if self.walkTimer > 0:
            return
        self.walkTimer=config.WALK_TIMER


        target_pos = self._getCoordinates(self.pos, direction)
        if not current_map.is_walkable(*target_pos):
            return

        self.pos = target_pos

        self._direction = direction
        self._updateRect()
        self._updateImage()