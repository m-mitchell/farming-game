"""
Bed

"""

from models.Sprite import Sprite
from models.GameTime import GameTime

# Our main Bed class
class Bed(Sprite):
    def __init__(self, pos):
        image = "bed"
        super(Bed, self).__init__(image, pos)

    def interact(self, item):
        if item is None:
            self.__sleep()

    def __sleep(self):
        print("Sleeping...")
        gameTime = GameTime.Instance()
        gameTime.advanceDay()