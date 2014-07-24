"""
Map

"""

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
        self._renderer = None
        self._running = False
        self._dirty = False
        self._filename = r'%s\data\maps\%s.tmx' % (config.PROJECT_ROOT, internalName)
        self.load_map()

    def render(self):
        temp = pygame.Surface(self._renderer.size)
        self._renderer.render(temp)
        #pygame.transform.smoothscale(temp, self._surface.get_size(), self._surface)
        self._surface.blit(temp, (0,0))

    def load_map(self):
        self._renderer = TiledRenderer(self._filename)

        print("Objects in map:")
        for o in self._renderer.tmx_data.objects:
            print(o)
            for k, v in o.properties.items():
                print("  ", k, v)

        print("GID (tile) properties:")
        for k, v in self._renderer.tmx_data.tile_properties.items():
            print("  ", k, v)

class TiledRenderer(object):
    """
    Super simple way to render a tiled map
    """
    def __init__(self, filename):
        tm = load_pygame(filename)
        self.size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm

    def render(self, surface):
        # not going for efficiency here
        # for demonstration purposes only

        # deref these heavily used variables for speed
        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        gt = self.tmx_data.get_tile_image_by_gid
        surface_blit = surface.blit

        # fill the background color
        if self.tmx_data.background_color:
            surface.fill(self.tmx_data.background_color)

        # iterate over all the visible layers, then draw them
        # according to the type of layer they are.
        for layer in self.tmx_data.visible_layers:

            # draw map tile layers
            if isinstance(layer, TiledTileLayer):
                for x, y, gid in layer:
                    tile = gt(gid)
                    if tile:
                        surface_blit(tile, (x * tw, y * th))

            # draw objects
            elif isinstance(layer, TiledObjectGroup):
                for o in layer:
                    print(o)

                    # objects with points are polygons or lines
                    if hasattr(o, 'points'):
                        pygame.draw.lines(surface, (0, 255, 0),
                                          o.closed, o.points, 3)

                    # if the object has a gid, then use a tile image to draw
                    elif o.gid:
                        tile = gt(o.gid)
                        if tile:
                            surface_blit(tile, (o.x, o.y))

                    # draw a rect for everything else
                    else:
                        pygame.draw.rect(surface, (255, 0, 0),
                                         (o.x, o.y, o.width, o.height), 3)

            # draw image layers
            elif isinstance(layer, TiledImageLayer):
                image = gt(layer.gid)
                if image:
                    surface.blit(image, (0, 0))