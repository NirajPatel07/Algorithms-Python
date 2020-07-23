#Binary Search Can Be apllied only on Sorted list.
#Iterative Method
def BinarySearchI(data, target):
    low=0
    high=len(data)-1
    
    while low<=high:
        mid=low+high//2
        if target==data[mid]:
            return True
        elif target>data[mid]:
            low= mid+1
        else:
            high= mid-1
    return False


#Recursive Method

def BinarySearchR(data, target, low, high):
    if low>=high:
        return False
    else:
        mid=low+high//2
        if target==data[mid]:
            return True
        elif target>data[mid]:
            return BinarySearchR(data, target, mid+1, high)
        else:
            return BinarySearchR(data, target, low, mid-1)




data=list(map(int, input("Enter Values:\n").split()))
target=int(input("Enter Target:\n"))
print("Data is ",data)
print("Target is ",target)

print(BinarySearchI(data, target))
print(BinarySearchR(data, target, 0, len(data)-1))
