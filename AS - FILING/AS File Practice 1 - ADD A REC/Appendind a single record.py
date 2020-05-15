# Python code for: Adding a record to the end of a text file

rollNo = 0
sName = ""
sContact = ""
sFee = 0.0
isFeePaid = False

rollNo = int(input ("Enter roll number: "))
sName = input("Enter student name: ")
sContact = input("Enter student contact: ")
sFee = float(input("Enter fee amount: "))
isFeePaid = bool(input("Is fee paid? (True/False): "))

fileHandle = open("sRec.txt", "a")
fileHandle.write(str(rollNo) + "\n")
fileHandle.write(sName + "\n")
fileHandle.write(sContact + "\n")
fileHandle.write(str(sFee) + "\n")
fileHandle.write(str(isFeePaid) + "\n")

fileHandle.close()

