inputList=list(map(int,input("Enter Elements\n").split()))
c=int(input("1. Ascending Order\n2.Descending Order\nEnter Your Choice\n"))
print("Unsorted List:\n",inputList)

if c==1:
    for i in range(len(inputList)-1):
        for j in range(len(inputList)-1):
            if inputList[j]>inputList[j+1]:
                inputList[j],inputList[j+1]=inputList[j+1],inputList[j]
else:
    for i in range(len(inputList)-1):
        for j in range(len(inputList)-1):
            if inputList[j]<inputList[j+1]:
                inputList[j],inputList[j+1]=inputList[j+1],inputList[j]
    
print('Sorted List:\n',inputList)
