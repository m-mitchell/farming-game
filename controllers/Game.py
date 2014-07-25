import pygame

from controllers.BaseController import BaseController
from models.PlayerCharacter import PlayerCharacter
from models.Map import Map
from models.Mob import Direction
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
                if(event.key == pygame.K_z):
                    self.player.previousTool()

                elif(event.key == pygame.K_x):
                    self.player.nextTool()

                elif(event.key == pygame.K_c):
                    self.player.unequipTool()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(Direction.UP)

        elif keys[pygame.K_RIGHT]:
            self.player.move(Direction.RIGHT)

        elif keys[pygame.K_LEFT]:
            self.player.move(Direction.LEFT)

        elif keys[pygame.K_DOWN]:
            self.player.move(Direction.DOWN)




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

