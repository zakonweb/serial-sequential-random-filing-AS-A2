# sequential file operations
import os

def addFieldWiseSeqFile():
    added = False
    try:
        sf = open("PAFStudentsFieldS.txt", "rt")
    except:
        sf = open("PAFStudentsFieldS.txt", "xt")
        sf = open("PAFStudentsFieldS.txt", "rt")

    tf = open("PAFStudentsFieldST.txt", "wt")

    ID = int(input("Enter ID: "))
    Name = input("Enter name: ")
    Class = input("Enter class: ")
    Fee = float(input("Enter fee: "))

    stID = sf.readline()
    while stID != "":
        stID = int(stID)
        stName = sf.readline()
        stClass = sf.readline()
        stFee = float(sf.readline())

        if stID > ID and not added:
            added = True
            # save new record
            tf.write(str(ID) + '\n')
            tf.write(Name + '\n')
            tf.write(Class + '\n')
            tf.write(str(Fee) + '\n')

        # save file record
        tf.write(str(stID) + '\n')
        tf.write(stName)
        tf.write(stClass)
        tf.write(str(stFee) + '\n')

        stID = sf.readline()

    if not added:
        tf.write(str(ID) + '\n')
        tf.write(Name + '\n')
        tf.write(Class + '\n')
        tf.write(str(Fee) + '\n')
    sf.close()
    tf.close()
    os.remove("PAFStudentsFieldS.txt")
    os.rename("PAFStudentsFieldST.txt", "PAFStudentsFieldS.txt")

def addRecordWiseSerialFile():
    sf = open("PAFStudentsRecord.txt", "at")

    stName = input("Enter name (blank for ending): ")
    while stName != "":
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        sf.write(stName + '#' + stClass + '#' + str(stFee) + '\n')

        stName = input("Enter name (blank for ending): ")
    sf.close()

def readFieldWiseSerialFile():
    sf = open("PAFStudentsField.txt", "rt")
    stName = sf.readline()
    while stName != "":
        stClass = sf.readline()
        stFee = float(sf.readline())

        #single field per line
        print(stName, end='')
        print(stClass, end='')
        print(str(stFee))
        stName = sf.readline()
    sf.close()

def searchFieldWiseSerialFile():
    found = False
    searchName = input("Enter name to search for: ")

    sf = open("PAFStudentsField.txt", "rt")
    stName = sf.readline()
    while stName != "":
        stClass = sf.readline()
        stFee = float(sf.readline())

        #single field per line
        #match after removing \n from string
        if stName[0:len(stName)-1] == searchName:
            found = True
            print(stName, end='')
            print(stClass, end='')
            print(str(stFee))
        stName = sf.readline()
    if found is False: print(searchName, 'is not found')
    sf.close()

def readRecordWiseSerialFile():
    #complete record (all fields) with a separater character.
    sf = open("PAFStudentsRecord.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stName = ''
        stClass = ''
        stFee = ''
        for i in range(len(recline) - 1): # -1 to avoid \n
            myChar = recline[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                stName = stName + myChar
            elif fno == 1:
                stClass = stClass + myChar
            else:
                stFee = stFee + myChar
        print(stName, stClass, str(stFee))
        recline = sf.readline()
    sf.close()

def searchRecordWiseSerialFile():
    #complete record (all fields) with a separater character.
    found = False
    searchName = input("Enter name to search for: ")

    sf = open("PAFStudentsRecord.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stName = ''
        stClass = ''
        stFee = ''
        for i in range(len(recline) - 1): # -1 to avoid \n
            myChar = recline[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                stName = stName + myChar
            elif fno == 1:
                stClass = stClass + myChar
            else:
                stFee = stFee + myChar
        if stName == searchName:
            found = True
            print(stName, stClass, str(stFee))
        recline = sf.readline()

    if found is False: print(searchName, 'is not found')
    sf.close()

def deleteFieldWiseSerialFile():
    found = False
    searchName = input("Enter name to delete record for: ")

    sf = open("PAFStudentsField.txt", "rt")
    tf = open("tempStudentsField.txt", "wt")

    stName = sf.readline()
    while stName != "":
        stClass = sf.readline()
        stFee = float(sf.readline())

        #single field per line
        #match after removing \n from string
        if stName[0:len(stName)-1] != searchName:
            tf.write(stName)
            tf.write(stClass)
            tf.write(str(stFee) + "\n")
        else:
            found = True
        stName = sf.readline()
    if found is False:
        print(searchName, 'is not found')
    else:
        print(searchName, 'is deleted.')
    sf.close()
    tf.close()
    os.remove("PAFStudentsField.txt")
    os.rename("tempStudentsField.txt", "PAFStudentsField.txt")

def deleteRecordWiseSerialFile():
    #complete record (all fields) with a separater character.
    found = False
    searchName = input("Enter name to delete record for: ")

    sf = open("PAFStudentsRecord.txt", "rt")
    tf = open("tempStudentsRecord.txt", "wt")

    recline = sf.readline()
    while recline != "":
        fno = 0
        stName = ''
        stClass = ''
        stFee = ''
        for i in range(len(recline) - 1): # -1 to avoid \n
            myChar = recline[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                stName = stName + myChar
            elif fno == 1:
                stClass = stClass + myChar
            else:
                stFee = stFee + myChar

        if stName == searchName:
            found = True
        else:
            tf.write(stName + '#' + stClass + '#' + stFee + '\n')

        recline = sf.readline()

    if found is False:
        print(searchName, 'is not found')
    else:
        print(searchName, 'is deleted.')

    sf.close()
    tf.close()

    os.remove("PAFStudentsRecord.txt")
    os.rename("tempStudentsRecord.txt", "PAFStudentsRecord.txt")

def editFieldWiseSerialFile():
    found = False
    searchName = input("Enter name to edit record for: ")

    sf = open("PAFStudentsField.txt", "rt")
    tf = open("tempStudentsField.txt", "wt")

    stName = sf.readline()
    while stName != "":
        stClass = sf.readline()
        stFee = float(sf.readline())

        #single field per line
        #match after removing \n from string
        if stName[0:len(stName)-1] == searchName:
            print(stName, end='')
            print(stClass, end='')
            print(str(stFee))
            print()

            print("Now reenter data for editing:")
            stName = input("Enter name: ") + "\n"
            stClass = input("Enter class: ") + "\n"
            stFee = float(input("Enter fee: "))
            found = True
        tf.write(stName)
        tf.write(stClass)
        tf.write(str(stFee) + "\n")

        stName = sf.readline()

    if found is False:
        print(searchName, 'is not found')
    else:
        print(searchName, 'is edited.')
    sf.close()
    tf.close()
    os.remove("PAFStudentsField.txt")
    os.rename("tempStudentsField.txt", "PAFStudentsField.txt")

def options():
    print("1. add field per line wise")
    print("2. read field per line wise")
    print("3. search field per line wise")
    print("4. delete field per line wise")
    print("5. edit field per line wise")
    print("6. add record per line wise")
    print("7. read record per line wise")
    print("8. search record per line wise")
    print("9. delete record per line wise")
    print("10. edit record per line wise")
    print("0. quit")
    x = int(input("enter option... "))
    return x

# main program
opt = options()
while opt != 0:
    if opt == 1: addFieldWiseSeqFile()
    if opt == 2: readFieldWiseSerialFile()
    if opt == 3: searchFieldWiseSerialFile()
    if opt == 4: deleteFieldWiseSerialFile()
    if opt == 5: editFieldWiseSerialFile()

    if opt == 6: addRecordWiseSerialFile()
    if opt == 7: readRecordWiseSerialFile()
    if opt == 8: searchRecordWiseSerialFile()
    if opt == 9: deleteRecordWiseSerialFile()
    if opt == 10: print("do it yourself...")
    opt = options()
