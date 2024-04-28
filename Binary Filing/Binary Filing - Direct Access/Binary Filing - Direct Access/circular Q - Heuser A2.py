"""
*Circular Queue*
Task is to write circular queue code in python as per the following pseudocde:
//Circular Queue ADT

//Global Scope 
DECLARE Queue : ARRAY [0:5] OF CHARACTER

DECLARE tail, head, Qsize, Qlen : INTEGERS

PROCEDURE initQ()
   DECLARE i : INTEGER
   FOR i ← 0 TO 5
     Queue[i] ← ''
   NEXT

   tail ← -1
   head ← -
   Qsize ← 0		//SIZE OF QUEUE
   Qlen ← LEN(Queue)   //CAPACITY
END PROCEDURE

PROCEDURE EnQ(data : CHARACTER)
   IF Qsize = Qlen THEN //Overflow error
      OUTPUT "Overflow occured."
   ELSE
      IF tail = 5 THEN   //tail = Qlen -1
         tail ← 0
      ELSE
         tail ← tail +1
      ENDIF
      Queue[tail] ← data
      Qsize ← Qsize +1
   ENDIF
END PROCEDURE

FUNCTION DeQ() RETURNS CHARACTER
   DECLARE data : CHARACTER
   IF Qsize = 0 THEN 
      OUTPUT "Underflow error."
      RETURN '~'
   ELSE
      IF head = 5 THEN
         head ← 1
      ELSE
         head ← head +1
      END IF
      data ← Queue[head]
      Qsize ← Qsize -1
      RETURN data
   ENDIF
END FUNCTION
"""
# global scope
# declarartions
Queue = ['' for i in range(6)]
tail = -1
head = -1
Qsize = 0
Qlen = len(Queue)

# procedure initQ()
def initQ():
    global tail, head, Qsize, Qlen
    for i in range(6):
        Queue[i] = ''
    tail = -1
    head = -1
    Qsize = 0
    Qlen = len(Queue)

# procedure EnQ(data : CHARACTER)
def EnQ(data):
    global tail, Qsize
    if Qsize == Qlen:
        print("Overflow occured.")
    else:
        if tail == 5:
            tail = 0
        else:
            tail += 1
        Queue[tail] = data
        Qsize += 1

# function DeQ() RETURNS CHARACTER
def DeQ():
    global head, Qsize
    if Qsize == 0:
        print("Underflow error.")
        return '~'
    else:
        if head == 5:
            head = 1
        else:
            head += 1
        data = Queue[head]
        Qsize -= 1
        return data