import models.GameTime as gt
import models.Plot as plot
import models.Field as field



# Set up some global vars for persistence while we test.
money = 100
field = field.Field(4,4)

def main():
	# This is a really hacky menu system, but it's 100% temporary so that's OK. 
	gameTime = gt.GameTime.Instance()
	print("Today's date is " + gameTime.getFormattedDateTime())

	runMainMenu()


def runMainMenu():
	while True:
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
			runFieldMenu()

		elif nextAction == "barn":
			runBarnMenu()

		elif nextAction == "village":
			runVillageMenu()

		elif nextAction == "forest":
			print("not implemented yet!") # TODO

		elif nextAction == "shop":
			runShopMenu()

		elif nextAction == "sleep":
			# The user wants to sleep. Set the clock to the next day at 6am.
			gameTime = gt.GameTime.Instance()
			gameTime.advanceDay()

		elif nextAction == "quit":
			# The user wants to quit the game.
			print("Bye, see you next time!")
			exit(0)



def runFieldMenu():
	while True:
		print("You walk out to the field and survey the landscape:")
		for i, plot in enumerate(field):
			print("Plot %d -- %s" % (i, plot.getCropString()))

		print("")

		# Show the crop submenu
		options = {
			1: ("Plant Turnips", "turnip"),
			2: ("Plant Strawberries", "strawberry"),
			3: ("Water Plot", "water"),
			4: ("Clear Plot", "clear"),
			5: ("Back To Farm", "back")
		}
		nextAction = displayMenuPrompt(options)

		if nextAction == "back":
			return

		elif nextAction == "turnip":
			plot = displayPlotPrompt()
			plot.plant("turnip")

		elif nextAction == "strawberry":
			plot = displayPlotPrompt()
			plot.plant("strawberry")

		elif nextAction == "water":
			plot = displayPlotPrompt()
			plot.water()

		elif nextAction == "clear":
			plot = displayPlotPrompt()
			plot.clear()

def runBarnMenu():
	print("This isn't implemented yet!")
	return "sleep"

def runVillageMenu():
	print("This isn't implemented yet!")
	return "sleep"

def runShopMenu():
	print("This isn't implemented yet!")
	return "sleep"

def displayPlotPrompt():
	while True:
		maxOption = len(field) - 1

		# Prompt the user to pick an option
		print("Please choose a plot [0 to %d]." % maxOption)

		choice = input(">")

		# Check the user's input. It should be a number.
		if not choice.isdigit():
			print("Please pick a number from 0 to %d.\n" % maxOption )
			continue

		# Now check that the number is in the valid range.
		choice = int(choice)
		if choice >= 0 and choice <= maxOption :
			return field[choice]

		else:
			print("Please pick a number from 0 to %d.\n" % maxOption )

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