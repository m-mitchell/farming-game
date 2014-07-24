"""
Item

This is an abstract class that provides some common functionality for all items
(e.g., crops, jewelry, seeds, ...)

"""

import json
from abc import ABCMeta

import models.Config as config

# Our main Item class
class Item(metaclass=ABCMeta):

    def __init__(self, internalName):
        # The constructor. Set up the internal vars.
        self.internalName = ""
        self.displayName = ""
        self.buyPrice = 0
        self.shipPrice = 0

        jsonFile = r'%s\data\items\%s.json' % (config.PROJECT_ROOT, internalName)
        with open(jsonFile) as dataFile:    
            self._rawData = json.load(dataFile)
            
            self.internalName = self._rawData['internalName']
            self.displayName = self._rawData['displayName']
            self.shipPrice = int(self._rawData['shipPrice'])
            self.buyPrice = int(self._rawData['buyPrice'])


    def __str__(self):
        return self.displayName


    
