 #-------------------------------------------------------------------------------
# Name:        Calculator
# Purpose:      To add stuff
#
# Author:      Brennan
#
# Created:     12/02/2015
# Copyright:   (c) Brennan CD Ormes 2015
# Licence:     CHLEB International (c) 2014
#-------------------------------------------------------------------------------

UserSelection = str

""" Things to do:
    Better UI(DONE)
    Error Handling(DONE)
    Exit option for users(DONE)

No more feature additions need to be made."""

def addition():
#Addition
    try:
        Number1 = float(raw_input("Please Enter your first Number..."))
        Number2 = float(raw_input("Please Enter your second Number..."))

        Answer = Number1 + Number2
        final_answer(Answer)
    #Error handling
    except ValueError:
        print("That is not a number!")
        addition()




def subtraction():
    #Subtraction
     try:
        Number1 = float(raw_input("Please Enter your first Number..."))
        Number2 = float(raw_input("Please Enter your second Number..."))

        Answer = Number1 - Number2
        final_answer(Answer)
     #Error handling
     except ValueError:
        print("That is not a number!")
        subtraction()



def multiplication():
    #Multiplication
     try:
        Number1 = float(raw_input("Please Enter your first Number..."))
        Number2 = float(raw_input("Please Enter your second Number..."))

        Answer = Number1 * Number2
        final_answer(Answer)
     #Error handling
     except ValueError:
        print("That is not a number!")
        multiplication()



def division():
    #Division
     try:
        Number1 = float(raw_input("Please Enter your first Number..."))
        Number2 = float(raw_input("Please Enter your second Number..."))

        Answer = Number1 / Number2
        final_answer(Answer)
     #Error handling
     except ValueError:
        print("That is not a number!")
        division()

def final_answer(Answer):
    print("The answer is "+str(Answer)+"")


ExitSelection = False
while not ExitSelection:
    try:
        UserSelection = int(raw_input("What would you like to do?\n1:Addition\n2:Subtraction\n3:Multiplicaton\n4:Division\n5: Exit"))
        #User selects what they want to do
        if UserSelection == 1:
            #Addidtion
            addition()
        elif UserSelection == 2:
            subtraction()
            #Subtraction
        elif UserSelection == 3:
            #Multiplication
            multiplication()
        elif UserSelection == 4:
            #Division
            division()
        elif UserSelection == 5 or UserSelection == None:
            ExitSelection = True
    #Error handling
    except ValueError:
        print ("Please enter a valid menu selection.")
exit

#End of program





