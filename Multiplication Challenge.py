#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     12/03/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint


#Start of variables
RangeNumber1 = 0
RangeNumber2 = 0
MultiplyNumber1 = randint(RangeNumber1,RangeNumber2)
MultiplyNumber2 = randint(RangeNumber1,RangeNumber2)
MutiplyNumber1 = int
MutiplyNumber2 = int
count = 0
RealAnswer = int
RealAnswer = MultiplyNumber1 * MultiplyNumber2

#Number of questions
NumOfQuestions = int
NumOfQuestions = input("How many questions would you like?")


#Range of numbers (Difficulty)
RangeNumber1 = input("What range of numbers would you like between? (Enter first number)")
RangeNumber2 = input("Enter the second number...")

#Loop
for x in range(0,NumOfQuestions):
    MultiplyNumber1 = randint(RangeNumber1,RangeNumber2)
    MultiplyNumber2 = randint(RangeNumber1,RangeNumber2)
    Answer = input("What is " + str(MultiplyNumber1)+ " times " +str(MultiplyNumber2)+"?")


    if Answer != MultiplyNumber1 * MultiplyNumber2:
        #If the user gets the question wrong, this message shall appear
        print("Sorry that is not right. The answer is " + str(RealAnswer))

    else:
        #If the user gets the question right, this message shall appear
        print("Thats right well done")
        count += 1
        #Increase Difficulty
        RangeNumber1 -= 1
        RangeNumber2 += 1

#Final Output
print("You got "+str(count)+ " questions out of " + str(NumOfQuestions) + " Right!")