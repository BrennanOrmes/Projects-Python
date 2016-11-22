#-------------------------------------------------------------------------------
# Name:        Blackjack
# Purpose:
#
# Author:      cnys
#
# Created:     09/09/2015
# Copyright:   (c) cnys 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Deck import Deck
from Card import Card
from BlackJackHand import Hand



def main():
    #make a temporary object


    deck = Deck()
    hand = Hand()
    deck.shuffle()
    #print deck.toString()

    card1 = Card("","")
    card1 = deck.drawNext()
    hand.AddCard(card1)
    print hand.toString()

    card1 = deck.drawNext()
    hand.AddCard(card1)
    print hand.toString()

    total = hand.totalValue()
    print "Your hand is worth " + str(total)



if __name__ == '__main__':
    main()
