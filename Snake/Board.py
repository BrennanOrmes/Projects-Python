#-------------------------------------------------------------------------------
# Name:        The Board
# Purpose:
#
# Author:      Brennan
#
# Created:     22/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Square import Square



class Board:
    """A class to represen the snakes and ladders board of 100 suqares"""


    def __init__(self):
        """A constructor to make a board out of 100 squares
        >>>Board()
        Nonetype"""
        # Starts off with a black list of squares
        self.board = []
        for j in range (0, 100):
            #a 100 iteration loop...
            s = Square(j+1, "Plain", j+1)
            self.board.append(s)


    def toString(self):
        info = "Here is the state of the board!\n"
        for k in self.board:
            info = info + k.toString() + "\n"
        return info