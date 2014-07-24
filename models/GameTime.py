"""
GameTime

This is a Singleton class that represents the current in-game time and date.


More info about the Singleton pattern can be found here:
    http://www.oodesign.com/singleton-pattern.html
"""

from util.Singleton import Singleton
from util.Event import Event

# Set up some useful game-time related constants
class Season:
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4

class DayStage:
    MORNING = 1
    AFTERNOON = 2
    NIGHT = 3

# Our main GameTime class
@Singleton
class GameTime:
    def __init__(self):
        # The constructor. Set up the internal vars.
        # We'll prefix private variables with an underscore.
        # The default time is Spring 1 Year 1, 06:00.
        self._year = 1
        self._season = Season.SPRING
        self._day = 1

        self._hour = 6
        self._minute = 0

        # Define some custom events for the game time.
        # Other classes can register event handlers 
        # to "listen" for changes in the game time state.
        # E.g., a Field object would want to know when the day has changed
        # so it can advance the growth state of its plants (among other things).
        self.dayChanged = Event()


    def getFormattedDate(self):
        # Return the date, in the format "Fall 01, Year 13"
        seasonStr = ""
        if self._season == Season.SPRING:
            seasonStr = "Spring"
        elif self._season == Season.SUMMER:
            seasonStr = "Summer"
        elif self._season == Season.FALL:
            seasonStr = "Fall"
        elif self._season == Season.WINTER:
            seasonStr = "Winter"


        return "%s %s, Year %d" % (seasonStr, str(self._day).zfill(2), self._year)

    def getFormattedTime(self):
        # Return the hour (padded to 2 digits) and minute (padded to 2 digits)
        # E.g., 12:00, 23:49, 00:01
        return str(self._hour).zfill(2) + ":" + str(self._minute).zfill(2)

    def getFormattedDateTime(self):
        return self.getFormattedTime() + " " + self.getFormattedDate()

    def getDayStage(self):
        # This can be used for various effects, e.g., sunrise/sunset/nighttime filters. 
        # We'll keep it basic for now but we can make it more fine-grained later if we want.
        if self._hour < 6:
            return DAY_STAGE.NIGHT
        elif self._hour < 11:
            return DAY_STAGE.MORNING
        elif self._hour < 18:
            return DAY_STAGE.AFTERNOON
        else:
            return DAY_STAGE.NIGHT

    def getSeason(self):
        # We can be lazy here and just return the season.
        # If we wanted to replace our season-months with actual months (1-12), we could add some more logic later.
        return self._season


    def advanceDay(self):
        # Increment the current day by 1.
        if self._day < 30:
            # E.g., 17th => 18th
            self._day += 1
        elif self._season < Season.WINTER:
            # E.g., Fall 30th => Winter 1st
            self._day = 1
            self._season += 1
        else:
            # E.g., Winter 30th Year 2 => Spring 1st Year 3
            self._day = 1
            self._season = 1
            self._year += 1

        # Trigger the day changed event.
        self.dayChanged.fire()
