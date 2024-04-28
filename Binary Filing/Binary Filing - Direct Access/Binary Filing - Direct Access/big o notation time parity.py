# array of 5000 random values
import random
arr = [random.randint(0, 100000) for i in range(5000)]
arr1 = arr.copy()
arr2 = arr.copy()

# read time at the beginning and at the end of algorithm
# and print the difference at the end
import time
startTime = 0
endTime = 0 
difference = 0

# simple bubble sort algorithm over the array
startTime = time.time()
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
endTime = time.time()
difference = endTime - startTime

print("Time: ", endTime - startTime)

# bubble sort with inner diminishing loop
startTime = time.time()
for i in range(len(arr1)):
    for j in range(len(arr1) - 1 - i):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
endTime = time.time()

print("Time: ", endTime - startTime)
diffPer = 100 - (((endTime - startTime)/difference)*100)
print("Diff Per: ", diffPer)

# fully efficient bubble sort with a flag and inner diminishing loop
startTime = time.time()
for i in range(len(arr2)):
    flag = False
    for j in range(len(arr2) - 1 - i):
        if arr2[j] > arr2[j+1]:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
            flag = True
    if not flag:
        break
endTime = time.time()

print("Time: ", endTime - startTime)
diffPer = 100-(((endTime - startTime)/difference)*100)
print("Diff Per: ", diffPer)