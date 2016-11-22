#-------------------------------------------------------------------------------
# Name:        Deck
# Purpose:     A deck of 52 card objects
#
# Author:      cnys
#
# Created:     09/09/2015
# Copyright:   (c) cnys 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Card import Card
import random

class Deck:
    """a class to represent a card deck of 52 card objects"""

    def __init__(self):
        """a class to return a deck of 52 cards held in a list
        >>>Deck()
        DeckType"""
        self.cardlist = []
        self.next = -1

        j = 0
        for j in range (0, 13):
            j += 1
            card = Card("Hearts", str(j))
            if j == 1:
                card.setRank("Ace")
            elif j == 11:
                card.setRank("Jack")
                card.setValue(10)
            elif j == 12:
                card.setRank("Queen")
                card.setValue(10)
            elif j == 13:
                card.setRank("King")
                card.setValue(10)
            self.cardlist.append(card)

        j = 0
        for j in range (0, 13):
            j += 1
            card = Card("Clubs", str(j))
            if j == 1:
                card.setRank("Ace")
            elif j == 11:
                card.setRank("Jack")
                card.setValue(10)
            elif j == 12:
                card.setRank("Queen")
                card.setValue(10)
            elif j == 13:
                card.setRank("King")
                card.setValue(10)
            self.cardlist.append(card)

        j = 0
        for j in range (0, 13):
            j += 1
            card = Card("Diamonds", str(j))
            if j == 1:
                card.setRank("Ace")
            elif j == 11:
                card.setRank("Jack")
                card.setValue(10)
            elif j == 12:
                card.setRank("Queen")
                card.setValue(10)
            elif j == 13:
                card.setRank("King")
                card.setValue(10)
            self.cardlist.append(card)

        j = 0
        for j in range (0, 13):
            j += 1
            card = Card("Spades", str(j))
            if j == 1:
                card.setRank("Ace")
            elif j == 11:
                card.setRank("Jack")
                card.setValue(10)
            elif j == 12:
                card.setRank("Queen")
                card.setValue(10)
            elif j == 13:
                card.setRank("King")
                card.setValue(10)
            self.cardlist.append(card)

    def toString(self):
        info = ""
        for k in self.cardlist:
            k.turn()
            #take this out later once we know it works
            #info = info + k.toString() + "\n"
        return info

    def shuffle(self):
        random.shuffle(self.cardlist)

    def drawNext(self):
        self.next += 1
        nextcard = self.cardlist[self.next]
        nextcard.turn()
        return nextcard








