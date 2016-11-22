#-------------------------------------------------------------------------------
# Name:        Student Results
# Purpose:
#
# Author:      Brennan
#
# Created:     05/02/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
Things to do:
    Make better UI
    Error Handling(DONE)
    Loop(DONE)
"""
def grade_calculator():
# Variables
    name = str
    grade = str
    score = int
    # Start Loop, until 5th iteration of output is complete
    for x in range (0, 5):

        #Input (Student name and Score)
        name = raw_input("What is your name?")
        try:
            score = int(raw_input("What score did you achieve."))
        #Error Handling
        except ValueError:
            print("That is not a number!")
            grade_calculator()

        #Grading Calc
        if score < 50:
            grade = ("F")
        elif score > 49 and score < 60:
            grade = ("C")
        elif score > 59 and score < 70:
            grade = ("B")
        elif score > 69:
            grade = ("A")

        #End Output (Student Name, Score and Grade)
        if score < 50:
            print(name+ ", Sorry you have failed. Your mark is "+str(score)+" and your grade is " +grade)
        else:
            print(name+ ", Congrats you have passed!. Your mark is "+str(score)+" and your grade is " +grade)

grade_calculator()
