def addFileSer():
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sFILE = open("skhGulR.txt", 'at')

    sNAME = input("Enter name: (leave blank to end...): ")
    while sNAME != "":
        sCLASS = input("Enter class: ")
        sFEE = float(input("Enter fee: "))
        sFILE.write(sNAME + "#" + sCLASS + "#" + str(sFEE) + "\n")

        sNAME = input("Enter name: (leave blank to end...): ")
    sFILE.close()

def printFileSer():
    # sNAME STRING
    # sREC STRING

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    sREC = ""

    try:
        sFILE = open("skhGulR.txt", 'rt')

        sREC = sFILE.readline()
        while sREC != "":
            sNAME, sCLASS, sFEE = sREC.split('#')

            print("Student name: ", sNAME)
            print("Student class: ", sCLASS)
            print("Student fee: ", sFEE.strip())
            print()

            sREC = sFILE.readline()
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
        sFILE = open("skhGulR.txt", 'rt')
        searchName = input("Enter name to search for: ")

        sREC = sFILE.readline()
        while sREC != "":
            sNAME, sCLASS, sFEE = sREC.split('#')

            if sNAME == searchName:
                found = True
                print("Student name: ", sNAME.strip())
                print("Student class: ", sCLASS.strip())
                print("Student fee: ", sFEE)
                print()
            sREC = sFILE.readline()
        sFILE.close()
        if not found:
            print(searchName, "is not found in file...")
    except Exception as error:
        print(error)
#addFileSer()
printFileSer()
searchFileSer()