import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer
from gui.BaseWindow import BaseWindow, HALIGN_RIGHT
import models.Config as config

DEFAULT_HEIGHT = config.SCREEN_HEIGHT
DEFAULT_WIDTH = config.SCREEN_WIDTH / 5

class Inventory(BaseWindow):

    def __init__(self, surface):
        super(Inventory, self).__init__(surface, DEFAULT_WIDTH, DEFAULT_HEIGHT, halign=HALIGN_RIGHT)

    def _renderContent(self):
        lines = []

        # Render the date/time info
        gameTime = GameTime.Instance()

        for item in getPlayer().rucksack:
            lines.append(item.displayName)

        for i, line in enumerate(lines):
            renderedText = self.font.render(line, 1, self.FONT_COLOR)
            dest = (self.MARGIN, self.MARGIN + i*self.LINE_HEIGHT)
            self.surface.blit(renderedText, dest)
