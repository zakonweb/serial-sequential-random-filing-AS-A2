# Sequential file operations
import os

def addFieldWiseSeqFile():
    thisID = int(input("Enter ID (-1 for ending): "))
    found = searchFieldWiseSeqFile(thisID, 2)
    if thisID != -1 and found is False:
        Name = input("Enter name: ")
        Class = input("Enter class: ")
        Fee = float(input("Enter fee: "))

        added = False
        try:
            sf = open("PAFStudentsFieldS.txt", "rt")
        except:
            sf = open("PAFStudentsFieldS.txt", "xt")
            sf = open("PAFStudentsFieldS.txt", "rt")
        tf = open("PAFStudentsFieldT.txt", "wt")

        stID = sf.readline()
        while stID != "":
            stName = sf.readline()
            stClass = sf.readline()
            stFee = sf.readline()

            if int(stID) > thisID and added is False:
                added = True
                tf.write(str(thisID) + "\n")
                tf.write(Name + "\n")
                tf.write(Class + "\n")
                tf.write(str(Fee)+"\n")
            tf.write(stID)
            tf.write(stName)
            tf.write(stClass)
            tf.write(stFee)

            stID = sf.readline()

        if added is False:
            tf.write(str(thisID) + "\n")
            tf.write(Name + "\n")
            tf.write(Class + "\n")
            tf.write(str(Fee)+"\n")

        sf.close()
        tf.close()

    if found:
        print("record already exists...")
    else:
        os.remove("PAFStudentsFieldS.txt")
        os.rename("PAFStudentsFieldT.txt", "PAFStudentsFieldS.txt")

def readFieldWiseSerialFile():
    try:
        sf = open("PAFStudentsFieldS.txt", "rt")
        stID = sf.readline()
        while stID != "":
            stName = sf.readline()
            stClass = sf.readline()
            stFee = float(sf.readline())

            #single field per line
            print(stID, end='')
            print(stName, end='')
            print(stClass, end='')
            print(str(stFee))
            stID = sf.readline()
        sf.close()
    except:
        print("File doesn't exist...")

def searchFieldWiseSeqFile(id, par):
    found = False
    try:
        sf = open("PAFStudentsFieldS.txt", "rt")
        stID = sf.readline()
        while stID != "" and int(stID) <= id:
            stName = sf.readline()
            stClass = sf.readline()
            stFee = sf.readline()

            #single field per line
            #match after removing \n from string
            if int(stID) == id:
                found = True
                if par == 1:
                    print(stID, end='')
                    print(stName, end='')
                    print(stClass, end='')
                    print(stFee, end='')
                break
            stID = sf.readline()
        sf.close()
    except:
        pass
    return found

def deleteFieldWiseSeqFile():
    found = False
    searchID = int(input("Enter ID to delete record for: "))

    sf = open("PAFStudentsFieldS.txt", "rt")
    tf = open("tempStudentsFieldT.txt", "wt")

    stID = sf.readline()
    while stID != "":
        stName = sf.readline()
        stClass = sf.readline()
        stFee = float(sf.readline())

        #single field per line
        #match after removing \n from string
        if int(stID) != searchID:
            tf.write(stID)
            tf.write(stName)
            tf.write(stClass)
            tf.write(str(stFee) + "\n")
        else:
            found = True
        stID = sf.readline()
    if found is False:
        print(searchID, 'is not found')
    else:
        print(searchID, 'is deleted.')
    sf.close()
    tf.close()
    os.remove("PAFStudentsFieldS.txt")
    os.rename("tempStudentsFieldT.txt", "PAFStudentsFieldS.txt")

def editFieldWiseSeqFile():
    found = False
    searchID = int(input("Enter ID to edit record for: "))

    sf = open("PAFStudentsFieldS.txt", "rt")
    tf = open("tempStudentsField.txt", "wt")

    stID = sf.readline()
    while stID != "":
        stName = sf.readline()
        stClass = sf.readline()
        stFee = float(sf.readline())

        #single field per line
        #match after removing \n from string
        if int(stID) == searchID:
            print(stID, end='')
            print(stName, end='')
            print(stClass, end='')
            print(str(stFee))
            print()

            print("Now reenter data for editing:")
            #stID = IDs don't get edited ever...
            stName = input("Enter name: ") + "\n"
            stClass = input("Enter class: ") + "\n"
            stFee = float(input("Enter fee: "))
            found = True

        tf.write(stID)
        tf.write(stName)
        tf.write(stClass)
        tf.write(str(stFee) + "\n")

        stID = sf.readline()

    if found is False:
        print(searchID, 'is not found')
    else:
        print(searchID, 'is edited.')

    sf.close()
    tf.close()
    os.remove("PAFStudentsFieldS.txt")
    os.rename("tempStudentsField.txt", "PAFStudentsFieldS.txt")

def addRecordWiseSeqFile():
    thisID = int(input("Enter ID (-1 for ending): "))
    if thisID != -1:
        added = False
        try:
            sf = open("PAFStudentsRecordS.txt", "rt")
        except:
            sf = open("PAFStudentsRecordS.txt", "xt")
            sf = open("PAFStudentsRecordS.txt", "rt")
        tf = open("PAFStudentsRecordT.txt", "wt")

        recLine = sf.readline()
        while recLine != "":
            thisChar = ''
            stID = ''
            for thisChar in recLine:
                if thisChar == '#':
                    break
                else:
                    stID += thisChar

            if int(stID) == thisID:
                added = True
                print("This ID already exists")
            elif int(stID) > thisID and added is False:
                added = True
                Name = input("Enter name: ")
                Class = input("Enter class: ")
                Fee = float(input("Enter fee: "))
                tf.write(str(thisID) + "#"+ Name + "#" + Class + "#" + str(Fee)+ "\n")
            tf.write(recLine)
            recLine = sf.readline()

        if added is False:
            Name = input("Enter name: ")
            Class = input("Enter class: ")
            Fee = float(input("Enter fee: "))
            tf.write(str(thisID) + "#"+ Name + "#" + Class + "#" + str(Fee)+ "\n")

        sf.close()
        tf.close()
        os.remove("PAFStudentsRecordS.txt")
        os.rename("PAFStudentsRecordT.txt", "PAFStudentsRecordS.txt")

def deleteRecordWiseSeqFile():
    #complete record (all fields) with a separater character.
    found = False
    searchID = input("Enter ID to delete record for: ")

    sf = open("PAFStudentsRecordS.txt", "rt")
    tf = open("tempStudentsRecordT.txt", "wt")

    recLine = sf.readline()
    while recLine != "":
        fno = 0
        stID = ''
        myChar = ''
        for myChar in recLine:
            if myChar == '#':
                break
            else:
                stID += myChar
        if stID == searchID:
            found = True
        else:
            tf.write(recLine)

        recLine = sf.readline()

    if found is False:
        print(searchID, 'is not found')
    else:
        print(searchID, 'is deleted.')

    sf.close()
    tf.close()

    os.remove("PAFStudentsRecordS.txt")
    os.rename("tempStudentsRecordT.txt", "PAFStudentsRecordS.txt")

def readRecordWiseSeqFile():
    #complete record (all fields) with a separater character.
    sf = open("PAFStudentsRecordS.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stID = ''
        stName = ''
        stClass = ''
        stFee = ''
        for i in range(len(recline) - 1): # -1 to avoid \n
            myChar = recline[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                stID = stID + myChar
            elif fno == 1:
                stName = stName + myChar
            elif fno == 2:
                stClass = stClass + myChar
            else:
                stFee = stFee + myChar
        print("ID: " + stID, "Name: " + stName, "Class: " + stClass, \
            "Fee: " + str(stFee))
        recline = sf.readline()
    sf.close()

def searchRecordWiseSeqFile():
    #complete record (all fields) with a separater character.
    found = False
    searchID = input("Enter ID to search for: ")

    sf = open("PAFStudentsRecordS.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stID = ''
        stName = ''
        stClass = ''
        stFee = ''
        for i in range(len(recline) - 1): # -1 to avoid \n
            myChar = recline[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                stID = stID + myChar
            elif fno == 1:
                stName = stName + myChar
            elif fno == 2:
                stClass = stClass + myChar
            else:
                stFee = stFee + myChar
        if stID == searchID:
            found = True
            print("ID: " + stID, "Name: " + stName, "Class: " + stClass, \
                "Fee: " + str(stFee))
        recline = sf.readline()

    if found is False: print(searchID, 'is not found')
    sf.close()

def options():
    print("Field per line wise.")
    print("1. add")
    print("2. read")
    print("3. search")
    print("4. delete")
    print("5. edit")

    print("Record per line wise.")
    print("6. add")
    print("7. read")
    print("8. search")
    print("9. delete")
    print("10. edit")
    print("0. quit")
    x = int(input("enter option... "))
    return x

# main program
opt = options()
while opt != 0:
    # field wise sequential file
    if opt == 1: addFieldWiseSeqFile()
    if opt == 2: readFieldWiseSerialFile()
    if opt == 3:
        thisID = int(input("Enter ID to serach for: "))
        found = searchFieldWiseSeqFile(thisID, 1)
        if found is False:
            print(thisID, "is not found in file...")
    if opt == 4: deleteFieldWiseSeqFile()
    if opt == 5: editFieldWiseSeqFile()

    # record wise sequential file
    if opt == 6: addRecordWiseSeqFile()
    if opt == 7: readRecordWiseSeqFile()
    if opt == 8: searchRecordWiseSeqFile()
    if opt == 9: deleteRecordWiseSeqFile()
    if opt == 10: print("do it yourself...")
    opt = options()