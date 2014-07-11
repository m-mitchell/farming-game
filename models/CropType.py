"""
CropType

This class represents a type of crop, e.g., "turnip". It doesn't represent an actual turnip item, just the concept of turnipness. :) 

"""

import json

import models.Config as config
import models.GameTime as gt

# Set up some useful constants
class GrowSpeed:
	FAST = 2
	NORMAL = 1
	SLOW = 0.5
	NONE = 0


# Our main CropType class.
class CropType():
	def __init__(self, type):
		# Use the provided type string to find the JSON file with the crop data in it. 
		jsonFile = r'%s\data\crops\%s.json' % (config.PROJECT_ROOT, type)

		with open(jsonFile) as dataFile:    
			data = json.load(dataFile)
			
			self.internalName = data['internalName']
			self.displayName = data['displayName']
			self.growTime = int(data['growTime'])
			self.regrows = bool(data['regrows'])
			self.shipPrice = int(data['shipPrice'])
			self.buyPrice = int(data['buyPrice'])

			self.seasons = {}
			for season, speed in data['seasons'].items():
				parsedSeason = getattr(gt.Season, season.upper())
				parsedSpeed = getattr(GrowSpeed, speed.upper())
				self.seasons[parsedSeason] = parsedSpeed
