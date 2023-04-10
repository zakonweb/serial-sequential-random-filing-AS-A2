#Serail file operation
#one record per line with field separator '#'
import os

def addRecWiseSer():
    sf = open("studentGALrec.txt","at")

    stName = input("Enter name (Leave blank to end): ")
    while stName != "":
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        sf.write(stName + "#" + stClass + "#" + str(stFee) + "\n")

        stName = input("Enter name (Leave blank to end): ")

    sf.close()

def displayRecWiseSer():
    try:
        fno = 0
        thisChar = ''
        sf = open("studentGALrec.txt","rt")
        stRec = sf.readline()
        while stRec != "":
            fno = 0
            thisChar = ''
            stName = ''
            stClass = ''
            stFee = ''
            """
            for thisChar in stRec:
                if thisChar == '#':
                    fno += 1
                elif fno == 0:
                    stName +=thisChar
                elif fno == 1:
                    stClass += thisChar
                else:
                    stFee += thisChar
            """
            stName, stClass, stFee = stRec.split('#')
            print(stName)
            print(stClass)
            print(stFee)
            stRec = sf.readline()

        sf.close()
    except Exception as e:
        print("File doesn't exists...", e)

def searchRecWiseSer():
    found = False
    searchName = input("Enter name to search for: ")
    try:
        sf = open("studentGALrec.txt","rt")
        stRec = sf.readline()
        while stRec != "":
            stName, stClass, stFee = stRec.split('#')

            if searchName == stName.strip():
                found = True
                print(stName)
                print(stClass)
                print(stFee)
            stRec = sf.readline()
        sf.close()
        if not found:
            print(searchName, "is not found...")
    except:
        print("File doesn't exists...")

def delRecWiseSer():
    found = False
    searchName = input("Enter name to delete record: ")
    try:
        sf = open("studentGALrec.txt","rt")
        tf = open("temp.txt","wt")

        stRec = sf.readline()
        while stRec != "":
            stName, stClass, stFee = stRec.split('#')

            if searchName != stName.strip():
                tf.write(stName + '#' + stClass + '#' + stFee)
            else:
                found = True
            stRec = sf.readline()
        sf.close()
        tf.close()
        if not found:
            print(searchName, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("studentGALrec.txt")
            os.rename("temp.txt","studentGALrec.txt")
    except:
        print("File doesn't exists...")

def editRecWiseSer():
    found = False
    searchName = input("Enter name to edit record: ")
    try:
        sf = open("studentGALrec.txt","rt")
        tf = open("temp.txt","wt")

        stRec = sf.readline()
        while stRec != "":
            stName, stClass, stFee = stRec.split('#')

            if searchName != stName:
                tf.write(stName + '#' + stClass + '#' + stFee)
            else:
                found = True
                print(stName)
                print(stClass)
                print(stFee)
                print()
                print("Now enter new data or enter blank to keep previous data.")
                sN = input("Enter updated name:")
                if sN == "":
                    sN = stName.strip()
                sC = input("Enter updated class:")
                if sC == "":
                    sC = stClass.strip()
                sF = input("Enter updated fee:")
                if sF == "":
                    sF = stFee.strip()
                tf.write(sN + "#" + sC + "#" + sF + "\n")
            stRec = sf.readline()
        sf.close()
        tf.close()
        if not found:
            print(searchName, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("studentGALrec.txt")
            os.rename("temp.txt","studentGALrec.txt")
    except:
        print("File doesn't exists...")

def options():
    print("1. Add field wise record.")
    print("2. Read field wise record.")
    print("3. Search field wise record.")
    print("4. Delete field wise record.")
    print("5. Edit field wise record.")
    print("0. Quit.")
    opt = int(input("Enter the choice... "))
    return opt

# main program
opt = options()
while opt != 0:
    if opt == 1: addRecWiseSer()
    if opt == 2: displayRecWiseSer()
    if opt == 3: searchRecWiseSer()
    if opt == 4: delRecWiseSer()
    if opt == 5: editRecWiseSer()
    opt = options()