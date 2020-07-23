def mergeSort(list1):
    c=0
    if len(list1)>1:
        mid=len(list1)//2
        leftList=list1[:mid]
        rightList=list1[mid:]
        mergeSort(leftList)
        mergeSort(rightList)
        i=0
        j=0
        k=0
        while i<len(leftList) and j<len(rightList):
            if leftList[i]<rightList[j]:
                list1[k]=leftList[i]
                i+=1
                k+=1
            else:
                list1[k]=rightList[j]
                
                j+=1
                k+=1
        while i<len(leftList):
            list1[k]=leftList[i]
            i+=1
            k+=1
        while j<len(rightList):
            list1[k]=rightList[j]
            j+=1
            k+=1
    

list1=list(map(int,input("Enter Elements of Array:\n").split()))
print(mergeSort(list1))
print("Sorted List:\n",list1)
