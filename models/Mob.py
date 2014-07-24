"""
Mob

"""
import pygame
import models.Config as config

class Mob(pygame.sprite.Sprite):
    def __init__(self, sprite, pos=(100,100)):
        super(Mob, self).__init__()

        filename = r'%s\media\images\mobs\%s.png' % (config.PROJECT_ROOT, sprite)
        self._sprites = [pygame.image.load(filename)]
        self.image = self._sprites[0]
        
        self.pos = pos
        self.rect = self.image.get_rect()

    def moveUp(self):
        #self.pos = (self.pos[0], self.pos[1]-32)
        self.rect = self.rect.move(0, -32)

    def moveRight(self):
        #self.pos = (self.pos[0]+32, self.pos[1])
        self.rect = self.rect.move(32, 0)

    def moveLeft(self):
        #self.pos = (self.pos[0]-32, self.pos[1])
        self.rect = self.rect.move(-32, 0)

    def moveDown(self):
        #self.pos = (self.pos[0], self.pos[1]+32)
        self.rect = self.rect.move(0, 32)