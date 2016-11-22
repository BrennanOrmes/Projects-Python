#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     09/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------




def binsearch(InputListInt, search):
   right = len(InputList)
   left = 0
   previous_centre = -1
   if search < InputList[0]:
       return -1
   while 1:
       centre = (left + right) / 2
       candidate = InputList[centre]
       if search == candidate:
           return centre
       if centre == previous_centre:
           return - 2 - centre
       elif search < candidate:
           right = centre
       else:
           left = centre
       previous_centre = centre

InputList = []
# Counter
x = 0

UserInput = raw_input("Enter a value (int)")
InputList.append(UserInput)
InputListInt = [int(f) if f.isdigit() else f for f in InputList]
InputListInt.sort()
x += 1
while x !=5:
    UserInput = raw_input("Enter a value (int)")
    InputList.append(UserInput)
    InputListInt = [int(f) if f.isdigit() else f for f in InputList]
    InputListInt.sort()
    x += 1
    print (InputListInt)
else:
    search = raw_input("What number are you looking for?")
    binsearch(InputList, search)

print binsearch(InputListInt, search)


