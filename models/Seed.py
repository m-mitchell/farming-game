"""
Seed

"""

from models.Item import Item

# Our main Seed class
class Seed(Item):
    def __init__(self, internalName):
        super().__init__(internalName)
        self.crop = self._rawData['crop']