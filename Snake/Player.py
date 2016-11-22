#-------------------------------------------------------------------------------
# Name:        PlayerClass
# Purpose:     A class to simulate a player in a board game
#
# Author:      Brennan
#
# Created:     22/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Player:
    """A class to represent a player in a board game"""

    def __init__(self):
        """A constructor method for the player class
        >>>Player()
        NoneType"""
        self.name = "nameless"
        self.position = 1


    def setName(self, newval):
        """Resets the name of the player
        >>>setName("Piggy")
        NoneType"""
        self.name = newval

    def toString(self):
        """returns the attribute values as one big string
        >>>toString()
        'Peter is on position 27'"""
        info = self.name + "is on square number " + str(self.position)
        return info