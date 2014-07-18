"""
Seed

"""

import models.CropType as ct
import models.Item as item

# Our main Seed class
class Seed(item.Item):
	def __init__(self, type):
		super().__init__()

		# The constructor. Set up the internal vars.
		cropType = ct.CropType(type)
		self.buyPrice = cropType.seed.buyPrice
		self.sellPrice = cropType.seed.shipPrice
		self.internalName = cropType.seed.internalName
		self.displayName = cropType.seed.displayName


		

