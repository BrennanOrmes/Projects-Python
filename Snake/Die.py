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
from random import randint

class Die:
    """ To simulate a die for playing board games and crap"""

    def __init__(self):
        """Constructor method for the die, does not need any parameters"""
        pass

    def roll(self):
        """when roll() is called it returns a random integer 1 - 6
        >>>roll()
        4"""
        return randint(1,6)



