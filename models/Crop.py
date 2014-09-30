"""
Crop

"""
import pygame

import models.GameTime as gt

from models.Item import Item
from models.Seed import Seed

import models.Config as config

class GrowSpeed:
    FAST = 2
    NORMAL = 1
    SLOW = 0.5
    NONE = 0

# Our main Crop class
class Crop(Item):
    def __init__(self, internalName):
        super().__init__(internalName)

        # The constructor. Set up the internal vars.
        self.growTime = int(self._rawData['growTime'])
        self.regrows = bool(self._rawData['regrows'])
        if 'regrowTime' in self._rawData:
            self.regrowTime = int(self._rawData['regrowTime'])

        self.spriteChanges = self._rawData['spriteChanges']

        self.seasons = {}
        for season, speed in self._rawData['seasons'].items():
            parsedSeason = getattr(gt.Season, season.upper())
            parsedSpeed = getattr(GrowSpeed, speed.upper())
            self.seasons[parsedSeason] = parsedSpeed


    @property
    def seed(self):
        return Seed(self._rawData['seed'])

    def getFieldImage(self, cropIndex):
        filename = r'%s\media\images\crops\%s_%s.png' % (config.PROJECT_ROOT, self.internalName, cropIndex)
        return pygame.image.load(filename)


