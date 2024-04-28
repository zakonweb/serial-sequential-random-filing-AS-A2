"""
Python code for the following
Recursive Binary Search pseudocode

FUNCTION BsearchR(val, LB, UB : INTEGER) RETURN INTEGER
       MID ← (LB+UB) MOD 2
       IF LB>UB THEN //STOP VALUE
          RETURN -1
       ELSEIF Arr[MID] = val THEN
          RETURN MID
       ELSEIF val > Arr[MID] THEN
          RETURN BsearchR(val, MID+1, UB) //RECURSION
       ELSE
          RETURN BsearchR(val, LB, MID-1) //RECURSION
       ENDIF
END FUNCTION
"""
# global space
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# recusrsive binary search
def bsearchR(val, LB, UB):
    # base case
    if LB > UB:
        return -1 # if value not found

    # recursive case
    else:
        MID = (LB + UB) // 2
        if arr[MID] == val:
            return MID
        elif val > arr[MID]:
            return bsearchR(val, MID + 1, UB)
        else:
            return bsearchR(val, LB, MID - 1)

# main program
choice = 0
# main menu
while choice != 2:
    print("1. Recursive Binary Search")
    print("2. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        val = int(input("Enter value to search: "))
        index = bsearchR(val, 0, len(arr) - 1)
        if index == -1:
            print("Value not found")
        else:
            print("Value found at index", index+1)
    elif choice == 2:
        print("Exiting...")
    else:
        print("Invalid choice")
# end of program