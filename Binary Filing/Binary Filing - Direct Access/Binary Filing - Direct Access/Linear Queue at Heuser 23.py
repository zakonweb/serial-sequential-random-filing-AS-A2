"""
*LINEAR QUEUE*
Task is to write python code for linear queue as mentioned in following pseudocode:
//LINEAR QUEUE ADT
DECLARE Queue : ARRAY [0:5] OF CHARACTER
DECLARE tail, head : INTEGER

CONSTANT Null ← -1

PROCEDURE InitQ()
   DECLARE i : INTEGER
   FOR i ← 0 TO 5
     Queue[i] ← ''
   NEXT

   tail ← Null
   head ← Null
END PROCEDURE

PROCEDURE EnQ(data : CHARACTER)
   IF tail = LEN(Queue)-1 THEN //Overflow error
      OUTPUT "Overflow error. Data cannot be added anymore."
   ELSE
      tail ← tail +1
      Queue[tail] ← data
   ENDIF
END PROCEDURE

FUNCTION DeQ() RETURN CHARACTER
   DECLARE data : CHARACTER

   IF head = tail THEN
      OUTPUT "Underflow erroe. No item to delete anymore."
   ELSE
      head ← head +1
      data ← Queue[head]
      RETURN data
   ENDIF
END FUNCTION
"""
# DECLARE Queue : ARRAY [0:5] OF CHARACTER
Queue = [None for i in range(6)]

# CONSTANT Null ← -1
Null = -1

# DECLARE tail, head : INTEGER
tail = Null
head = Null

def InitQ():
    global tail, head
    for i in range(6):
        Queue[i] = ''
    tail = Null
    head = Null

def EnQ(data):
    global tail
    if tail == len(Queue)-1:
        print("Overflow error. Data cannot be added anymore.")
    else:
        tail += 1
        Queue[tail] = data

def DeQ():
    global head
    if head == tail:
        print("Underflow error. No item to delete anymore.")
        return '*'
    else:
        head += 1
        data = Queue[head]
        Queue[head] = ''
        return data

def display():
    print("head: ", head)
    print("tail: ", tail)
    print("Queue: ", Queue)

# main program
InitQ()
choice = 0
while choice != 4:
    print("1. EnQ")
    print("2. DeQ")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter data to be inserted: ")
        EnQ(data)
    elif choice == 2:
        data = DeQ()
        if data != '*':
            print("Data deleted: ", data)
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice. Try again.")
# end of the program