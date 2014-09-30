import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer

HALIGN_LEFT = 0
HALIGN_CENTER = 1
HALIGN_RIGHT = 2

VALIGN_TOP = 0
VALIGN_CENTER = 1
VALIGN_BOTTOM = 2

WIDTH_AUTO = "auto"
HEIGHT_AUTO = "auto"

class BaseWindow(object):
    FONT_SIZE = 18
    FONT_FACE = None
    FONT_COLOR = (10,10,10)
    LINE_HEIGHT = FONT_SIZE * 1.2
    MARGIN = 10

    def __init__(self, surface, width, height, halign=HALIGN_LEFT, valign=VALIGN_TOP):
        self._parentSurface = surface
        self.width = width
        self.height = height
        self.halign = halign
        self.valign = valign
        self._contentHeight = 0
        self._contentWidth = 0

        self.font = pygame.font.Font(self.FONT_FACE, self.FONT_SIZE)

    def renderContent(self):
        pass

    def render(self):
        parentRect = self._parentSurface.get_rect()
        width = self.width
        height = self.height

        if width == WIDTH_AUTO:
            # TODO
            pass

        if height == HEIGHT_AUTO:
            # TODO
            pass


        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

        # Figure out the left for the window surface
        left = 0
        if self.halign == HALIGN_RIGHT:
            left = parentRect.width - width

        elif self.halign == HALIGN_CENTER:
            left = parentRect.width/2 - width/2

        # Figure out the top for the window surface
        top = 0
        if self.valign == VALIGN_BOTTOM:
            top = parentRect.height - height

        elif self.valign == VALIGN_CENTER:
            top = parentRect.height/2 - height/2

        # Make the subsurface for the window and fill it
        # Then blit onto the main surface
        self.surface.fill((255, 255, 255, 100))
        self._renderContent()
        self._parentSurface.blit(self.surface, (left, top))

