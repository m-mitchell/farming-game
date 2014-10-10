"""
Bed

"""

from models.Sprite import Sprite
from models.GameTime import GameTime
import models.Config as config
from controllers.BaseController import getController
from gui.MessageBox import MessageBox

class Sign(Sprite):
    def __init__(self, pos):
        image = "sign"
        super(Sign, self).__init__(image, pos, collision=True)

    def interact(self, item):
        text = "Welcome to the farm!\nIt's farmalicious!"
        messagebox = MessageBox(text=text)
        getController().setGui(messagebox)