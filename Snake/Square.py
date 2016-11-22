#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     22/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Square:
    """A class to simulate a sqaure on a snakes and ladders board
    Requires parameters for position, categiry, start and end."""


    def __init__(self, pos, cat, end):
        """A constructor method fir a snakes and ladders square
        >>>Sqaure(pos, cat, end)"""
        self.position = pos
        self.cat = cat
        self.end = end

    def setCat(self, newval):
        """Resets the category of the sqaure to be a ladder or a snake.
        >>> setCat("Ladder")
        NoneType"""
        self.cat = newval


    def setEnd(self, newval):


    def toString(self):
        """Return all values as one big string.
        >>>toString()
        'square 57 is a snake square. Slide down to 50'"""
        info = "Sqaure number " + str(self.position) + " is a " + self.cat + " square."
        if (self.cat == "Snake"):
            info = info + "\nSlide down the snake to " + str(self.end)
        elif (self.cat == "Ladder"):
            info = info + "\nClimb up the ladder to " + str(self.end)
        return info