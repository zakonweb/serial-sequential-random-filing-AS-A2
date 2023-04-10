# Sequential Filing
import os
def addSeqFW():
    # sID, nID INT
    # sNAME, nNAME STRING
    # sCLASS, nCLASS STRING
    # sFEE, nFEE FLOAT
    # added BOOLEAN

    sID = 0
    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    nID = 0
    nNAME = ""
    nCLASS = ""
    nFEE = 0.0
    added = False
    t = ""

    nID = int(input("Enter new ID: "))
    nNAME = input("Enter new name: ")
    nCLASS = input("Enter new class: ")
    nFEE = float(input("Enter new fee: "))

    try:
        stuFile = open("skhNorthSeq.txt", "rt")
    except:
        stuFile = open("skhNorthSeq.txt", "xt")
        stuFile.close()
        stuFile = open("skhNorthSeq.txt", "rt")

    tempFile = open("tempFile.txt", "wt")
    t = stuFile.readline()
    while t != "":
        sID = int(t)
        sNAME = stuFile.readline()
        sCLASS = stuFile.readline()
        sFEE = stuFile.readline()

        if sID > nID and added is False:
            added = True
            tempFile.write(str(nID) + "\n")
            tempFile.write(nNAME + "\n")
            tempFile.write(nCLASS + "\n")
            tempFile.write(str(nFEE) + "\n")

        if sID == nID:
            added = True
            print(nID, "already exists...")

        tempFile.write(str(sID) + "\n")
        tempFile.write(sNAME)
        tempFile.write(sCLASS)
        tempFile.write(sFEE)

        t = stuFile.readline()

    if added is False:
        added = True
        tempFile.write(str(nID) + "\n")
        tempFile.write(nNAME + "\n")
        tempFile.write(nCLASS + "\n")
        tempFile.write(str(nFEE) + "\n")

    stuFile.close()
    tempFile.close()
    os.remove("skhNorthSeq.txt")
    os.rename("tempFile.txt", "skhNorthSeq.txt")


def readRecordsFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT

    sID = ""
    sNAME = ""
    sCLASS = ""
    sFEE = ""

    try:
        theFile = open("skhNorthSeq.txt", "rt")
        sID = theFile.readline()
        while sID != "":
            sNAME = theFile.readline()
            sCLASS = theFile.readline()
            sFEE = float(theFile.readline())

            print("Student ID:", sID.strip())
            print("Student Name:", sNAME.strip())
            print("Student Class:", sCLASS.strip())
            print("Student Fee:", sFEE)
            print()
            sID = theFile.readline()
        theFile.close()
    except FileNotFoundError:
        print("file doesn't exist...")

def searchRecordsFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT
    #searchName STRING
    #Found BOOLEAN

    sNAME = ""
    sCLASS = ""
    sFEE = 0
    searchName = ""
    Found = False

    try:
        theFile = open("skhNorthSeq.txt", "rt")
        searchName = input("Enter name to search for: ")
        sNAME = theFile.readline()
        while sNAME != "":
            sCLASS = theFile.readline()
            sFEE = float(theFile.readline())

            if searchName == sNAME.strip():
                Found = True
                print("Student Name:", sNAME.strip())
                print("Student Class:", sCLASS.strip())
                print("Student Fee:", sFEE)
                print()
            sNAME = theFile.readline()
        theFile.close()
        if Found is False: print("Record not found...")
    except FileNotFoundError:
        print("file doesn't exist...")


def deleteRecordsFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT
    #searchName STRING
    #Found BOOLEAN

    sNAME = ""
    sCLASS = ""
    sFEE = 0
    searchName = ""
    Found = False

    try:
        theFile = open("skhNorthSeq.txt", "rt")
        tempFile = open("temp.txt", "wt")

        searchName = input("Enter name to delete for: ")

        sNAME = theFile.readline()
        while sNAME != "":
            sCLASS = theFile.readline()
            sFEE = theFile.readline()

            if searchName != sNAME.strip():
                Found = True
                tempFile.write(sNAME)
                tempFile.write(sCLASS)
                tempFile.write(sFEE)
            sNAME = theFile.readline()
        theFile.close()
        tempFile.close()
        if Found is False:
            print("Record not found...")
            os.remove("temp.txt")
        else:
            os.remove("skhNorthSeq.txt")
            os.rename("temp.txt", "skhNorthSeq.txt")
    except FileNotFoundError:
        print("file doesn't exist...")

def editRecordsFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT
    #searchName STRING
    #Found BOOLEAN

    sNAME = ""
    sCLASS = ""
    sFEE = 0
    sn = ""
    sc = ""
    sf = 0
    searchName = ""
    Found = False

    try:
        theFile = open("skhNorthSeq.txt", "rt")
        tempFile = open("temp.txt", "wt")

        searchName = input("Enter name to delete for: ")

        sNAME = theFile.readline()
        while sNAME != "":
            sCLASS = theFile.readline()
            sFEE = theFile.readline()

            if searchName != sNAME.strip():
                tempFile.write(sNAME)
                tempFile.write(sCLASS)
                tempFile.write(sFEE)
            else:
                Found = True
                sn = input("Enter new name: ")
                if sn == "": sn = sNAME.strip()

                sc = input("Enter new class: ")
                if sc == "": sc = sCLASS.strip()

                sf = input("Enter new fee: ")
                if sf == "": sf = sFEE.strip()

                tempFile.write(sn + "\n")
                tempFile.write(sc + "\n")
                tempFile.write(sf + "\n")
            sNAME = theFile.readline()
        theFile.close()
        tempFile.close()
        if Found is False:
            print("Record not found...")
            os.remove("temp.txt")
        else:
            os.remove("skhNorthSeq.txt")
            os.rename("temp.txt", "skhNorthSeq.txt")
    except FileNotFoundError:
        print("file doesn't exist...")


# main program
#addSeqFW()
readRecordsFW()