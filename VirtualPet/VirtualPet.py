#-------------------------------------------------------------------------------
# Name:        Virtual Pet
# Purpose:
#
# Author:      Brennan
#
# Created:     08/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class VirtualPet:
    """A class to simulate a virtual pet that you can play with
    >>>VirtualPet()
    VirtualPetType"""

    def __init__(self):
        """Virtual Pet Constructor
        define the attributes first"""
        self.Name = "Poop"
        self.LifeRemaining = 25
        self.HowClean = 10
        self.Fed = 10
        self.Entertained = 10
        self.Happiness = (self.LifeRemaining + self.HowClean + self.Fed + self.Entertained)
        self.Alive = True


    def setName(self, newName):
        """Gives the virtual pet a name
        >>>setName("Felix")
        Felix"""
        self.Name = newName

    def getName(self):
        return self.Name


    def toString(self):
        info = "This pet is called " + self.Name + "and he has " + str(self.Fed) + " food points."
        return info

    def Feed(self, foodstuff, points):
        """A method to feed the Pet
        >>>Feed("XL Bacon Double Cheese Burger", 10)
        NoneType"""
        self.Fed += points
        return ("This pet has just eaten a dank "+ foodstuff)

    def getFed(self):
        return self.Fed

def getHappiness(self, Name):
    self.Happiness = (self.LifeRemaining + self.HowClean + self.Fed + self.Entertained)
    if self.Happiness > 50:
        return ("I am very happy! :D:D:D:D:D:D:D")
    elif self.Happiness > 35:
        return ("Meh need more dank memes...")
    elif self.Happiness > 10:
        return ("TOO many damn pepes in the comment section... >:(")
    else:
        return (Name + " Has signed out.")

def isAlive(self):
    if self.Happiness < 0:
        self.Alive = False




