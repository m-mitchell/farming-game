"""
PlayerCharacter

"""
from models.Rucksack import Rucksack
from models.Seed import Seed
from models.Tool import Tool
from models.Mob import Mob, Direction

def getPlayer():
    global __current
    return __current

def setPlayer(player):
    global __current
    __current = player

# Our main PlayerCharacter class
class PlayerCharacter(Mob):
    def __init__(self, pos=(0,0)):
        # The constructor. Set up the internal vars.
        super(PlayerCharacter, self).__init__("player", pos=pos)

        self.rucksack = Rucksack(self)
        self.money = 100
        self.currentTool = None
        self.currentItem = None

        self.rucksack.add(Tool("wateringCan"))
        self.rucksack.add(Tool("hoe"))
        self.rucksack.add(Seed("watermelonSeed"))
        self.rucksack.add(Seed("strawberrySeed"))
        self.rucksack.add(Seed("potatoSeed"))
        self.rucksack.add(Seed("turnipSeed"))

    def nextTool(self):
        tools = []
        currToolIndex = -1
        for i, item in enumerate(self.rucksack):
            if type(item) is Seed or type(item) is Tool:
                tools.append(item)
                
            if item is self.currentTool:
                currToolIndex = i

        if len(tools):
            self.currentTool = tools[(currToolIndex+1) % len(tools)]

    def previousTool(self):
        tools = []
        currToolIndex = -1
        for i, item in enumerate(self.rucksack):
            if type(item) is Seed or type(item) is Tool:
                tools.append(item)
                
            if item is self.currentTool:
                currToolIndex = i

        if len(tools):
            self.currentTool = tools[(currToolIndex-1) % len(tools)]

    def unequipTool(self):
        self.currentTool = None

    def equipTool(self, item):
        if not item in self.rucksack:
            return

        if type(item) is Seed or type(item) is Tool:
            self.currentTool = item

    def nextItem(self):
        inv = []
        currItemIndex = -1
        for i, item in enumerate(self.rucksack):
            if type(item) is not Seed and type(item) is not Tool:
                inv.append(item)
                
            if item is self.currentItem:
                currItemIndex = i

        if len(inv):
            self.currentItem = inv[(currItemIndex+1) % len(inv)]

    def previousItem(self):
        inv = []
        currItemIndex = -1
        for i, item in enumerate(self.rucksack):
            if type(item) is not Seed and type(item) is not Tool:
                inv.append(item)
                
            if item is self.currentItem:
                currItemIndex = i

        if len(inv):
            self.currentItem = inv[(currItemIndex-1) % len(inv)]

    def unequipItem(self):
        self.currentItem = None

    def spawnInteract(self, map):
        targetPos = self._getCoordinates(self.pos, self._direction)
        map.interact(self.currentItem, *targetPos)

    def spawnUseTool(self, map):
        targetPos = self._getCoordinates(self.pos, self._direction)

        if self.currentTool:
            map.useTool(self.currentTool, *targetPos)

    def spawnWalkTrigger(self, map):
        map.walkTrigger(*self.pos)
