import os

def addRecordFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0

    theFile = open("skhnorth.txt", "at")
    sNAME = input("Enter name (leave blank to quit.): ")
    while sNAME != "":
        sCLASS = input("Enter class: ")
        sFEE = float(input("Enter fee: "))

        theFile.write(sNAME + "\n")
        theFile.write(sCLASS + "\n")
        theFile.write(str(sFEE) + "\n")

        sNAME = input("Enter name (leave blank to quit.): ")
    theFile.close()

def readRecordsFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0

    try:
        theFile = open("skhnorth.txt", "rt")
        sNAME = theFile.readline()
        while sNAME != "":
            sCLASS = theFile.readline()
            sFEE = float(theFile.readline())

            print("Student Name:", sNAME.strip())
            print("Student Class:", sCLASS.strip())
            print("Student Fee:", sFEE)
            print()
            sNAME = theFile.readline()
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
        theFile = open("skhnorth.txt", "rt")
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
        theFile = open("skhnorth.txt", "rt")
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
            os.remove("skhnorth.txt")
            os.rename("temp.txt", "skhnorth.txt")
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
        theFile = open("skhnorth.txt", "rt")
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
            os.remove("skhnorth.txt")
            os.rename("temp.txt", "skhnorth.txt")
    except FileNotFoundError:
        print("file doesn't exist...")

def addRecordRW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0

    theFile = open("skhnorthR.txt", "at")
    sNAME = input("Enter name (leave blank to quit.): ")
    while sNAME != "":
        sCLASS = input("Enter class: ")
        sFEE = float(input("Enter fee: "))

        theFile.write(sNAME + "#" + sCLASS + "#" + str(sFEE) + "\n")

        sNAME = input("Enter name (leave blank to quit.): ")
    theFile.close()

def readRecordsRW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT
    #sREC STRING

    sNAME = ""
    sCLASS = ""
    sFEE = 0
    sREC = ""

    try:
        theFile = open("skhnorthR.txt", "rt")
        sREC = theFile.readline()
        while sREC != "":
            sNAME, sCLASS, sFEE = sREC.split('#')

            print("Student Name:", sNAME)
            print("Student Class:", sCLASS)
            print("Student Fee:", sFEE.strip())
            print()
            sREC = theFile.readline()
        theFile.close()
    except FileNotFoundError:
        print("file doesn't exist...")

def searchRecordsRW():
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
        theFile = open("skhnorthR.txt", "rt")
        searchName = input("Enter name to search for: ")

        sREC = theFile.readline()
        while sREC != "":
            sNAME, sCLASS, sFEE = sREC.split('#')

            if searchName == sNAME:
                Found = True
                print("Student Name:", sNAME)
                print("Student Class:", sCLASS)
                print("Student Fee:", sFEE.strip())
                print()
            sREC = theFile.readline()
        theFile.close()
        if Found is False: print("Record not found...")
    except FileNotFoundError:
        print("file doesn't exist...")


# main program
#addRecordRW()
readRecordsFW()
editRecordsFW()
readRecordsFW()
#searchRecordsRW()