"""
Tool

"""

from models.Item import Item

# Our main Tool class
class Tool(Item):
    def __init__(self, internalName):
        super().__init__(internalName)