"""
Bed

"""

from models.Sprite import Sprite
from models.GameTime import GameTime
import models.Config as config
from controllers.BaseController import getController
from gui.Menu import Menu

# Our main Bed class
class Bed(Sprite):
    def __init__(self, pos):
        image = "bed"
        super(Bed, self).__init__(image, pos, collision=True, height=config.TILE_SIZE*2)

    def interact(self, item):
        options = [
            ('yes', 'Yes'),
            ('no', 'No'),
        ]
        text = "Are you sure you want to sleep?"
        menu = Menu(options, escape="no", text=text, handler=self.handleMenuSelection)
        getController().setGui(menu)

    def handleMenuSelection(self, option):
        if option == 'yes':
            self.__sleep()
        getController().setGui(None)

    def __sleep(self):
        gameTime = GameTime.Instance()
        gameTime.advanceDay()