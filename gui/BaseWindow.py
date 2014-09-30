import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer

class BaseWindow(object):
    FONT_SIZE = 18
    FONT_FACE = None
    FONT_COLOR = (10,10,10)
    LINE_HEIGHT = FONT_SIZE * 1.2
    MARGIN = 10

    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font(self.FONT_FACE, self.FONT_SIZE)

    def render(self):
        pass