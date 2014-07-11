"""
Plot

This class represents a single tile on a field. 

"""

import models.CropType as ct

# Our main Plot class
class Plot:
	def __init__(self):
		# The constructor. Set up the internal vars.
		self._crop = None
		self._growthTime = None
		self._watered = False


	def water(self):
		self._watered = True

	def clear(self):
		self._crop = None
		self._growthTime = None

	def getCropString(self):
		# Return a user-readable string describing the plot's contents
		if self._crop:
			watered = ""
			if self._watered:
				watered = "[WATERED]"

			return "%s (growth: %d) %s" % (self._crop.displayName, self._growthTime, watered)
		else:
			return "Empty"

	def plant(self, type):
		self._crop = ct.CropType(type)
		self._growthTime = 0