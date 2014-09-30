"""
ShippingBin

"""

from models.Sprite import Sprite
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer
import models.Config as config

# Our main Bed class
class ShippingBin(Sprite):
    def __init__(self, pos):
        image = "shippingBin"
        super(ShippingBin, self).__init__(image, pos, collision=True, height=config.TILE_SIZE*2, width=config.TILE_SIZE*2)

    def interact(self, item):
        self.__ship(item)

    def __ship(self, item):
        rucksack = getPlayer().rucksack
        rucksack.remove(item)
        getPlayer().money += item.shipPrice