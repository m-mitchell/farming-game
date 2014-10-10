import pygame
from math import floor

from models.GameTime import GameTime
from models.PlayerCharacter import getPlayer
import models.Config as config

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

    def __init__(self, surface=None, width=SIZE_AUTO, height=SIZE_AUTO, halign=HALIGN_LEFT, valign=VALIGN_TOP, image="default"):
        self._parentSurface = surface
        self.width = width
        self.height = height
        self.halign = halign
        self.valign = valign
        self._contentHeight = 0
        self._contentWidth = 0

        filename = r'%s\media\images\gui\%s.png' % (config.PROJECT_ROOT, image)
        self._spritesheet = pygame.image.load(filename)
        self._loadTiles()

        self.font = pygame.font.Font(self.FONT_FACE, self.FONT_SIZE)


    def _loadTiles(self):
        # Figure out the height and width of the sheet (in sprites)
        spritesheetRect = self._spritesheet.get_rect()
        sheetWidthInTiles = floor(spritesheetRect.width / config.GUI_TILE_SIZE)
        sheetHeightInTiles = floor(spritesheetRect.height / config.GUI_TILE_SIZE)

        self._tiles = []
        for y in range(0, sheetHeightInTiles):
            row = []
            for x in range(0, sheetWidthInTiles):
                rect = pygame.Rect(x*config.GUI_TILE_SIZE, y*config.GUI_TILE_SIZE, config.GUI_TILE_SIZE, config.GUI_TILE_SIZE)
                sprite = self._spritesheet.subsurface(rect)
                row.append(sprite)
            self._tiles.append(row)

    def _renderContent(self, surface):
        return surface

    def setSurface(self, surface):
        self._parentSurface = surface

    def handleEvent(self, event):
        pass

    def render(self):
        if not self._parentSurface:
            return 

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

        # Snap the window size so it's evenly divisible by the tile size.
        # This lets us make tileable (patterned) window gfx and still have them be pretty ^o^
        if width % config.GUI_TILE_SIZE != 0:
            width = (int(width/config.GUI_TILE_SIZE) + 1) * config.GUI_TILE_SIZE

        if height % config.GUI_TILE_SIZE != 0:
            height = (int(height/config.GUI_TILE_SIZE) + 1) * config.GUI_TILE_SIZE

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

        # Make the surface for the window and draw the window area on it. 
        self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)

        # Top-left corner
        self.surface.blit(self._tiles[0][0], (0, 0))

        # Top-right corner
        self.surface.blit(self._tiles[0][2], (width-config.GUI_TILE_SIZE, 0))

        # Bottom-left corner
        self.surface.blit(self._tiles[2][0], (0, height-config.GUI_TILE_SIZE))

        # Bottom-right corner
        self.surface.blit(self._tiles[2][2], (width-config.GUI_TILE_SIZE, height-config.GUI_TILE_SIZE))

        # Top edge
        for i in range(1, int(width/config.GUI_TILE_SIZE)-1):
            self.surface.blit(self._tiles[0][1], (config.GUI_TILE_SIZE*i, 0))

        # Bottom edge
        for i in range(1, int(width/config.GUI_TILE_SIZE)-1):
            self.surface.blit(self._tiles[2][1], (config.GUI_TILE_SIZE*i, height-config.GUI_TILE_SIZE))

        # Left edge
        for i in range(1, int(height/config.GUI_TILE_SIZE)-1):
            self.surface.blit(self._tiles[1][0], (0, config.GUI_TILE_SIZE*i))

        # Right edge
        for i in range(1, int(height/config.GUI_TILE_SIZE)-1):
            self.surface.blit(self._tiles[1][2], (width-config.GUI_TILE_SIZE, config.GUI_TILE_SIZE*i))

        # THE MIDDLE BIT!
        for i in range(1, int(width/config.GUI_TILE_SIZE)-1):
            for j in range(1, int(height/config.GUI_TILE_SIZE)-1):
                self.surface.blit(self._tiles[1][1], (config.GUI_TILE_SIZE*i, config.GUI_TILE_SIZE*j))

        # Add the content surface, then blit onto the main surface
        self.surface.blit(contentSurface, (0, 0))
        self._parentSurface.blit(self.surface, (left, top))

