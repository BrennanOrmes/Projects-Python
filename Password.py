#-------------------------------------------------------------------------------
# Name:        Password
# Purpose:      Prompt user for password, for every time user fails to get
#               the correct, a value will be added to the counter to show
#               the amount of attempts the user took to get the password right.
# Author:      Brennan
#
# Created:     05/02/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Variables
Access = False
counter = 1
ListCounter = 0

#Array
AccountList=[],[]
PasswordList=[]

again = 'yes'


while again == "yes":
    AccountName = raw_input("Please input an account name?")
    Password = raw_input("Please input a password for this account")

    AccountList.append(AccountName)
    PasswordList.append(Password)
    ListCounter = ListCounter + 1

    again = raw_input("Would you like to make another account? (Yes/No)")

if again == "no" or again == "No":

    #Start Loop
    while Access == False:
        AccountInput = raw_input("Please enter your account name?")
        PasswordInput = raw_input ("Please enter the password")
        #End Loop when password = CorrectPassword


        if AccountInput == AccountList(CounterList) and PasswordList(CounterList) == PasswordInput:
            Access = True
    else:
        #If Password = Incorrect; add 1 to counter.
        counter = counter + 1

    #Once "Access" = True, then Display Message below;
    if Access == True:
        print ("You have gotten the password correct! It took you " +str(counter)+ " times(s) to get the password correct!")




