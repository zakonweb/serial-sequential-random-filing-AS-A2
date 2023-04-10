def serialAddRecFW():
    #sNAME STRING
    #sCLASS STRING
    #sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sf = open("akari.txt", 'at')
    sNAME = input("Enter name (leave blank to quit): ")
    while sNAME != "":
        sCLASS = input("Enter class: ")
        sFEE = float(input("Enter fee: "))

        sf.write(sNAME + "\n")
        sf.write(sCLASS + "\n")
        sf.write(str(sFEE) + "\n")
        sNAME = input("Enter name (leave blank to quit): ")
    sf.close()

def serialPrintRecFW():
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0

    sf = open("akari.txt", 'rt')
    sNAME = sf.readline()
    while sNAME != "":
        sCLASS = sf.readline()
        sFEE = sf.readline()

        print("Student name: ", sNAME.strip())
        print("Student class: ", sCLASS.strip())
        print("Student fee: ", sFEE)

        sNAME = sf.readline()
    sf.close()

def serialSearchRecFW():
    # sNAME STRING
    # sCLASS STRING
    # sFEE FLOAT
    # searchName STRING
    # found BOOLEAN

    sNAME = ""
    sCLASS = ""
    sFEE = 0.0
    searchName = ""
    found = False

    searchName = input("Enter name to search for: ")

    sf = open("akari.txt", 'rt')
    sNAME = sf.readline()
    while sNAME != "":
        sCLASS = sf.readline()
        sFEE = sf.readline()
        if sNAME.strip() == searchName:
            found = True
            print("Student name: ", sNAME.strip())
            print("Student class: ", sCLASS.strip())
            print("Student fee: ", sFEE)
        sNAME = sf.readline()
    sf.close()
    if not found:
        print(searchName, "is not found...")

serialPrintRecFW()
serialSearchRecFW()