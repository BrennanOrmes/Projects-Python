#-------------------------------------------------------------------------------
# Name:        TestHarnessCard
# Purpose:
#
# Author:      Brennan
#
# Created:     02/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Card import Card
import random
def main():
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
    ranks = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    random.shuffle(suits)
    random.shuffle(ranks)

    c1 = Card(suits[0], ranks[0])
    print c1.toString()
    c1.turn()
    print c1.toString()

    c2 = Cardard(suits[1], ranks[1])
    print c2.toString()
    c2.turn()
    print c1.toString()

    sum = (c1.getValue() + c2.getValue())
    if (sum < 21):
        answer = raw_input("Type T or t to twist, anything else to stick")
        if (answer == "T" or answer == "t"):
            c3 = Card(suits[2], ranks[2])
            print c3.toString()
            c3.turn()
            print c3.toString()
            sum = sum + c3.getValue()

    print("Your hand is worth"+str(sum))

    if(sum >21):
        print("busted!")

if __name__ == '__main__':
    main()
