l=[12,22,33,77,128,90]
largestNumber = l[0]
index = 0
for i in range (len(l)):
    if l[i]>largestNumber:
        largestNumber=l[i]
        index=i
print("the largest number is :",largestNumber)
print("The index is :",index)
