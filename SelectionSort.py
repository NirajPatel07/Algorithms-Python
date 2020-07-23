print("*****Selection Sort*****\n")
print("1. Sorting In Ascending Order\n2.Sorting in Descending Order\n")
s=input("Enter Your Choice:\n")
iList=list(map(int,input("Enter Elements\n").split()))
print("Given List:\n",iList)

if s=='1':
    for i in range(len(iList)):
        minValue=min(iList[i:])
        indexMinValue=iList.index(minValue,i)
        iList[i],iList[indexMinValue]= iList[indexMinValue],iList[i]
else:
    for i in range(len(iList)):
        maxValue=max(iList[i:])
        indexMaxValue=iList.index(maxValue,i)
        iList[i],iList[indexMaxValue]= iList[indexMaxValue],iList[i]
    
print("Sorted List:\n",iList)
