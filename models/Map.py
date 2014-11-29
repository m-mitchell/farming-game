"""
Map

"""
import importlib

import pygame
from pygame.locals import *
from pytmx import *
from pytmx.tmxloader import load_pygame
import os
import models.Config as config
from models.PlayerCharacter import getPlayer

class Map(object):
    def __init__(self, surface, internalName):
        self._internalName = internalName
        self._surface = surface
        self._loader = None
        self._running = False
        self._dirty = False
        self._filename = r'%s\data\maps\%s.tmx' % (config.PROJECT_ROOT, internalName)
        self._bgColor = None
        self._layers = []
        self._objects = pygame.sprite.RenderPlain()
        self._mobs = pygame.sprite.RenderPlain([getPlayer(),])
        self.loadMap()


    def render(self):
        temp = pygame.Surface(self.size)
        if self._bgColor:
            temp.fill(self._bgColor)

        for layer in self._layers:
            if layer._name != 'overhead':
                temp = layer.render(temp)

        self._objects.update()
        self._objects.draw(temp)

        self._mobs.update()
        self._mobs.draw(temp)

        for layer in self._layers:
            if layer._name == 'overhead':
                temp = layer.render(temp)

        self._surface.blit(temp, (0,0))

    def isWalkable(self, x, y):
        # Prevent walking off the map edge.
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return False

        walkable = True
        for layer in self._layers:
            walkable = walkable and layer.isWalkable(x, y)

        rect = pygame.Rect(x*config.TILE_SIZE, y*config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE)
        for obj in self._objects.sprites():
            if obj.collision and obj.rect.colliderect(rect):
               walkable = False
               break

        return walkable

    def walkTrigger(self, x, y):
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return

        rect = pygame.Rect(x*config.TILE_SIZE, y*config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE)
        for obj in self._objects.sprites():
            if obj.rect.colliderect(rect):
                obj.walkTrigger()
                break

    def interact(self, heldItem, x, y):
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return

        rect = pygame.Rect(x*config.TILE_SIZE, y*config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE)
        for obj in self._objects.sprites():
            if obj.rect.colliderect(rect):
                obj.interact(heldItem)
                break

    def useTool(self, tool, x, y):
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return

        rect = pygame.Rect(x*config.TILE_SIZE, y*config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE)
        for obj in self._objects.sprites():
            if obj.rect.colliderect(rect):
                obj.useTool(tool)
                break

    def loadMap(self):
        tmxData = load_pygame(self._filename)

        self.size = tmxData.width * tmxData.tilewidth, tmxData.height * tmxData.tileheight
        self.width = tmxData.width
        self.height = tmxData.height
        self.tileSize = tmxData.tilewidth

        if tmxData.background_color:
            self._bgColor = tmxData.background_color

        # iterate over all the visible layers and create a map layer for each.
        for layer in tmxData.visible_layers:
            if isinstance(layer, TiledTileLayer):
                self._layers.append(TileLayer(tmxData, layer))

            elif isinstance(layer, TiledObjectGroup):
                objFactory = ObjectFactory(tmxData)
                for obj in layer:
                    sprite = objFactory.construct(obj)
                    self._objects.add(sprite)

class ObjectFactory(object):
    def __init__(self, tmxData):
        pass

    def construct(self, tmxObj):
        module = importlib.import_module("models.%s"%tmxObj.type)
        cls = getattr(module, tmxObj.type)
        xPos = tmxObj.x/config.TILE_SIZE
        yPos = (tmxObj.y + tmxObj.height) / config.TILE_SIZE - 1
        obj = cls((xPos, yPos), **tmxObj.properties)

        return obj

class TileLayer(object):
    def __init__(self, tmxData, tmxLayer):
        self._name = tmxLayer.name
        self._tiles = {}
        self._height = tmxData.height
        self._width = tmxData.width
        self._tilewidth = tmxData.tilewidth
        self._tileheight = tmxData.tileheight

        for x, y, gid in tmxLayer:
            tile = tmxData.get_tile_image_by_gid(gid)
            if tile:
                if x not in self._tiles.keys():
                    self._tiles[x] = {}
                self._tiles[x][y] = tile

    def __str__(self):
        return self._name

    def render(self, surface):
        for x, row in self._tiles.items():
            for y, tile in row.items():
                surface.blit(tile, (x * self._tilewidth, y * self._tileheight))
        return surface

    def isWalkable(self, x, y):
        if self._name != 'collision':
            return True
        
        row = self._tiles.get(x, {})
        if row.get(y, False):
            return False

        return True
