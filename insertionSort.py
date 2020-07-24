def insertionSort(list1):
    for i in range(1,len(list1)):
        curr=list1[i]
        pos=i
        while curr<=list1[pos-1] and pos>0:
            list1[pos]=list1[pos-1]
            pos-=1
        list1[pos]=curr

list1=list(map(int, input("Enter Elements:\n").split()))
print("Before Sorting:\n",list1)
insertionSort(list1)
print("After Sorting:\n",list1)
