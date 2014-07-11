def main():

	while True:
		nextAction = getUserAction()


def getUserAction():
	# This is a really hacky menu system, but it's 100% temporary so that's OK. 
	currentSubMenu = None

	# Loop until we reach a final action (end of tree).
	while True:

		# Depending on the current submenu, figure out the list of available options.
		# Each option has a number (the user enters it to pick that option),
		# a display text ("Visit Field"), an internal text ("field") 
		# and whether the option is the final option in the branch (True/False).
		if currentSubMenu == None:
			# The user isn't in a submenu so show the top-level menu
			options = {
				1: ("Visit Field", "field", False),
				2: ("Visit Barn", "barn", False),
				3: ("Visit Village", "village", False),
				4: ("Visit Forest", "forest", True),
				5: ("Visit Shop", "shop", False),
				6: ("Sleep", "sleep", True),
				7: ("Quit", "quit", True)
			}

		else:
			raise Exception("Unknown submenu id `%s`." % currentSubMenu) 


		# Prompt the user to pick an option
		print("What do you want to do next?")
		for num, item in options.items():
			print(str(num) + " - "+item[0])

		choice = input(">")

		# Check the user's input. It should be a number.
		if not choice.isdigit():
			print("Please pick a number from 1 to %d.\n" % len(options) )
			continue

		# Now check that the number is in the valid range.
		choice = int(choice)
		if choice > 0 and choice <= len(options) :
			print("You picked option %d - %s\n" % (choice, options[choice][0]) )
		else:
			print("Please pick a number from 1 to %d.\n" % len(options) )

if __name__=='__main__':
	main()