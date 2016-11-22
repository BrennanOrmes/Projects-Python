#-------------------------------------------------------------------------------
# Name:        Clock
# Purpose:     simulate a simple clock
#
# Author:      cnys
#
# Created:     01/09/2015
# Copyright:   (c) cnys 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Clock:

#simulates a simple clock

    def __init__(self):
        """constructor method for the clock
        start be declaring all the attributes"""
        self.Hours = 0
        self.Minutes = 0
        self.Seconds = 0
        self.Timezone = "GMT"
        self.AM = True

    #accessor methods next - "get"
    def getHours(self):
        #return the value for the hours
        return self.Hours

    #accessor methods next - "get"
    def getMinutes(self):
        #return the value for the minutes
        return self.Minutes

    def printsomething(self):
        print(self.Hours)

    #accessor methods next - "get"
    def getSeconds(self):
        #return the value for the seconds
        return self.Seconds

    #accessor methods next - "get"
    def getTimezone(self):
        #return the value for the timezone
        return self.Timezone

    #accessor methods next - "get"
    def getAM(self):
        #return the value for whether AM (True) or PM (False)
        return self.AM

    #transformer/modifier methods next ("set")
    def setHours(self, newvalue):
        """a method to re-set the hours value
        >>>setHours(12)
        12"""
        self.Hours = newvalue

    #transformer/modifier methods next ("set")
    def setMinutes(self, newvalue):
        """a method to re-set the minutes value
        >>>setMinutes(59)
        59"""
        self.Minutes = newvalue

    #transformer/modifier methods next ("set")
    def setSeconds(self, newvalue):
        """a method to re-set the seconds value
        >>>setSeconds(52)
        52"""
        self.Seconds = newvalue

    #transformer/modifier methods next ("set")
    def setTimezone(self, newvalue):
        """a method to re-set the timezone
        >>>setTimezone("Lisbon")
        Lisbon"""
        self.Timezone = newvalue

    #transformer/modifier methods next ("set")
    def setAM(self, newvalue):
        """a method to re-set AM/PM (AM = True)
        >>>setAM(True)
        True"""
        self.AM = newvalue

    def toString(self):
        """a method to return ALL attribute values to string
        >>>toString()
        The time in Tel Aviv is now 11:59:59 AM"""
        clockstring = "The time in  " + self.getTimezone()
        clockstring = clockstring + " is now " + str(self.getHours())
        clockstring = clockstring + ":" + str(self.getMinutes()) + ":" + str(self.getSeconds())
        if self.AM == True:
            x = "AM"
        else:
            x = "PM"
        clockstring = clockstring + " " + x
        return clockstring

    def tick():
        """a method to make the clock tick over by 1 second"""
        pass

    def strike():
        """a method to make the clock strike on the hour.....
        >>>strike()
        BONG! BONG! BONG!"""
        pass

    def summerTime():
        """a method to put the clock forward an hour to account for BST"""
        pass









