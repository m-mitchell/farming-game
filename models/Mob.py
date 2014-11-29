"""
Mob

"""
import pygame
from math import floor

from models.Sprite import Sprite
import models.Config as config

class Direction:
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Mob(Sprite):
    def __init__(self, sprite, pos=(0,0), height=config.MOB_SIZE[1], width=config.MOB_SIZE[0], speed=config.ANIM_MEDIUM, collision=False):
        self._direction = Direction.DOWN

        self.walkTimer = 0
        self._walking = False
        self._prevPos = None

        super(Mob, self).__init__(sprite, pos, height, width, speed, collision)

    def teleport(self, x, y):
        self.pos = (int(x), int(y))
        self._spriteOffset = (0, 0)
        self._prevPos = None

    def update(self):
        if self.walkTimer > 0:
            self.walkTimer-=1
            self._updateSpriteOffset()
        else:
            self._walking = False
            self._spriteOffset = (0, 0)
            self._prevPos = None

        super(Mob, self).update()

    def move(self, currentMap, direction):
        if self.walkTimer > 0:
            return
        self.walkTimer=config.WALK_TIMER
        self._walking=True

        # Even if the target square isn't walkable, we can still turn in that direction.
        self._direction = direction

        targetPos = self._getCoordinates(self.pos, direction)
        if not currentMap.isWalkable(*targetPos):
            self._spriteOffset = (0, 0)
            self._prevPos = None
            return

        self._prevPos = self.pos
        self.pos = targetPos

        self._updateRect()
        self._updateImage()

    def _updateSpriteOffset(self):
        if not self._prevPos:
            self._spriteOffset = (0,0)
            return

        walkFractionMultiplier = self.walkTimer / config.WALK_TIMER # Fraction of tile moved across (based on walk timer)
        pixelMultiplier = config.TILE_SIZE # To convert from pos fraction to actual pixel offset
        xDirectionMultiplier = (self._prevPos[0] - self.pos[0]) # 1, 0, -1 depending on movement
        yDirectionMultiplier = (self._prevPos[1] - self.pos[1]) # 1, 0, -1 depending on movement

        xOffset = walkFractionMultiplier * xDirectionMultiplier * pixelMultiplier
        yOffset = walkFractionMultiplier * yDirectionMultiplier * pixelMultiplier
        self._spriteOffset = (int(xOffset), int(yOffset))

    def _updateAnimation(self):
        # Never eat shredded wheat. 
        if self._direction == Direction.UP:
            self._animation = self._animations[0]

        elif self._direction == Direction.RIGHT:
            self._animation = self._animations[1]

        elif self._direction == Direction.DOWN:
            self._animation = self._animations[2]

        elif self._direction == Direction.LEFT:
            self._animation = self._animations[3]

    def _updateImage(self):
        if self._animIndex is None:
            self._animIndex = -1

        if self._walking:
            self._animTimer-=1
            if self._animTimer <= 0:
                self._animIndex = (self._animIndex + 1) % len(self._animation)
                self._animTimer = self._animSpeed
        else:
            self._animIndex = 0

        self.image = self._animation[self._animIndex]