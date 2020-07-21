# TO-DO: complete the helper function below to merge 2 sorted arrays 
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    for i in range(elements):
        if arrA[0]<= arrB[0]:
            merged_arr[i-1] = arrA[0]
            arrA = arrA[1:]
        else:
            merged_arr[i-1] = arrA[0]
            arrB = arrB[1:]


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    leftArr = []
    rightArr = []
    
    # recursively split list into lists of 1
    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        pass # run merge
    else:
        arrLen = int(len(arr))
        for i in range(arrLen):
            if i <= arrLen/2:
                leftArr.append(i)
            else:
                rightArr.append(i)

    # use merge function to put things together correctly


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

