# Python code for: Reading and display all records from a text file

nextLine = ""
rollNo = 0
sName = ""
sContact = ""
sFee = 0.0
isFeePaid = False

fileHandle = open("sRec.txt", "r")
nextLine = fileHandle.readline()

while len(nextLine) > 0:
    rollNo = int(nextLine)
    sName = fileHandle.readline()
    sContact = fileHandle.readline()
    sFee = float(fileHandle.readline())
    isFeePaid = bool(fileHandle.readline())

    print("Student roll number:", rollNo)
    print("Student name:", sName[:-1])
    print("Student contact:", sContact[:-1])
    print("Student fee:", sFee)
    print("Fee paid:", isFeePaid)
    print()

    nextLine = fileHandle.readline()

fileHandle.close()