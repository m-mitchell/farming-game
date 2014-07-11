def main():

	# This is a really hacky menu system, but it's 100% temporary so that's OK. 
	while True:
		getUserAction()


def getUserAction():
		# This is the main menu. 
		options = {
			1: ("Visit Field", "field"),
			2: ("Visit Barn", "barn"),
			3: ("Visit Village", "village"),
			4: ("Visit Forest", "forest"),
			5: ("Visit Shop", "shop"),
			6: ("Sleep", "sleep"),
			7: ("Quit", "quit")
		}
		nextAction = displayMenuPrompt(options)

		# Check the user's choice and perform the appropriate action.
		if nextAction == "field":
			return getFieldAction()

		elif nextAction == "barn":
			return getBarnAction()

		elif nextAction == "village":
			return getVillageAction()

		elif nextAction == "forest":
			print("not implemented yet!") # TODO

		elif nextAction == "shop":
			return getShopAction()

		elif nextAction == "sleep":
			print("not implemented yet!") # TODO

		elif nextAction == "quit":
			print("Bye, see you next time!")
			exit(0)

		else:
			return nextAction



def getFieldAction():
		print("You walk out to the field and survey the landscape:")
		print("Plot 1 -- Empty.")
		print("Plot 2 -- Empty.")
		print("Plot 3 -- Empty.")
		print("Plot 4 -- Empty.")

		return "sleep"

def getBarnAction():
	print("This isn't implemented yet!")
	return "sleep"

def getVillageAction():
	print("This isn't implemented yet!")
	return "sleep"

def getShopAction():
	print("This isn't implemented yet!")
	return "sleep"

def displayMenuPrompt(options):
	while True:
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
			(optionDisplayText, optionInternalText) = options[choice]
			print("You picked option %d - %s\n" % (choice, optionDisplayText) )
			return optionInternalText

		else:
			print("Please pick a number from 1 to %d.\n" % len(options) )

if __name__=='__main__':
	main()