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

        self.walkTimer=config.WALK_TIMER
        self._walking = False

        super(Mob, self).__init__(sprite, pos, height, width, speed, collision)

    def update(self):
        super(Mob, self).update()

        if self.walkTimer > 0:
            self.walkTimer-=1
        else:
            self._walking = False

    def move(self, currentMap, direction):
        if self.walkTimer > 0:
            return
        self.walkTimer=config.WALK_TIMER
        self._walking=True


        targetPos = self._getCoordinates(self.pos, direction)
        if not currentMap.isWalkable(*targetPos):
            return

        self.pos = targetPos

        self._direction = direction
        self._updateRect()
        self._updateImage()

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