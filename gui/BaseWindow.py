import pygame
from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer

HALIGN_LEFT = 0
HALIGN_CENTER = 1
HALIGN_RIGHT = 2

VALIGN_TOP = 0
VALIGN_CENTER = 1
VALIGN_BOTTOM = 2

SIZE_AUTO = "auto"

class BaseWindow(object):
    FONT_SIZE = 18
    FONT_FACE = None
    FONT_COLOR = (10,10,10)
    LINE_HEIGHT = FONT_SIZE * 1.2
    HMARGIN = 20
    VMARGIN = 10

    def __init__(self, surface, width=SIZE_AUTO, height=SIZE_AUTO, halign=HALIGN_LEFT, valign=VALIGN_TOP):
        self._parentSurface = surface
        self.width = width
        self.height = height
        self.halign = halign
        self.valign = valign
        self._contentHeight = 0
        self._contentWidth = 0

        self.font = pygame.font.Font(self.FONT_FACE, self.FONT_SIZE)

    def _renderContent(self, surface):
        return surface

    def render(self):

        # Figure out the size of the content surface.
        # If we're autosizing, we use the parent surface size to give the content some space to blit on.
        # We'll crop the surface after.
        parentRect = self._parentSurface.get_rect()

        if self.width == SIZE_AUTO:
            contentWidth = parentRect.width
        else:
            contentWidth = self.width

        if self.height == SIZE_AUTO:
            contentHeight = parentRect.height
        else:
            contentHeight = self.height

        # Render the content.
        contentSurface = pygame.Surface((contentWidth, contentHeight), flags=pygame.SRCALPHA)
        self._renderContent(contentSurface)

        # Figure out the size of the full window surface.
        contentRect = contentSurface.get_bounding_rect()
        if self.width == SIZE_AUTO:
            width = contentRect.width + self.HMARGIN * 2
        else:
            width = self.width

        if self.height == SIZE_AUTO:
            height = contentRect.height + self.VMARGIN * 2
        else:
            height = self.height

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

        # Make the surface for the window and fill it
        # Then blit onto the main surface
        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        self.surface.fill((255, 255, 255, 100))
        self.surface.blit(contentSurface, (0,0))
        self._parentSurface.blit(self.surface, (left, top))

