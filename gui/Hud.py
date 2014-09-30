import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer
from gui.BaseWindow import BaseWindow

class Hud(BaseWindow):

    def __init__(self, surface):
        super(Hud, self).__init__(surface, width=180, height=100)

    def _renderContent(self):
        lines = []

        # Render the date/time info
        gameTime = GameTime.Instance()
        lines.append(gameTime.getFormattedDateTime())

        # Render the player's $$$
        lines.append("Money: %s" % getPlayer().money)

        # Render the current tool
        toolText = "None"
        if getPlayer().currentTool:
            toolText = getPlayer().currentTool.displayName
        lines.append("Tool: " + toolText)

        # Render the current held item
        itemText = "None"
        if getPlayer().currentItem:
            itemText = getPlayer().currentItem.displayName
        lines.append("Held Item: " + itemText)


        for i, line in enumerate(lines):
            renderedText = self.font.render(line, 1, self.FONT_COLOR)
            dest = (self.MARGIN, self.MARGIN + i*self.LINE_HEIGHT)
            self.surface.blit(renderedText, dest)
