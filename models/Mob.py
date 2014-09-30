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
    def __init__(self, sprite, pos=(0,0), height=config.MOB_SIZE[1], width=config.MOB_SIZE[0], collision=False):
        self._direction = Direction.DOWN
        self.walkTimer=config.WALK_TIMER

        super(Mob, self).__init__(sprite, pos, height, width, collision)

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

    def update(self):
        if self.walkTimer > 0:
            self.walkTimer-=1

    def move(self, currentMap, direction):
        if self.walkTimer > 0:
            return
        self.walkTimer=config.WALK_TIMER


        targetPos = self._getCoordinates(self.pos, direction)
        if not currentMap.isWalkable(*targetPos):
            return

        self.pos = targetPos

        self._direction = direction
        self._updateRect()
        self._updateImage()