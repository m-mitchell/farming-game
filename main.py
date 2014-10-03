import pygame, time

import models.Config as config

import models.GameTime as gt
import models.Plot as plot
import models.Seed as seed
import models.Crop as crop

from models.PlayerCharacter import PlayerCharacter, setPlayer
from controllers.MainMenu import MainMenu
from controllers.BaseController import getController, setController


def main():
    pygame.init()
    pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Farming Game")

    player = PlayerCharacter(pos=(2,2))
    setPlayer(player)

    controller = setController(MainMenu())
    while controller:
        controller = controller.run()
        setController(controller)


if __name__=='__main__':
    main()
