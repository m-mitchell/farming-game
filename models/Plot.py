"""
Plot

This class represents a single tile of a field. 

"""
import pygame

from models.Seed import Seed
from models.Tool import Tool
from models.Crop import Crop
from models.Sprite import Sprite
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer

# Our main Plot class
class Plot(Sprite):
    def __init__(self, pos):
        image = "plot"

        # The constructor. Set up the internal vars.
        self._crop = None
        self._growTime = None
        self._plowed = False
        self._watered = False

        super(Plot, self).__init__(image, pos)

        # Add an event handler for when the day changes.
        gameTime = GameTime.Instance()
        gameTime.dayChanged.handle(self.onDayChanged)

    def useTool(self, tool):
        if type(tool) is Seed:
            self.plant(tool.crop)

        elif type(tool) is Tool:
            if tool.type == 'hoe':
                self.clear()

            elif tool.type == 'wateringCan':
                self.water()

        return False

    def interact(self, heldItem):
        print(str(self))

        if not heldItem:
            self.harvest()

    def water(self):
        self._watered = True

    def clear(self):
        self._crop = None
        self._growTime = None
        self._plowed = True

    def plant(self, internalName):
        # To plant, we need a plowed, unplanted plot.
        if not self._plowed or self._crop:
            return False

        crop = Crop(internalName)
        rucksack = getPlayer().rucksack
        seed = rucksack.search(Seed, {'internalName': crop.seed.internalName})
        if seed:
            rucksack.remove(seed)
            self._crop = crop
            self._growTime = 0

    def harvest(self):
        if not self._crop:
            return None

        if self._growTime < self._crop.growTime:
            # Not ready for harvest.
            return None

        # TODO could add some logic for quality/quantity of harvest here
        rucksack = getPlayer().rucksack
        if not rucksack.add(self._crop):
            return None

        if self._crop.regrows:
            self._crop = Crop(self._crop.internalName)
            self._growTime = self._crop.growTime - self._crop.regrowTime
        else:
            self._crop = None
            self._growTime = None

    def onDayChanged(self):
        if self._watered and self._crop and self._crop.growTime > self._growTime:
            self._growTime += 1

        self._watered = False

    def __str__(self):
        # Return a user-readable string describing the plot's contents
        plowed = ""
        if self._plowed:
            plowed = "[PLOWED]"

        if self._crop:
            watered = ""
            if self._watered:
                watered = "[WATERED]"

            return "%s (growth: %d) %s %s" % (self._crop.displayName, self._growTime, plowed, watered)
        else:
            return "Empty %s" % (plowed)

    def _updateAnimation(self):
        if self._plowed and self._watered:
            self._animation = self._animations[2]
        elif self._plowed:
            self._animation = self._animations[1]
        else:
            self._animation = self._animations[0]

    def _updateImage(self):
        super(Plot, self)._updateImage()

        # If we have a crop, we have to superimpose it on top of the plot tile.
        if self._crop:
            # Figure out which sprite we should use.
            cropIndex = 1
            for index in self._crop.spriteChanges:
                if index > self._growTime:
                    break
                cropIndex += 1

            # Get the actual image
            cropImage = self._crop.getFieldImage(cropIndex)

            # Create a temp surface and blit the plot and crop onto it.
            # If we blit the crop directly on the plot it seems to get stuck there forever ;(
            temp = pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA)
            temp.blit(self.image, (0,0))
            temp.blit(cropImage, (0,0))
            self.image = temp