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
        self.load_map()


    def render(self):
        temp = pygame.Surface(self.size)
        if self._bgColor:
            temp.fill(self._bgColor)

        for layer in self._layers:
            temp = layer.render(temp)

        self._objects.update()
        self._objects.draw(temp)

        self._surface.blit(temp, (0,0))

    def is_walkable(self, x, y):
        # Prevent walking off the map edge.
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return False

        walkable = True
        for layer in self._layers:
            walkable = walkable and layer.is_walkable(x, y)
        return walkable

    def interact(self, held_item, x, y):
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return

        rect = pygame.Rect(x*config.TILE_SIZE, y*config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE)
        for obj in self._objects.sprites():
            if obj.rect.colliderect(rect):
                obj.interact(held_item)
                break

    def use_tool(self, tool, x, y):
        if x < 0 or y < 0 or x == self.width or y == self.height:
            return

        rect = pygame.Rect(x*config.TILE_SIZE, y*config.TILE_SIZE, config.TILE_SIZE, config.TILE_SIZE)
        for obj in self._objects.sprites():
            if obj.rect.colliderect(rect):
                obj.use_tool(tool)
                break

    def load_map(self):
        tmx_data = load_pygame(self._filename)

        self.size = tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight
        self.width = tmx_data.width
        self.height = tmx_data.height
        self.tileSize = tmx_data.tilewidth

        if tmx_data.background_color:
            self._bgColor = tmx_data.background_color

        # iterate over all the visible layers and create a map layer for each.
        for layer in tmx_data.visible_layers:
            if isinstance(layer, TiledTileLayer):
                self._layers.append(TileLayer(tmx_data, layer))

            elif isinstance(layer, TiledObjectGroup):
                obj_factory = ObjectFactory(tmx_data)
                for obj in layer:
                    sprite = obj_factory.construct(obj)
                    self._objects.add(sprite)

class ObjectFactory(object):
    def __init__(self, tmx_data):
        pass

    def construct(self, tmx_obj):
        kwargs = {}
        module = importlib.import_module("models.%s"%tmx_obj.type)
        cls = getattr(module, tmx_obj.type)
        obj = cls((tmx_obj.x/config.TILE_SIZE, tmx_obj.y/config.TILE_SIZE + 1), **kwargs)

        return obj

class TileLayer(object):
    def __init__(self, tmx_data, tmx_layer):
        self._name = tmx_layer.name
        self._tiles = {}
        self._height = tmx_data.height
        self._width = tmx_data.width
        self._tilewidth = tmx_data.tilewidth
        self._tileheight = tmx_data.tileheight

        for x, y, gid in tmx_layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
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

    def is_walkable(self, x, y):
        if self._name != 'collision':
            return True
        
        row = self._tiles.get(x, {})
        if row.get(y, False):
            return False

        return True
