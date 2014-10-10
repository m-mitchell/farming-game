import pygame
from gui.BaseWindow import BaseWindow, HALIGN_CENTER, VALIGN_BOTTOM, SIZE_AUTO
import models.Config as config
from util.Event import Event
from controllers.BaseController import getController

class MessageBox(BaseWindow):

    def __init__(self, text, surface=None, halign=HALIGN_CENTER, valign=VALIGN_BOTTOM, handler=None):
        self.text = text
        self.done = Event()

        super(MessageBox, self).__init__(surface, halign=halign, valign=valign, width=config.SCREEN_WIDTH)

        if handler == None:
            handler = self._defaultHandler

        self.done.handle(handler)

    def _renderContent(self, surface):
        # Render the text (if any)
        lines = []
        if self.text:
            lines = [self.text] # TODO split long lines into multiple
            for i, line in enumerate(lines):
                renderedText = self.font.render(line, 1, self.FONT_COLOR)
                dest = (self.HMARGIN, self.VMARGIN + i*self.LINE_HEIGHT )
                surface.blit(renderedText, dest)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if(event.key in [pygame.K_RETURN, pygame.K_SPACE]):
                self.done.fire()

    def _defaultHandler(self):
        getController().setGui(None)