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