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

"""Improved version
To do in future:
    Make better user interface.
    Add function if the user trys to make same account twice. (DONE)
    Make user enter one uppercase letter in there password (Would be nice to know how to do it for future reference)"""


#Variables
Access = False
counter = 0
ListCounter = 0

#Array
AccountList=[]
PasswordList=[]

again = 'yes'


#Loop
while again == "yes" or again == "Yes":
    AccountName = input("Please input an account name?\n(Please note that the account name is case sensitive)")
    while AccountName in AccountList:
        AccountName = input("Account name is already in the system.\nPlease try again.")

    Password = input("Please input a password for this account")

    AccountList.append(AccountName)
    PasswordList.append(Password)
    ListCounter+=1
    #End loop when user input 'no' (Not case sensitive!!!)
    try:
        again = input("Would you like to make another account? (Yes/No)")
    except:
        again = input("Please enter Yes or No.")

if again == "no" or again == "No":
    while not Access:
        AccountInput = input("Please enter your account name:")
        PasswordInput = input("Please enter the password:")
        #For 'in zip' it searches both arrays at the same time
        for account, password in zip(AccountList, PasswordList):
            if account == AccountInput and password == PasswordInput:
                Access = True
                #Break out of the loop
                break
        counter+=1

    if Access:
        #Final output. Displays amount of times the user took to get the password right.
        #Counts the actual attempt even when getting it correct. (That is ment to happen)
        print ("You have gotten the password correct! It took you " + str(counter) + " time(s) to get the password correct!")

#end







