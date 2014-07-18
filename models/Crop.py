"""
Crop

"""

from models.Item import Item
from models.CropType import CropType

# Our main Crop class
class Crop(Item):
	def __init__(self, type):
		super().__init__()

		# The constructor. Set up the internal vars.
		cropType = CropType(type)
		self.internalName = cropType.internalName
		self.displayName = cropType.displayName

		#self.buyPrice = cropType.buyPrice
		#self.sellPrice = cropType.sellPrice


		

