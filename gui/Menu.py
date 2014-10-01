import pygame
from gui.BaseWindow import BaseWindow, HALIGN_CENTER, VALIGN_CENTER, SIZE_AUTO
import models.Config as config

class Menu(BaseWindow):
    CURSOR_MARGIN = 5

    def __init__(self, options, surface, width=SIZE_AUTO, height=SIZE_AUTO, halign=HALIGN_CENTER, valign=VALIGN_CENTER):
        self.options = options
        self.cursorIndex = 0


        super(Menu, self).__init__(surface, width, height, halign, valign)

    def _renderContent(self, surface):
        # Render the menu cursor
        renderedText = self.font.render(">", 1, self.FONT_COLOR)
        dest = (self.HMARGIN, self.VMARGIN + self.cursorIndex*self.LINE_HEIGHT)
        surface.blit(renderedText, dest)

        # Render each option.
        leftTextPos = self.HMARGIN + self.CURSOR_MARGIN + renderedText.get_rect().width
        for i, (optionValue, optionText) in enumerate(self.options):
            renderedText = self.font.render(optionText, 1, self.FONT_COLOR)
            dest = (leftTextPos, self.VMARGIN + i*self.LINE_HEIGHT )
            surface.blit(renderedText, dest)

    def setCursor(self, index):
        self.cursorIndex = index

    def moveCursorDown(self):
        self.cursorIndex = (self.cursorIndex+1) % len(self.options)

    def moveCursorUp(self):
        self.cursorIndex = (self.cursorIndex-1) % len(self.options)

    def getCurrentOption(self):
        return self.options[self.cursorIndex][0]