# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    #these values are used to break while loops.
    a = b = c = 0

    #While both arrays lengths are greater than 0 (to start).
    while a < len(arrA) and b < len(arrB):
        #arrA LESS than arrB
        if (arrA[a] < arrB[b]):
            #Then the first element in a new array will be equal to the first element in arrA.
            merged_arr[c] = arrA[a]
            #Add values to "a" and "c" in order to stop iteration.
            a += 1
            c += 1
        #if arrA is GREATER than arrB.
        else:
            #Make the first element in the new array equal to arrB's first element instead.
            merged_arr[c] = arrB[b]
            #Update values in order to stop iteration.
            b += 1
            c += 1
    #as long as a is greater than the length of arrA.
    while a < len(arrA):
        #The value of "c" equals the value in arrA.
        merged_arr[c] = arrA[a]
        a += 1
        c += 1
    #as long as b is less than length of arrB.
    while b < len(arrB):
        #The value of "c" equals the value in arrB.
        merged_arr[c] = arrB[b]
        b += 1
        c += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        #left side being recursed.
        left = merge_sort(arr[0:len(arr) // 2])
        #left side being recursed.
        right = merge_sort(arr[len(arr) // 2:])
        #left and right get merged.
        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
