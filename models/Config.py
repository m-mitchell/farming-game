"""
Config

This represents the project config.
"""
import os, sys

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, "../../"))

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOB_SIZE = (32, 64)
TILE_SIZE = 32
GUI_TILE_SIZE = 8
TICK_TIME = 25
WALK_TIMER = 7
ANIM_FAST = 5
ANIM_MEDIUM = 7
ANIM_SLOW = 10