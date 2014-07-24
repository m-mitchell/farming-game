"""
PlayerCharacter

"""
from models.Rucksack import Rucksack
from models.Seed import Seed
from models.Tool import Tool
from models.Mob import Mob

# Our main PlayerCharacter class
class PlayerCharacter(Mob):
    def __init__(self):
        # The constructor. Set up the internal vars.
        super(PlayerCharacter, self).__init__("player")

        self.rucksack = Rucksack()
        self.money = 100
        self.currentTool = None

        self.rucksack.add(Tool("wateringCan"))
        self.rucksack.add(Tool("hoe"))
        self.rucksack.add(Seed("strawberrySeed"))
        self.rucksack.add(Seed("strawberrySeed"))
        self.rucksack.add(Seed("turnipSeed"))
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
