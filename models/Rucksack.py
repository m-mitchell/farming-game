"""
Rucksack

This class represents a player character's inventory.

"""


# Our main Rucksack class
class Rucksack(object):
	def __init__(self, size=8):
		# The constructor. Set up the internal vars.
		self._size = size
		self._contents = []

	def add(self, item):
		if self._size == len(self._contents):
			return False

		self._contents.append(item)
		return True

	def remove(self, item):
		self._contents.remove(item)

	def search(self, cls, attrs):
		for item in self._contents:
			if type(item) is cls:
				for attrKey, attrValue in attrs.items():
					if not hasattr(item, attrKey):
						raise Exception("Attr does not exist.")
					if getattr(item,attrKey) == attrValue:
						return item

		return None

	def __iter__(self):
		for item in self._contents:
			yield item

	def __contains__(self, item):
		return item in self._contents

	def __len__(self):
		return len(self._contents)

	def __str__(self):
		resultList = []
		for item in self._contents:
			resultList.append(item.displayName)
		return ", ".join(resultList)