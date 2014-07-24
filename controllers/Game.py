import pygame

from controllers.BaseController import BaseController
from models.PlayerCharacter import PlayerCharacter
from models.Map import Map
from gui.Hud import Hud

class Game(BaseController):
    BACKGROUND_COLOR = (255,255,255)

    def __init__(self):
        super().__init__()

        self.player = PlayerCharacter()
        self.currentMap = Map(self.background, 'test')
        self.spriteList = pygame.sprite.RenderPlain([self.player])
        self.hud = Hud(self.background, self.player)

    def tick(self):
        self.clock.tick(self.TICK_TIME)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_LEFT):
                    self.player.moveLeft()

                elif(event.key == pygame.K_UP):
                    self.player.moveUp()

                elif(event.key == pygame.K_RIGHT):
                    self.player.moveRight()

                elif(event.key == pygame.K_DOWN):
                    self.player.moveDown()

                elif(event.key == pygame.K_z):
                    self.player.previousTool()

                elif(event.key == pygame.K_x):
                    self.player.nextTool()

                elif(event.key == pygame.K_c):
                    self.player.unequipTool()


    def run(self):
        while not self.quit and not self.nextController:
            self.tick()

            self.background.fill(self.BACKGROUND_COLOR)
            self.currentMap.render()

            self.spriteList.update()
            self.spriteList.draw(self.background)

            self.hud.render()
            self.screen.blit(self.background, (0,0))

            pygame.display.flip()

        if not self.quit:
            return self.nextController

        return None

