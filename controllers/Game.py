import pygame

from controllers.BaseController import BaseController
from models.PlayerCharacter import getPlayer
from models.Map import Map
from models.Mob import Direction
from gui.Hud import Hud
from gui.Inventory import Inventory
from gui.Menu import Menu

class Game(BaseController):
    BACKGROUND_COLOR = (255,255,255)

    def __init__(self):
        super().__init__()

        self.player = getPlayer()

        self.maps = {}
        self.setMap('test')

        self.hud = Hud(self.background)
        self.inventory = Inventory(self.background)
        self.gui = None

    def tick(self):
        self.clock.tick(self.TICK_TIME)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            elif self.gui:
                self.gui.handleEvent(event)

            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_z):
                    self.player.previousTool()

                elif(event.key == pygame.K_x):
                    self.player.nextTool()

                elif(event.key == pygame.K_c):
                    self.player.unequipTool()

                if(event.key == pygame.K_a):
                    self.player.previousItem()

                elif(event.key == pygame.K_s):
                    self.player.nextItem()

                elif(event.key == pygame.K_d):
                    self.player.unequipItem()

                elif(event.key == pygame.K_LCTRL):
                    self.player.spawnUseTool(self.currentMap)

                elif(event.key == pygame.K_SPACE):
                    self.player.spawnInteract(self.currentMap)

                elif(event.key == pygame.K_ESCAPE):
                    options = [
                        ('quit', 'Quit'),
                        ('cancel', 'Cancel'),
                    ]
                    menu = Menu(options, self.background, escape="cancel", handler=self.handleMenuSelection)
                    self.setGui(menu)

        if self.gui:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.move(self.currentMap, Direction.UP)

        elif keys[pygame.K_RIGHT]:
            self.player.move(self.currentMap, Direction.RIGHT)

        elif keys[pygame.K_LEFT]:
            self.player.move(self.currentMap, Direction.LEFT)

        elif keys[pygame.K_DOWN]:
            self.player.move(self.currentMap, Direction.DOWN)

        self.player.spawnWalkTrigger(self.currentMap)

    def setMap(self, mapName):
        if mapName not in self.maps.keys():
            self.maps[mapName] = Map(self.background, mapName)

        self.currentMap = self.maps[mapName]

    def setGui(self, gui):
        self.gui = gui
        if gui:
            self.gui.setSurface(self.background)

    def run(self):
        while not self.quit and not self.nextController:
            self.tick()

            self.background.fill(self.BACKGROUND_COLOR)
            self.currentMap.render()

            self.hud.render()
            self.inventory.render()

            if self.gui:
                self.gui.render()

            self.screen.blit(self.background, (0,0))


            pygame.display.flip()

        if not self.quit:
            return self.nextController

        return None

    def handleMenuSelection(self, option):
        if option == 'cancel':
            self.setGui(None)

        elif option == 'quit':
            self.quit = True

