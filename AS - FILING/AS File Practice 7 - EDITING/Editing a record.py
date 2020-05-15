# Python code for: Editing a record in a text file
import os

nextLine = ""
isFound = False
reqRollNo = 0
rollNo = 0
sName = ""
sContact = ""
sFee = 0.0
isFeePaid = False

reqRollNo = int(input("Enter roll number to edit record for: "))

fileHandle = open("sRec.txt", "r")
fileHandleNew = open("temp.txt", "w")
nextLine = fileHandle.readline()

while len(nextLine) > 0:
    rollNo = int(nextLine)
    sName = fileHandle.readline()
    sContact = fileHandle.readline()
    sFee = float(fileHandle.readline())
    isFeePaid = bool(fileHandle.readline())

    if rollNo == reqRollNo:
        isFound = True
        sName = input("Enter student name: ")
        sName = sName + "\n"
        sContact = input("Enter student contact: ")
        sContact = sContact + "\n"
        sFee = float(input("Enter fee amount: "))
        isFeePaid = bool(input("Is fee paid? (True/False): "))

    fileHandleNew.write(str(rollNo) + "\n")
    fileHandleNew.write(sName)
    fileHandleNew.write(sContact)
    fileHandleNew.write(str(sFee) + "\n")
    fileHandleNew.write(str(isFeePaid) + "\n")

    nextLine = fileHandle.readline()

if isFound == False:
    print("Roll number", reqRollNo, "is not found.")
else:
    print("Record edited successfully.")

fileHandle.close()
fileHandleNew.close()
os.remove("sRec.txt")
os.rename("temp.txt", "sRec.txt")