# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) == 0:
        return -1
    midpoint = int(start +((end - start)) / 2) 
    if target == arr[midpoint]:
        return midpoint
    elif target == arr[start]:
        return start
    elif target == arr[end]:
        return end
    elif target > arr[midpoint]:
        return binary_search(arr, target, midpoint + 1, end)
    elif target < arr[midpoint]:
        return binary_search(arr, target, start, midpoint - 1)
    else:
        return -1


def rev_binary_search(arr, target, start, end):
    if len(arr) == 0:
        return -1
    
    midpoint = int((end - start) / 2) 
    if target == arr[midpoint]:
        return midpoint
    elif target == arr[start]:
        return start
    elif target == arr[end]:
        return end
    elif target > arr[midpoint]:
        return rev_binary_search(arr, target, start, midpoint - 1)
    elif target < arr[midpoint]:
        return rev_binary_search(arr, target, midpoint + 1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

#     if len(arr) == 0:
#         return -1

#     arrLen = int(len(arr))
#     lastIndex = arr[arrLen - 1]
#     firstIndex = arr[0]
    

#     if firstIndex < lastIndex:
#         lowToHigh = binary_search(arr, target, 0, arrLen - 1)
#         return lowToHigh
#     elif firstIndex > lastIndex:
#         highToLow = rev_binary_search(arr, target, 0, arrLen - 1)
#         return highToLow
#     else:
#         return -1
    
    


