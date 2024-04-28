"""
O/N/22/42/Q3

A program uses a linear queue to store up to 100 integers.
(a) A 1D array, Queue, is used to store the data. The head pointer points to the first number
stored in the queue and the tail pointer points to the next free space in the queue.
Write program code to:
• declare the global array Queue
• declare the global variable head pointer and assign an appropriate initial value
• declare the global variable tail pointer and assign an appropriate initial value.
"""
Queue = [0 for i in range(100)]
head = 0 # head pointer
tail = 0

"""
(b) The function Enqueue() takes an integer value as a parameter and stores it in the queue. It
returns TRUE if the value was successfully stored and FALSE otherwise.
Write program code for the function Enqueue().
"""
def Enqueue(value):
    global tail
    if tail < 100:
        Queue[tail] = value
        tail += 1
        return True
    else:
        return False

"""
(d) The following iterative pseudocode function calculates the total of all the values stored in the
queue.
FUNCTION IterativeOutput(Start: INTEGER) RETURNS INTEGER
    DECLARE Total : INTEGER
    Total ← 0
    FOR Count ← Start - 1 TO HeadPointer STEP -1
        Total ← Total + Queue[Count]
    NEXT Count
    RETURN Total
ENDFUNCTION
Rewrite the function as a recursive function using program code.
"""
def RecursiveOutput(start):
    if start == head:
        return 0
    else:
        return Queue[start-1] + RecursiveOutput(start-1)

"""
(c) The main program uses the Enqueue() function to store the numbers 1 to 20 (inclusive)
in the queue, in ascending numerical order. The program should output ‘Successful’ if all
numbers are successfully enqueued, and ‘Unsuccessful’ otherwise.
Amend the main program by writing program code to perform this task.
"""
# main program
wasSuccessful = True
for i in range(1, 21):
    if Enqueue(i) == False:
        wasSuccessful = False
        break
if wasSuccessful:
    print("Successful")
else:
    print("Unsuccessful")

"""
(e) The main program calls the recursive function from part 3(d) and outputs the value returned.
(i) Amend the main program by writing program code to perform this task.
"""
print(RecursiveOutput(tail))
# end of program