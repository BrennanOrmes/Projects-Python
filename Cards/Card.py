#-------------------------------------------------------------------------------
# Name:        Card
# Purpose:     simulate a simple clock
#
# Author:      cnys
#
# Created:     01/09/2015
# Copyright:   (c) cnys 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Card:

#simulates a simple clock

    #def __init__(self):
       # """empty constructor method for the clock
       # start be declaring all the attributes"""
       # self.Suit = ""
       # self.Rank = ""
       # self.Value = ""
       # self.Hidden = True

   # def __init__(self, suit, rank, value, hidden):
       # """empty constructor method for the clock
       # start be declaring all the attributes"""
       # self.Suit = suit
       # self.Rank = rank
       # self.Value = value
       # self.Hidden = hidden


    def __init__(self, suit, rank):
        """constructor method for the clock
        start be declaring all the attributes"""
        self.Suit = suit
        self.Rank = rank
        self.Hidden = True
        if self.Rank == "Ace":
            self.Value = 1
        elif self.Rank == "Jack" or self.Rank == "Quueen" or self.Rank == "King":
            self.Value = 10
        else:
            self.Value = int(self.Rank)


    #accessor methods next - "get"

    def getSuit(self):
        #return the value for the hours
        return self.Hours

    #accessor methods next - "get"
    def getRank(self):
        #return the value for the minutes
        return self.Minutes

    def printsomething(self):
        print(self.Hours)

    #accessor methods next - "get"
    def getValue(self):
        #return the value for the seconds
        return self.Seconds

    #accessor methods next - "get"
    def getHidden(self):
        #return the value for the timezone
        return self.Timezone

    #transformer/modifier methods next ("set")
    def setSuit(self, newvalue):
        """a method to re-set the suit value
        >>>setSuit(diamonds)
        diamonds"""
        self.Suit = newvalue

    #transformer/modifier methods next ("set")
    def setRank(self, newvalue):
        """a method to re-set the rank value
        >>>setRank("king")
        king
        >>>setRank("4")
        4
        """
        self.Rank = newvalue

    #transformer/modifier methods next ("set")
    def setValue(self, newvalue):
        """a method to re-set the value
        >>>setValue(9)
        9"""
        self.Value = newvalue

    #transformer/modifier methods next ("set")
    def setHidden(self, newvalue):
        """a method to re-set the hidden value
        >>>setHidden("Hidden")
        Hidden"""
        self.Hidden = newvalue

    def toString(self):
        """a method to return ALL attributes values to string
        >>>toString()
        This cards is the jack of Clubs and is worth 10"""
        if self.Hidden == True:
            info = ("The card is face down")
        else:
            info = "The card is the "+self.Rank+" of "+self.Suit
            info = info+ " and is worth " +str(self.Value)
        return info

    def turn(self):
        """a method that makes a face down card visible, or not hides an already visible card
        >>>turn()
        NoneTupe"""
        if self.Hidden:
            self.Hidden = False
        else:
            self.Hidden = True
