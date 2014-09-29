import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer

class Inventory(object):
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

        for item in getPlayer().rucksack:
            lines.append(item.displayName)

        for i, line in enumerate(lines):
            renderedText = self.font.render(line, 1, self.FONT_COLOR)
            dest = (self.MARGIN, 200 + self.MARGIN + i*self.LINE_HEIGHT)
            self.surface.blit(renderedText, dest)
