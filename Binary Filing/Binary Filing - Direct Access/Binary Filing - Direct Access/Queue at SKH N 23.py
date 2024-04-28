"""
Task is to create a circular queue using a 
1D array as per the following pseudocode:

DECLARE Queue : ARRAY [0:9] OF CHARACTER
DECLARE FrontP, RearP, Qsize : INTEGER

PROCEDURE initQ()
   DECLARE i : INTEGER
   FOR i = 0 TO 9
     Queue[i] = '' //Null
   NEXT
   FrontP = -1
   RearP = -1
   Qsize = 0
END PROCEDURE

PROCEDURE EnQ(x : CHARACTER)
  IF Qsize = 10 THEN
     OUTPUT "Overflow. No space to add a new element."
  ELSE
     IF RearP = 9 THEN
        RearP = 0
     ELSE
        RearP = RearP + 1
     ENDIF
     Queue[RearP] = x
     Qsize = Qsize +1
  ENDIF 
END PROCEDURE

FUNCTION DeQ() : CHARACTER
  IF Qsize = 0 THEN
     OUTPUT "Underflow. No element to delete."
  ELSE
     IF FrontP = 9 THEN
        FrontP = 0
     ELSE
        FrontP = FrontP + 1
     ENDIF
     x = Queue[FrontP]
     Qsize = Qsize -1
     RETURN x
  ENDIF 
END FUNCTION

"""
# global space
Queue = ['' for i in range(10)]
FrontP = -1
RearP = -1
Qsize = 0

def initQ():
    global FrontP, RearP, Qsize
    for i in range(10):
        Queue[i] = ''
    FrontP = -1
    RearP = -1
    Qsize = 0

def EnQ(x):
    global RearP, Qsize
    if Qsize == 10:
        print("Overflow. No space to add a new element.")
    else:
        if RearP == 9:
            RearP = 0
        else:
            RearP = RearP + 1
        Queue[RearP] = x
        Qsize = Qsize +1

def DeQ():
    global FrontP, Qsize
    if Qsize == 0:
        print("Underflow. No element to delete.")
    else:
        if FrontP == 9:
            FrontP = 0
        else:
            FrontP = FrontP + 1
        x = Queue[FrontP]
        Qsize = Qsize -1
        return x

def displayQ():
    if Qsize == 0:
        print("No element to show.")
    else:
        print("FrontP = ", FrontP)
        print("RearP = ", RearP)
        print("Qsize = ", Qsize)
        print("Queue = ", Queue)

# main program showing menu for Q ops.
choice = 0
while choice != 5:
    print("1. Initialize Queue")
    print("2. EnQ")
    print("3. DeQ")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        initQ()
    elif choice == 2:
        x = input("Enter the element to be added: ")
        EnQ(x)
    elif choice == 3:
        x = DeQ()
        print("The element deleted is: ", x)
    elif choice == 4:
        displayQ()
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid choice. Try again.")
# end of program