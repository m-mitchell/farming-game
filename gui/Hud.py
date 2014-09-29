import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer

class Hud(object):
    FONT_SIZE = 18
    FONT_FACE = None
    FONT_COLOR = (10,10,10)
    LINE_HEIGHT = FONT_SIZE * 1.2
    MARGIN = 10

    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font(self.FONT_FACE, self.FONT_SIZE)

    def render(self):
        lines = []

        # Render the date/time info
        gameTime = GameTime.Instance()
        lines.append(gameTime.getFormattedDateTime())

        # Render the current tool
        toolText = "None"
        if getPlayer().currentTool:
            toolText = getPlayer().currentTool.displayName
        lines.append("Tool: " + toolText)


        for i, line in enumerate(lines):
            renderedText = self.font.render(line, 1, self.FONT_COLOR)
            dest = (self.MARGIN, self.MARGIN + i*self.LINE_HEIGHT)
            self.surface.blit(renderedText, dest)
