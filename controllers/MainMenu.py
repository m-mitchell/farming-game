import pygame
from controllers.BaseController import BaseController
from controllers.Game import Game
from gui.Menu import Menu

class MainMenu(BaseController):
    BACKGROUND_COLOR = (128,128,128)

    def __init__(self):
        super().__init__()

        options = [
            ('start', 'Start'),
            ('quit', 'Quit')
        ]
        self.menu = Menu(options, self.background)

    def tick(self):
        self.clock.tick(self.TICK_TIME)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_DOWN):
                    self.menu.moveCursorDown()

                elif(event.key == pygame.K_UP):
                    self.menu.moveCursorUp()

                elif(event.key == pygame.K_RETURN):
                    self.handleMenuSelection(self.menu.getCurrentOption())


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
            return self.nextController

        return None

