import pygame
from gui.BaseWindow import BaseWindow, HALIGN_CENTER, VALIGN_CENTER
import models.Config as config

DEFAULT_HEIGHT = config.SCREEN_HEIGHT
DEFAULT_WIDTH = config.SCREEN_WIDTH / 5

class Menu(BaseWindow):

    def __init__(self, options, surface, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, halign=HALIGN_CENTER, valign=VALIGN_CENTER):
        self.options = options
        self.cursorIndex = 0


        super(Menu, self).__init__(surface, width, height, halign, valign)

    def _renderContent(self):
        # Render the menu cursor
        renderedText = self.font.render(">", 1, self.FONT_COLOR)
        dest = (self.MARGIN, self.MARGIN + self.cursorIndex*self.LINE_HEIGHT)
        self.surface.blit(renderedText, dest)

        # Render each option.
        leftTextPos = self.MARGIN*2 + renderedText.get_rect().width
        for i, (optionValue, optionText) in enumerate(self.options):
            renderedText = self.font.render(optionText, 1, self.FONT_COLOR)
            dest = (leftTextPos, self.MARGIN + i*self.LINE_HEIGHT )
            self.surface.blit(renderedText, dest)

    def setCursor(self, index):
        self.cursorIndex = index

    def moveCursorDown(self):
        self.cursorIndex = (self.cursorIndex+1) % len(self.options)

    def moveCursorUp(self):
        self.cursorIndex = (self.cursorIndex-1) % len(self.options)

    def getCurrentOption(self):
        return self.options[self.cursorIndex][0]