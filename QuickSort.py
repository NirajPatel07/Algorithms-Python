def pivotPlace(list1, first, last):
    pivot=list1[first] #Selecting First Element as Pivot
    left=first+1
    right=last
    while True:
        while left<=right and pivot>=list1[left]:
            left+=1
        while left<=right and pivot<=list1[right]:
            right-=1
        if left>right:
            break
        else:
            list1[left], list1[right]= list1[right], list1[left]
    list1[first], list1[right]=list1[right], list1[first]
    return right

def quickSort(list1, first, last):
    if first<last:
        p=pivotPlace(list1, first, last)
        quickSort(list1, first, p-1)
        quickSort(list1, p+1, last)


list1=list(map(int, input().split()))
first=0
last=len(list1)-1
quickSort(list1, first, last)
print(list1)
