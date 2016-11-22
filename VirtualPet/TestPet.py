#-------------------------------------------------------------------------------
# Name:        TestHarness
# Purpose:
#
# Author:      Brennan
#
# Created:     08/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from VirtualPet import VirtualPet

def main():
    pet1 = VirtualPet()
    pet1.setName(raw_input("Name your pet"))
    pet1.Feed("XL Bacon Double Cheeseburger", 300000)
    print pet1.toString()

    pet2 = VirtualPet()
    pet2.setName(raw_input("Name your pet"))
    pet2.Feed("XL Bacon Double Cheeseburger", 300000)
    print pet2.toString()


    print("And he has" + pet1.Happiness + " happiness points")
    print("And he has" + pet2.Happiness + " happiness points")

main()