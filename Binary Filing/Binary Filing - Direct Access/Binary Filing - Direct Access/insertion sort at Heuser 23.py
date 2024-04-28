"""
pyhthon code for the insertion sort.
where j is outer loop
i is inner loop
and a key variable is used to store the value of the element to be inserted
"""

# global space
arr = [5, 2, 4, 6, 1, 3, 7]

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key # this is the place where the key is inserted

# main program
print("before sorting: ", arr)
insertion_sort(arr)
print("after sorting: ", arr)
# end of the program