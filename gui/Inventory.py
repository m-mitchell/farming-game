import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer
from gui.BaseWindow import BaseWindow

class Inventory(BaseWindow):

    def __init__(self, surface):
        super(Inventory, self).__init__(surface)

    def render(self):
        super(Inventory, self).render()

        lines = []

        # Render the date/time info
        gameTime = GameTime.Instance()

        for item in getPlayer().rucksack:
            lines.append(item.displayName)

        for i, line in enumerate(lines):
            renderedText = self.font.render(line, 1, self.FONT_COLOR)
            dest = (self.MARGIN, 200 + self.MARGIN + i*self.LINE_HEIGHT)
            self.surface.blit(renderedText, dest)
