import os

def addSeqFW():
    nID = 0
    nNAME = ""
    nCLASS = ""
    nFEE = 0.0

    fID = 0
    fNAME = ""
    fCLASS = ""
    sFEE = 0.0

    added = False

    try:
        thisFile = open("askariSeq.txt", "rt")
    except:
        thisFile = open("askariSeq.txt", "xt")
        thisFile.close()
        thisFile = open("askariSeq.txt", "rt")
    tempFile = open("temp.txt", "wt")

    nID = int(input("Enter new ID: "))
    nNAME = input("Enter new name: ")
    nCLASS = input("Enter new class: ")
    nFEE = float(input("Enter new fee: "))

    fID = thisFile.readline()
    while fID != "":
        fNAME = thisFile.readline()
        fCLASS = thisFile.readline()
        fFEE = thisFile.readline()

        if int(fID) == nID:
            added = True
            print(nID, "already exists...")
        elif int(fID) > nID and added is False:
            added = True
            tempFile.write(str(nID) + "\n")
            tempFile.write(nNAME + "\n")
            tempFile.write(nCLASS + "\n")
            tempFile.write(str(nFEE) + "\n")

        tempFile.write(fID)
        tempFile.write(fNAME)
        tempFile.write(fCLASS)
        tempFile.write(fFEE)

        fID = thisFile.readline()

    if not added:
        added = True
        tempFile.write(str(nID) + "\n")
        tempFile.write(nNAME + "\n")
        tempFile.write(nCLASS + "\n")
        tempFile.write(str(nFEE) + "\n")

    thisFile.close()
    tempFile.close()
    os.remove("askariSeq.txt")
    os.rename("temp.txt", "askariSeq.txt")

def SeqPrintRecFW():
    # sID INTEGER
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT

    sID = ""
    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sf = open("askariSeq.txt", 'rt')
    sID = sf.readline()
    while sID != "":
        sNAME = sf.readline()
        sCLASS = sf.readline()
        sFEE = sf.readline()

        print("Student ID: ", sID.strip())
        print("Student name: ", sNAME.strip())
        print("Student class: ", sCLASS.strip())
        print("Student fee: ", sFEE)

        sID = sf.readline()
    sf.close()

def SeqSearchRecFW():
    # sID INTEGER
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT
    # searchName STRING
    # found BOOLEAN

    sID = ""
    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    searchID = ""
    found = False

    searchID = input("Enter ID to search for: ")

    sf = open("askariSeq.txt", 'rt')
    sID = sf.readline()
    while sID != "":
        sNAME = sf.readline()
        sCLASS = sf.readline()
        sFEE = sf.readline()

        if sID.strip() == searchID:
            found = True
            print("Student ID: ", sID.strip())
            print("Student name: ", sNAME.strip())
            print("Student class: ", sCLASS.strip())
            print("Student fee: ", sFEE)
        sID = sf.readline()
    sf.close()
    if not found:
        print(searchID, "is not found...")


def DelSeqFW():
    nID = 0

    fID = 0
    fNAME = ""
    fCLASS = ""
    sFEE = 0.0

    deleted = False

    try:
        thisFile = open("askariSeq.txt", "rt")
        tempFile = open("temp.txt", "wt")

        nID = int(input("Enter ID to delete: "))

        fID = thisFile.readline()
        while fID != "":
            fNAME = thisFile.readline()
            fCLASS = thisFile.readline()
            fFEE = thisFile.readline()

            if int(fID) != nID:
                tempFile.write(fID)
                tempFile.write(fNAME)
                tempFile.write(fCLASS)
                tempFile.write(fFEE)
            else:
                deleted = True

            fID = thisFile.readline()

        thisFile.close()
        tempFile.close()

        if not deleted:
            print(nID, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("askariSeq.txt")
            os.rename("temp.txt", "askariSeq.txt")
    except:
        print("File doe not exists...")


# main program
#addSeqFW()
#SeqSearchRecFW()
SeqPrintRecFW()
print("---------------------------")

DelSeqFW()
print("---------------------------")

SeqPrintRecFW()