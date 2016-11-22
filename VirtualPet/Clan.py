#-------------------------------------------------------------------------------
# Name:        Deck
# Purpose:
#
# Author:      Brennan
#
# Created:     09/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Cardv2 import Card

class Deck:
    """a class to represent a card deck of 52 objects"""
    def __init__(self):
        """A class to return a deck of 52 cards jeld in a list
        >>>Deck()
        DeckType"""
        self.cardlist = []
        self.next = -1

        j = 0
        for j in range (0,13):
            j += 1
            card = Card("Starks", str(j))
            if j == 1:
                card.setRank("Ned")
            elif j == 11:
                card.setRank("Rob")
            elif j == 12:
                card.setRank("Brand")
            elif j == 13:
                card.setRank("Jon Snow")
            self.cardlist.append(card)

        j = 0
        for j in range (0,13):
            j += 1
            card = Card("Lannisters", str(j))
            if j == 1:
                card.setRank("Tyrion")
            elif j == 11:
                card.setRank("")
            elif j == 12:
                card.setRank("Queen")
            elif j == 13:
                card.setRank("King")
            self.cardlist.append(card)

        j = 0
        for j in range (0,13):
            j += 1
            card = Card("Targaryen", str(j))
            if j == 1:
                card.setRank("Ace")
            elif j == 11:
                card.setRank("Jack")
            elif j == 12:
                card.setRank("Queen")
            elif j == 13:
                card.setRank("King")
            self.cardlist.append(card)

        j = 0
        for j in range (0,13):
            j += 1
            card = Card("Bulton", str(j))
            if j == 1:
                card.setRank("Ace")
            elif j == 11:
                card.setRank("Jack")
            elif j == 12:
                card.setRank("Queen")
            elif j == 13:
                card.setRank("King")
            self.cardlist.append(card)

    def toString(self):
        info = ""
        for k in self.cardlist:
            k.turn()
            info = info + k.toString() + "\n"
        return info

    def shuffle(self):
        random.shuffle(self.card)

    def drawNext(self):
        self.next += 1
Deck()
