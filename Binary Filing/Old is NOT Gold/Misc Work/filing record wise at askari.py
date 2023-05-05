def serialAddRecRW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sf = open("askari.txt", 'at')
    sNAME = input("Enter name (leave blank to quit): ")
    while sNAME != "":
        sCLASS = input("Enter class: ")
        sFEE = float(input("Enter fee: "))

        sf.write(sNAME + "#" + sCLASS + "#" + str(sFEE) + "\n")
        sNAME = input("Enter name (leave blank to quit): ")
    sf.close()

def serialPrintRecRW():
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT
    # sREC STRING

    sREC = ""
    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sf = open("askari.txt", 'rt')
    sREC = sf.readline()
    while sREC != "":
        sNAME, sCLASS, sFEE = sREC.split('#')

        print("Student name: ", sNAME)
        print("Student class: ", sCLASS)
        print("Student fee: ", sFEE)

        sREC = sf.readline()
    sf.close()

def serialSearchRecRW():
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT
    # sREC STRING

    sREC = ""
    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    searchName = ""
    found = False

    searchName = input("Enter name to search for: ")

    sf = open("askari.txt", 'rt')
    sREC = sf.readline()
    while sREC != "":
        sNAME, sCLASS, sFEE = sREC.split('#')

        if searchName == sNAME:
            found = True
            print("Student name: ", sNAME)
            print("Student class: ", sCLASS)
            print("Student fee: ", sFEE)

        sREC = sf.readline()
    sf.close()
    if found is False:
        print(searchName, "is not found....")
serialPrintRecRW()
serialSearchRecRW()