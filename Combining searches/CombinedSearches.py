#-------------------------------------------------------------------------------
# Name:        A combined sort
# Purpose:     A program that combines multiple searches together, allowing
#               the user to input what program done
# Author:      Brennan
#
# Created:     16/09/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def BinSearch():
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

def SelectionSort():
    marks = []

    for j in range (0,6):
        MarksInput = int(raw_input("Please enter 6 numbers"))
        marks.append(MarksInput)
        j += 1
    top=len(marks)


    for i in range(0,top):
        min=i
        for j in range(i+1,top):
            if marks[j] < marks[min]:
                    min=j
        marks[i], marks[min]= marks [min], marks[i]
    print marks

def BubbleSort():
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

def InsertionSort():
    marks = []
    for j in range (0,6):
        MarksInput = int(raw_input("Please enter 6 numbers"))
        marks.append(MarksInput)

    top=len(marks)


    for i in range(1,top):
        temp = marks[i]
        j=i
        while j>0 and marks[j-1] > temp:
            marks[j] = marks [j-1]
            j=j-1
        marks[j]=temp
    print marks

def MergeSort():
    marks = []
    for j in range (0,6):
        MarksInput = int(raw_input("Please enter 6 numbers"))
        marks.append(MarksInput)

    top=len(marks)

    def merge_sort(marks):
        merge_sort_r(marks, 0, top-1)

    def merge (marks, first, last, sred):
        helper_list =[]

        i=first
        j=sred+1
        while i<= sred and j<=last:
            if marks[i]<= marks[j]:
                helper_list.append(marks[i])
                i=i+1
            else:
                helper_list.append(marks[j])
                j=j+1
        while i <=sred:
            helper_list.append(marks[i])
            i=i+1
        while j<= last:
            helper_list.append(marks[j])
            j=j+1
        for k in range(0, last-first+1):
            marks[first+k]=helper_list[k]

    def merge_sort_r(marks, first, last):
        if first<last:
            sred=((first+last)/2)
            merge_sort_r(marks, first,sred)
            merge_sort_r(marks, sred+1,last)
            merge(marks,first,last,sred)

    merge_sort(marks)
    print marks





ExitSelection = False
while not ExitSelection:
    try:
        UserSelection = int(raw_input("What would you like to do?\n1:Binary Search\n2:SelectionSort\n3:Bubble Sort\n4:Insertion Sort\n5:Merge Sort\n6: Exit"))
        #User selects what they want to do
        if UserSelection == 1:
            #BinarySort
            BinSearch()
        elif UserSelection == 2:
            SelectionSort()
            #SelectionSort
        elif UserSelection == 3:
            #BubbleSort
            BubbleSort()
        elif UserSelection == 4:
            #Insertion Sort
            InsertionSort()
        elif UserSelection == 5:
            #mergesort
            MergeSort()
        elif UserSelection == 6 or UserSelection == None:
            ExitSelection = True

    #Error handling
    except ValueError:
        print ("Please enter a valid menu selection.")
exit

