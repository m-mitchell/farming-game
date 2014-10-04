import pygame
from gui.BaseWindow import BaseWindow, HALIGN_CENTER, VALIGN_CENTER, SIZE_AUTO
import models.Config as config
from util.Event import Event

class Menu(BaseWindow):
    CURSOR_MARGIN = 5

    def __init__(self, options, surface, width=SIZE_AUTO, height=SIZE_AUTO, halign=HALIGN_CENTER, valign=VALIGN_CENTER, escape=None, text=None):
        self.options = options
        self.escape = escape
        self.cursorIndex = 0
        self.optionSelected = Event()
        self.text = text

        super(Menu, self).__init__(surface, width, height, halign, valign)

    def _renderContent(self, surface):
        # Render the text (if any)
        lines = []
        if self.text:
            lines = [self.text] # TODO split long lines into multiple
            for i, line in enumerate(lines):
                renderedText = self.font.render(line, 1, self.FONT_COLOR)
                dest = (self.HMARGIN, self.VMARGIN + i*self.LINE_HEIGHT )
                surface.blit(renderedText, dest)

        # Render the menu cursor
        renderedText = self.font.render(">", 1, self.FONT_COLOR)
        dest = (self.HMARGIN, self.VMARGIN + (len(lines) + self.cursorIndex)*self.LINE_HEIGHT)
        surface.blit(renderedText, dest)

        # Render each option.
        leftTextPos = self.HMARGIN + self.CURSOR_MARGIN + renderedText.get_rect().width
        for i, (optionValue, optionText) in enumerate(self.options):
            renderedText = self.font.render(optionText, 1, self.FONT_COLOR)
            dest = (leftTextPos, self.VMARGIN + (len(lines) + i)*self.LINE_HEIGHT )
            surface.blit(renderedText, dest)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_DOWN):
                self.moveCursorDown()

            elif(event.key == pygame.K_UP):
                self.moveCursorUp()

            elif(event.key in [pygame.K_RETURN, pygame.K_SPACE]):
                self.optionSelected.fire(self.getCurrentOption())

            elif(event.key == pygame.K_ESCAPE):
                if self.escape:
                    self.optionSelected.fire(self.escape)

    def setCursor(self, index):
        self.cursorIndex = index

    def moveCursorDown(self):
        self.cursorIndex = (self.cursorIndex+1) % len(self.options)

    def moveCursorUp(self):
        self.cursorIndex = (self.cursorIndex-1) % len(self.options)

    def getCurrentOption(self):
        return self.options[self.cursorIndex][0]