#-------------------------------------------------------------------------------
# Name:        Bubble Sort
# Purpose:
#
# Author:      Brennan
#
# Created:     15/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Array for marks
marks = []
for p in range (0,6):
    #User input
    MarksInput = int(raw_input("Please enter 6 numbers"))
    marks.append(MarksInput)
#    print marks
    p += 1

#Bubble sort
top=len(marks)
i=0
for i in range (0,top):
    for j in range (0,top-1):
        if marks[j]>marks[j+1]:
            temp=marks[j+1]
            marks[j+1]=marks[j]
            marks[j]=temp
        j=j+1
    i=i+1
print (marks)