# Python code for: Searching and display a record from a text file

nextLine = ""
isFound = False
reqRollNo = 0
rollNo = 0
sName = ""
sContact = ""
sFee = 0.0
isFeePaid = False

reqRollNo = int(input("Enter roll number to search for: "))

fileHandle = open("sRec.txt", "r")
nextLine = fileHandle.readline()

while len(nextLine) > 0 and isFound == False:
    rollNo = int(nextLine)
    sName = fileHandle.readline()
    sContact = fileHandle.readline()
    sFee = float(fileHandle.readline())
    isFeePaid = bool(fileHandle.readline())

    if rollNo == reqRollNo:
        print("Student roll number:", rollNo)
        print("Student name:", sName[:-1])
        print("Student contact:", sContact[:-1])
        print("Student fee:", sFee)
        print("Fee paid:", isFeePaid)
        print()
        isFound = True

    nextLine = fileHandle.readline()

if isFound == False:
    print("Roll number", reqRollNo, "is not found.")
fileHandle.close()