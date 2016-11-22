#-------------------------------------------------------------------------------
# Name:        Challenge 1
# Purpose:
#
# Author:      Brennan
#
# Created:     26/02/2015
# Copyright:   (c) Brennan CEO & Lewis CEO
# Licence:     CHLEB International (C)
#-------------------------------------------------------------------------------

#Declare Variables
NoOfChildren = int
Activity1 =  int
Activity2 = int
Activity3 = int
Activity4 = int

repeat = "yes"

#Totals for each activity
Total1 = int
Total2 = int
Total3 = int
Total4 = int

if repeat == "yes":
    while repeat == "Yes" or repeat == "yes":
    	#User input
    	NoOfChildren = input("How many children have attended today?")
    	Activity1 = input("Ropes and Swings" +"\n"+  "How many children did this activity?")
    	Activity2 = input("Water Fun" +"\n"+  "How many children did this activity?")
    	Activity3 = input("Animal antics" +"\n"+  "How many children did this activity?")
    	Activity4 = input("Driving mini" +"\n"+  "How many children did this activity?")

    	#Adding totals up
    	Total1 = Total1 + Activity1
    	Total2 = Total2 + Activity2
    	Total3 = Total3 + Activity3
    	Total4 = Total4 + Activity4

elif repeat == "No" or repeat == "no":
    #Final Output and result.
    print("For Ropes and Swings there were " +str(Total1)+"\n"+"For Water Fun there were " +str(Total2)+"\n"+"For Animal Antics there were " +str(Total3)+"\n"+"For Driving Mini's there were " +str(Total4))






