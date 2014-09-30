"""
Bed

"""

from models.Sprite import Sprite
from models.GameTime import GameTime
import models.Config as config

# Our main Bed class
class Bed(Sprite):
    def __init__(self, pos):
        image = "bed"
        super(Bed, self).__init__(image, pos, collision=True, height=config.TILE_SIZE*2)

    def interact(self, item):
        if item is None:
            self.__sleep()

    def __sleep(self):
        print("Sleeping...")
        gameTime = GameTime.Instance()
        gameTime.advanceDay()