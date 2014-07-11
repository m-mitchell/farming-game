def main():

	# This is a really hacky menu system, but it's 100% temporary so that's OK. 
	while True:
		nextAction = getUserAction()
		print("You chose to do action %s" % nextAction)



def getUserAction():
		options = {
			1: ("Visit Field", "field", False),
			2: ("Visit Barn", "barn", False),
			3: ("Visit Village", "village", False),
			4: ("Visit Forest", "forest", True),
			5: ("Visit Shop", "shop", True),
			6: ("Sleep", "sleep", True),
			7: ("Quit", "quit", True)
		}
		return displayMenuPrompt(options)


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
			(optionDisplayText, optionInternalText, optionIsFinal) = options[choice]
			print("You picked option %d - %s\n" % (choice, optionDisplayText) )
			return optionInternalText

		else:
			print("Please pick a number from 1 to %d.\n" % len(options) )

if __name__=='__main__':
	main()