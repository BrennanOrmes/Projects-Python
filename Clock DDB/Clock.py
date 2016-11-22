#-------------------------------------------------------------------------------
# Name:        Clock
# Purpose:
#
# Author:      cnys
#
# Created:     05/09/2014
# Copyright:   (c) cnys 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Clock:
#creates a clock object as a series of hours, minutes, seconds, locale
#this is only partially complete, you will have to add bits yourself

    def __init__(self):
    #the constructor
    #start by declaring attributes
        self.theHours = 0
        self.theMinutes= 0
        self.theSeconds= 0
        self.theTimezone = "BST"
        self.validTime= True

    def setHours(self, newvalue):
	#a modifier (transformer) method
    #change Hours
        self.theHours = newvalue

    def setMinutes(self, newvalue):
	#a modifier (transformer) method
    #change Minutes
        self.theMinutes = newvalue

    def setSeconds(self, newvalue):
	#a modifier (transformer) method
    #change Seconds
        self.theSeconds = newvalue

    def setTimezone(self, newvalue):
	#a modifier (transformer) method
    #change Timezone
    #expects a string as a parameter!
        self.theTimezone = newvalue

    def getHours (self):
	#an accessor (return) method
    #return a value for the hours
        return self.theHours

    def getMinutes (self):
	#an accessor (return) method
    #return a value for the hours
        return self.theMinutes

    def getSeconds (self):
	#an accessor (return) method
    #return a value for the hours
        return self.theSeconds

    def getTimezone (self):
	#an accessor (return) method
    #return a value for the hours
        return self.theTimezone

    def toString(self):
    # return a string representing the whole Clock
        clockstring = "The time in " + self.getTimezone() + " is now "
        clockstring = clockstring + str(self.getHours()) + ":" + str(self.getMinutes())
        clockstring = clockstring + ":" + str(self.getSeconds())
        return clockstring

    def clockTick(self):
    #clock seconds increase by 1
    #this may also affect hours and minutes
    #increment your seconds by 1
        self.theSeconds = self.theSeconds +1
    #are the seconds at 60?  if they are, the minutes go up by 1
    #and the seconds reset to 0.
        if (self.getSeconds()== 60):
            self.setSeconds(0)
            self.theMinutes = self.theMinutes+1
    #now check the minutes, are they at 60?  if so put up the hours by 1
    #finally, check the hours.  Are they at 24?  if so reset them to 0.

#end of the Clock class


def main():
    clock1 = Clock()
    #created a clock object called clock1
    hh = raw_input ("Enter the hours here 0 - 23 >> ")
    hh = int(hh)
    clock1.setHours(hh)
    clock1.setSeconds(59)
    #using the set method to change the value from 0 to 14
    print clock1.toString()
    #print it out to test it
    print clock1.getSeconds()
    clock1.clockTick()
    print clock1.getSeconds()
    print clock1.toString()
    #lx = raw_input ("Get timezone >> ")
    #clock1.setTimezone(lx)
    clock1.setTimezone(raw_input ("Get timezone >> "))
    print clock1.toString()

    clock2 = Clock()
    clock2.setHours(11)
    clock2.setMinutes(59)
    clock2.setSeconds(59)
    clock2.setTimezone("San Francisco")

    clock3 = Clock()
    clock3.setHours(01)
    clock3.setMinutes(12)
    clock3.setSeconds(44)
    clock3.setTimezone("Brussels")

    print clock1.toString()
    print clock2.toString()
    print clock3.toString()


if __name__ == '__main__':
    main()


#Clock tasks
#complete toString() and test it
#complete clockTick() and test it
#complete setTime(string) and test it
