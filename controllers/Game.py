import pygame
from controllers.BaseController import BaseController

class Game(BaseController):
	BACKGROUND_COLOR = (255,255,255)

	def __init__(self):
		super().__init__()

	def tick(self):
		self.clock.tick(self.TICK_TIME)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit = True

			elif event.type == pygame.KEYDOWN:
				if(event.key == pygame.K_DOWN):
					pass

				elif(event.key == pygame.K_UP):
					pass


	def run(self):
		while not self.quit and not self.nextController:
			self.tick()

			self.background.fill(self.BACKGROUND_COLOR)
			self.screen.blit(self.background, (0,0))

			pygame.display.flip()

		if not self.quit:
			return self.nextController

		return None

