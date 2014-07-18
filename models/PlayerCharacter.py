"""
PlayerCharacter

"""

from models.Rucksack import Rucksack

# Our main PlayerCharacter class
class PlayerCharacter(object):
	def __init__(self):
		# The constructor. Set up the internal vars.
		self.rucksack = Rucksack()
		self.money = 100