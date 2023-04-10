import os

def addSeq():
    nID = 0
    nName = ""
    nClass = ""
    nFee = 0.0

    sID = 0
    sName = ""
    sClass = ""
    sFee = 0.0

    added = False

    try:
        sFILE = open("skhGulSeq.txt", 'rt')
    except:
        sFILE = open("skhGulSeq.txt", 'xt')
        sFILE.close()
        sFILE = open("skhGulSeq.txt", 'rt')
    tFILE = open("temp.txt", 'wt')

    nID = int(input("Enter new ID: "))
    nName = input("Enter new name: ")
    nClass = input("Enter new class: ")
    nFee = float(input("Enter new fee: "))

    sID = sFILE.readline()
    while sID != "":
        sName = sFILE.readline()
        sClass = sFILE.readline()
        sFee = sFILE.readline()

        if int(sID) > nID and added is False:
            added = True
            tFILE.write(str(nID) + "\n")
            tFILE.write(nName + "\n")
            tFILE.write(nClass + "\n")
            tFILE.write(str(nFee) + "\n")
        elif int(sID) == nID:
            added = True
            print("Record ID:", nID, "already exists in file.")

        tFILE.write(sID)
        tFILE.write(sName)
        tFILE.write(sClass)
        tFILE.write(sFee)

        sID = sFILE.readline()

    if added is False:
        added = True
        tFILE.write(str(nID) + "\n")
        tFILE.write(nName + "\n")
        tFILE.write(nClass + "\n")
        tFILE.write(str(nFee) + "\n")
    sFILE.close()
    tFILE.close()

    os.remove("skhGulSeq.txt")
    os.rename("temp.txt", "skhGulSeq.txt")

def outputSeq():
    sID = 0
    sName = ""
    sClass = ""
    sFee = 0.0
    try:
        sFILE = open("skhGulSeq.txt", 'rt')
        sID = sFILE.readline()
        while sID != "":
            sName = sFILE.readline()
            sClass = sFILE.readline()
            sFee = sFILE.readline()

            print("Student ID: ", sID.strip())
            print("Student name:", sName.strip())
            print("Student class:", sClass.strip())
            print("Student fee:", sFee.strip())
            print()

            sID = sFILE.readline()
        sFILE.close()
    except:
        print("File doesn't exists...")

addSeq()
outputSeq()