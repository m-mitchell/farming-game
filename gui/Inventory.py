import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer
from gui.BaseWindow import BaseWindow, HALIGN_RIGHT
import models.Config as config

class Inventory(BaseWindow):

    def __init__(self, surface):
        super(Inventory, self).__init__(surface, halign=HALIGN_RIGHT)

    def _renderContent(self, surface):
        lines = []

        # Render the date/time info
        gameTime = GameTime.Instance()

        for item in getPlayer().rucksack:
            lines.append(item.displayName)

        for i, line in enumerate(lines):
            renderedText = self.font.render(line, 1, self.FONT_COLOR)
            dest = (self.HMARGIN, self.VMARGIN + i*self.LINE_HEIGHT)
            surface.blit(renderedText, dest)
