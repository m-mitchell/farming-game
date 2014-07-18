"""
Item

This is an abstract class that provides some common functionality for all items
(e.g., crops, jewelry, seeds, ...)

"""

from abc import ABCMeta

# Our main Item class
class Item(metaclass=ABCMeta):
	def __init__(self):
		# The constructor. Set up the internal vars.
		self.internalName = None
		self.displayName = None


	def __str__(self):
		return self.displayName


	
