import os

def addFileSer():
    # sNAME STRING

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sFILE = open("skhGul.txt", 'at')

    sNAME = input("Enter name: (leave blank to end...): ")
    while sNAME != "":
        sCLASS = input("Enter class: ")
        sFEE = float(input("Enter fee: "))

        sFILE.write(sNAME + "\n")
        sFILE.write(sCLASS + "\n")
        sFILE.write(str(sFEE) + "\n")

        sNAME = input("Enter name: (leave blank to end...): ")
    sFILE.close()

def printFileSer():
    # sNAME STRING

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    try:
        sFILE = open("skhGul.txt", 'rt')

        sNAME = sFILE.readline()
        while sNAME != "":
            sCLASS = sFILE.readline()
            sFEE = float(sFILE.readline())

            print("Student name: ", sNAME.strip())
            print("Student class: ", sCLASS.strip())
            print("Student fee: ", sFEE)
            print()

            sNAME = sFILE.readline()
        sFILE.close()
    except Exception as error:
        print(error)

def searchFileSer():
    # sNAME STRING

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    searchName = ""
    found = False

    try:
        sFILE = open("skhGul.txt", 'rt')
        searchName = input("Enter name to search for: ")

        sNAME = sFILE.readline()
        while sNAME != "":
            sCLASS = sFILE.readline()
            sFEE = float(sFILE.readline())

            if sNAME.strip() == searchName:
                found = True
                print("Student name: ", sNAME.strip())
                print("Student class: ", sCLASS.strip())
                print("Student fee: ", sFEE)
                print()
            sNAME = sFILE.readline()
        sFILE.close()
        if not found:
            print(searchName, "is not found in file...")
    except Exception as error:
        print(error)

def deleteFileSer():
    # sNAME STRING

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    searchName = ""
    found = False

    try:
        sFILE = open("skhGul.txt", 'rt')
        tFILE = open("temp.txt", "wt")

        searchName = input("Enter name to delete: ")

        sNAME = sFILE.readline()
        while sNAME != "":
            sCLASS = sFILE.readline()
            sFEE = sFILE.readline()

            if sNAME.strip() != searchName:
                tFILE.write(sNAME)
                tFILE.write(sCLASS)
                tFILE.write(sFEE)
            else:
                found = True
            sNAME = sFILE.readline()
        sFILE.close()
        tFILE.close()
        if not found:
            print(searchName, "is not found in file...")
            os.remove("temp.txt")
        else:
            os.remove("skhGul.txt")
            os.rename("temp.txt", "skhGul.txt")
    except Exception as error:
        print(error)

def editFileSer():
    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    sN = ""
    sC = ""
    sF = 0
    searchName = ""
    found = False

    try:
        sFILE = open("skhGul.txt", 'rt')
        tFILE = open("temp.txt", "wt")

        searchName = input("Enter name to edit: ")

        sNAME = sFILE.readline()
        while sNAME != "":
            sCLASS = sFILE.readline()
            sFEE = sFILE.readline()

            if sNAME.strip() != searchName:
                tFILE.write(sNAME)
                tFILE.write(sCLASS)
                tFILE.write(sFEE)
            else:
                found = True
                print("Student name: ", sNAME.strip())
                print("Student class: ", sCLASS.strip())
                print("Student fee: ", sFEE)
                print("Now enter updated data to save")

                sN = input("Enter name: ")
                if sN == "": sN = sNAME.strip()

                sC = input("Enter class: ")
                if sC == "": sC = sCLASS.strip()

                sF = input("Enter fee: ")
                if sF == "": sF = sFEE.strip()

                tFILE.write(sN + "\n")
                tFILE.write(sC + "\n")
                tFILE.write(sF + "\n")

            sNAME = sFILE.readline()
        sFILE.close()
        tFILE.close()
        if not found:
            print(searchName, "is not found in file...")
            os.remove("temp.txt")
        else:
            os.remove("skhGul.txt")
            os.rename("temp.txt", "skhGul.txt")
    except Exception as error:
        print(error)

printFileSer()
editFileSer()
printFileSer()