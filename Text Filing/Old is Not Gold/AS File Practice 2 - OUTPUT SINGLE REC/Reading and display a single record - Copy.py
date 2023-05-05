# Python code for: Reading and display a record from a text file

rollNo = 0
sName = ""
sContact = ""
sFee = 0.0
isFeePaid = False

fileHandle = open("sRec.txt", "r")
rollNo = int(fileHandle.readline())
sName = fileHandle.readline()
sContact = fileHandle.readline()
sFee = float(fileHandle.readline())
isFeePaid = bool(fileHandle.readline())

print("Student roll number:", rollNo)
print("Student name:", sName[:-1])
print("Student contact:", sContact[:-1])
print("Student fee:", sFee)
print("Fee paid:", isFeePaid)

fileHandle.close()