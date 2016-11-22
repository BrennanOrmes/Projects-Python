#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     16/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Deck import Deck
from Card import Card


class Hand:
    def __init__ (self):
        self.SizeOfHand = 0
        self.CardsInHand = []

        """j = 0
        for j in range (0,2)"""

    def AddCard(self, card):
        self.CardsInHand.append(card)

    def toString(self):
            info = ""
            for k in self.CardsInHand:
                #take this out later once we know it works
                info = info + k.toString() + "\n"
            return info

    def totalValue(self):
        value = 0
        for x in self.CardsInHand:
            v = x.getValue()
            value = value + v
            return value












