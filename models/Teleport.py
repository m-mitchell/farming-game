"""
Teleport

"""

from models.Sprite import Sprite
from models.GameTime import GameTime
import models.Config as config
from models.PlayerCharacter import getPlayer
from controllers.BaseController import getController

class Teleport(Sprite):
    def __init__(self, pos, **kwargs):
        image = "teleport"
        super(Teleport, self).__init__(image, pos)

        self._target = kwargs['target']
        self._targetX = kwargs['targetX']
        self._targetY = kwargs['targetY']

    def walkTrigger(self):
        getController().setMap(self._target)
        getPlayer().pos = (int(self._targetX), int(self._targetY))