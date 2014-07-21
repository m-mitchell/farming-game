import pygame

class Menu(object):
	FONT_SIZE = 18
	FONT_FACE = None
	FONT_COLOR = (10,10,10)
	LINE_HEIGHT = FONT_SIZE * 1.2
	MARGIN = 10

	def __init__(self, options, surface):
		self.options = options
		self.surface = surface
		self.font = pygame.font.Font(self.FONT_FACE, self.FONT_SIZE)
		self.cursorIndex = 0

	def render(self):
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