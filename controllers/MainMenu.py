import pygame
from controllers.BaseController import BaseController
from controllers.Game import Game
from gui.Menu import Menu
import models.Config as config

class MainMenu(BaseController):
    BACKGROUND_COLOR = (128,128,128)

    def __init__(self):
        super().__init__()

        options = [
            ('start', 'Start'),
            ('quit', 'Quit')
        ]
        self.menu = Menu(options, self.background, handler=self.handleMenuSelection)

    def tick(self):
        self.clock.tick(self.TICK_TIME)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            else:
                self.menu.handleEvent(event)


    def handleMenuSelection(self, option):
        if option == 'start':
            self.nextController = Game

        elif option == 'quit':
            self.quit = True


    def run(self):
        while not self.quit and not self.nextController:
            self.tick()

            self.background.fill(self.BACKGROUND_COLOR)
            self.menu.render()
            self.screen.blit(self.background, (0,0))

            pygame.display.flip()

        if not self.quit:
            return self.nextController()

        return None

