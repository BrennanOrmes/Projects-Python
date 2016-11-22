#-------------------------------------------------------------------------------
# Name:        Card
# Purpose:     simulate a simple card
#
# Author:      cnys
#
# Created:     01/09/2015
# Copyright:   (c) cnys 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Card:

#simulates a simple card

    """def __init__(self):
        empty constructor method for the card
        start by declaring all the attributes
        self.Suit = ""
        self.Rank = ""
        self.Value = 0
        self.Hidden = True"""

    """def __init__(self, suit, rank, value, hidden):
        full constructor method for the card
        which passes all parameters
        start by declaring all the attributes
        self.Suit =  suit
        self.Rank = rank
        self.Value = value
        self.Hidden = hidden"""

    def __init__(self, suit, rank):
        """partial constructor method for the card
        which passes all parameters
        start by declaring all the attributes"""
        self.Suit =  suit
        self.Rank = rank
        self.Hidden = True
        if self.Rank == "Ace":
            self.Value = 1
        elif (self.Rank == "Jack" or self.Rank == "Queen" or self.Rank == "King"):
            self.Value = 10
        else:
            self.Value = int(self.Rank)



    #accessor methods next - "get"
    def getSuit(self):
        #return the value for the suit
        return self.Suit

    #accessor methods next - "get"
    def getRank(self):
        #return the value for the rank
        return self.Rank

    #accessor methods next - "get"
    def getValue(self):
        #return the value for the point value
        return self.Value

    #accessor methods next - "get"
    def getHidden(self):
        #return the value for whether hidden (True) or visible (False)
        return self.Hidden

    #transformer/modifier methods next ("set")
    def setSuit(self, newvalue):
        """a method to re-set the suit value
        >>>setSuit("Diamonds")
        Diamonds"""
        self.Suit = newvalue

    #transformer/modifier methods next ("set")
    def setRank(self, newvalue):
        """a method to re-set the rank of the card
        >>>setRank("King")
        King
        >>>setRank("4")
        4"""
        self.Rank = newvalue

    #transformer/modifier methods next ("set")
    def setValue(self, newvalue):
        """a method to re-set the points value
        >>>setValue(9)
        9"""
        self.Value = newvalue

    #transformer/modifier methods next ("set")
    def setHidden(self, newvalue):
        """a method to re-set whether hidden or not (hidden = True)
        >>>setHidden(True)
        True"""
        self.Hidden = newvalue

    def toString(self):
        """a method to return ALL attribute values to string
        >>>toString()
        This card is the Jack of Clubs and is worth 10."""
        if self.Hidden == True:
            info = "This card is face down."
        else:
            info = "This card is the " + self.Rank + " of " + self.Suit
            info = info + " and is worth " + str(self.Value)
        return info

    def turn(self):
        """a method that makes a face down card visible, or hides a visible card
        >>>turn()
        NoneType"""
        if self.Hidden == True:
            self.Hidden = False
        else:
            self.Hidden = True












