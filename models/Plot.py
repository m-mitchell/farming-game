"""
Plot

This class represents a single tile of a field. 

"""

from models.Seed import Seed
from models.Tool import Tool
from models.Crop import Crop
from models.Sprite import Sprite
from models.GameTime import GameTime

# Our main Plot class
class Plot(Sprite):
    def __init__(self, pos):
        image = "plot"
        super(Plot, self).__init__(image, pos)

        # The constructor. Set up the internal vars.
        self._crop = None
        self._growTime = None
        self._watered = False

        # Add an event handler for when the day changes.
        gameTime = GameTime.Instance()
        gameTime.dayChanged.handle(self.on_day_changed)

    def use_tool(self, tool):
        if type(tool) is Seed:
            self.plant(tool.crop)

        elif type(tool) is Tool:
            if tool.type == 'hoe':
                self.clear()

            elif tool.type == 'wateringCan':
                self.water()

        return False

    def interact(self, held_item):
        crop_name = "Empty"
        if self._crop:
            crop_name = self._crop.internalName

        watered_status = "Dry"
        if self._watered:
            watered_status = "Watered"

        print(str(self))

    def water(self):
        self._watered = True

    def clear(self):
        self._crop = None
        self._growTime = None

    def plant(self, internalName, rucksack=None):
        crop = Crop(internalName)
        #seed = rucksack.search(Seed, {'internalName': crop.seed.internalName})
        #if seed:
        if True:
            #rucksack.remove(seed)
            self._crop = crop
            self._growTime = 0

    def harvest(self, rucksack):
        if not self._crop:
            return None

        if self._growTime < self._crop.growTime:
            # Not ready for harvest.
            return None

        # TODO could add some logic for quality/quantity of harvest here
        rucksack.add(self._crop)

        if self._crop.regrows:
            self._crop = Crop(self._crop.internalName)
            self._growTime = self._crop.growTime - self._crop.regrowTime
        else:
            self._crop = None
            self._growTime = None

    def on_day_changed(self):
        if self._watered and self._crop and self._crop.growTime > self._growTime:
            self._growTime += 1

        self._watered = False

    def __str__(self):
        # Return a user-readable string describing the plot's contents
        if self._crop:
            watered = ""
            if self._watered:
                watered = "[WATERED]"

            return "%s (growth: %d) %s" % (self._crop.displayName, self._growTime, watered)
        else:
            return "Empty"