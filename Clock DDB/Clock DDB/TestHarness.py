#-------------------------------------------------------------------------------
# Name:        TestHarness
# Purpose:     to test the clock class
#
# Author:      cnys
#
# Created:     01/09/2015
# Copyright:   (c) cnys 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Clock import Clock
#from the Clock.py file, pull in the Clock class

def main():
    c1 = Clock()
    c1.setHours(11)
    c1.setMinutes(59)
    c1.setSeconds(59)
    c1.setTimezone("Tel Aviv")
    c1.setAM(False)

    #let's print out the information......
    print c1.getHours()
    print c1.getMinutes()
    print c1.Seconds
    print c1.getTimezone()
    print c1.getAM()

    c2 = Clock()
    c2.setHours(1)
    c2.setMinutes(51)
    c2.setSeconds(43)
    c2.setTimezone("Brussels")
    c2.setAM(True)

    #let's print out the information......
    print c2.toString()

    clocks = []
    clocks.append[c1]
    clocks.append[c2]




if __name__ == '__main__':
    main()

