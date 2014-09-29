"""
Field

This class represents a rectangular area filled with Plots.

"""

import models.Plot as plot
import models.GameTime as gt


# Our main Field class
class Field():
    def __init__(self, width, height):
        # The constructor. Set up the internal vars.
        self._crop = None
        self._width = width
        self._height = height

        self._plots = []
        """for i in range(0, width):
            self._plots.append([])
            for j in range(0, height):
                self._plots[i].append(plot.Plot())"""

        # Add an event handler for when the day changes.
        gameTime = gt.GameTime.Instance()
        gameTime.dayChanged.handle(self.onDayChanged)

    def __iter__(self):
        for i in range(0, self._width):
            for j in range(0, self._height):
                yield self._plots[i][j]

    def __len__(self):
        return self._width*self._height

    def __getitem__(self,index):
        width = int(index / self._height)
        height = index % self._width
        return self._plots[width][height]

    def onDayChanged(self):
        # For now we'll keep it simple, just delegate to the plot.
        for plot in self:
            plot.onDayChanged()