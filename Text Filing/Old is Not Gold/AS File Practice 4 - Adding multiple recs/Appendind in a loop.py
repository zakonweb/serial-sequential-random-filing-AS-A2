# Python code for: Adding several records to the end of a text file
ans = "y"

while ans.upper() == "Y":
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

    ans = input("Do you want to add more records? (Y/N): ")

fileHandle.close()