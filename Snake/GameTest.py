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
from Die import Die
from Square import Square
from Board import Board

def main():
    #make a die obj
    d = Die()
    print d.roll()
    b = Board()
    print b.toString()

    s1 = Square(57, "Snake", 40)
    s2 = Square(26, "Ladder", 84)
    s3 = Square(2, "Plain", 2)

    print s1.toString()
    print s2.toString()
    print s3.toString()

if __name__ == '__main__':
    main()
