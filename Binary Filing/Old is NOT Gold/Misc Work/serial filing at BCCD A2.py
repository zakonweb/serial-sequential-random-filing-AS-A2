# Serial File operations
import os

def addSerFileField():
    sf = open("SerFileBCCD.txt","at")

    stName = input("Enter student name: (blank to finish.): ")
    while stName != '':
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        sf.write(stName + "\n")
        sf.write(stClass + "\n")
        sf.write(str(stFee) + "\n")
        stName = input("Enter student name: (blank to finish.): ")
    sf.close()

def addSerFileRec():
    sf = open("SerFileBCCDRec.txt","at")

    stName = input("Enter student name: (blank to finish.): ")
    while stName != '':
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        sf.write(stName + "#" + stClass + "#" + str(stFee) + "\n")
        stName = input("Enter student name: (blank to finish.): ")
    sf.close()

def readSerFileField():
    try:
        sf = open("SerFileBCCD.txt","rt")

        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = float(sf.readline())

            print(stName, end='')
            print(stClass, end='')
            print(stFee)
            print()

            stName = sf.readline()
        sf.close()
    except:
        print("File doesn't exist...")

def delSerFileField():
    try:
        found = False
        searchName = input("Enter name to delete: ")

        sf = open("SerFileBCCD.txt","rt")
        tf = open("temp.txt", "wt")

        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = sf.readline()

            if stName.strip() != searchName:
                tf.write(stName)
                tf.write(stClass)
                tf.write(stFee)
            else:
                found = True
            stName = sf.readline()
        sf.close()
        tf.close()
        os.remove("SerFileBCCD.txt")
        os.rename("temp.txt","SerFileBCCD.txt")

        if found is False:
            print(searchName,"was not found...")
    except:
        print("File doesn't exist...")

def editSerFileField():
    try:
        found = False
        searchName = input("Enter name to edit: ")

        sf = open("SerFileBCCD.txt","rt")
        tf = open("temp.txt", "wt")

        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = sf.readline()

            if stName.strip() != searchName:
                tf.write(stName)
                tf.write(stClass)
                tf.write(stFee)
            else:
                found = True
                print(stName.strip(), stClass.strip(), stFee.strip())
                print()
                print("Now re-enter to edit record.")
                stName = input("Enter student name: ")
                stClass = input("Enter class: ")
                stFee = float(input("Enter fee: "))
                tf.write(stName + "\n")
                tf.write(stClass + "\n")
                tf.write(str(stFee) + "\n")
            stName = sf.readline()
        sf.close()
        tf.close()
        os.remove("SerFileBCCD.txt")
        os.rename("temp.txt","SerFileBCCD.txt")

        if found is False:
            print(searchName,"was not found...")
    except:
        print("File doesn't exist...")

def delSerFileRec():
    try:
        found = False
        searchName = input("Enter name to delete: ")

        sf = open("SerFileBCCDRec.txt","rt")
        tf = open("temp.txt", "wt")

        stRec = sf.readline()
        while stRec != "":
            stName = ''
            for i in range(len(stRec)-1): #stRec.strip()
                ch = stRec[i]
                if ch == '#':
                    break
                else:
                    stName += ch
            if stName != searchName:
                tf.write(stRec)
            else:
                found = True
            stRec = sf.readline()
        sf.close()
        tf.close()
        os.remove("SerFileBCCDRec.txt")
        os.rename("temp.txt","SerFileBCCDRec.txt")

        if found is False:
            print(searchName,"was not found...")
    except:
        print("File doesn't exist...")

def searchSerFileField():
    try:
        found = False
        searchName = input("Enter name to search for: ")
        sf = open("SerFileBCCD.txt","rt")

        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = float(sf.readline())
            if searchName == stName.strip():
                found = True
                print(stName, end='')
                print(stClass, end='')
                print(stFee)
                print()

            stName = sf.readline()
        sf.close()
        if found is False:
            print(searchName, "was not found...")
    except:
        print("File not found...")

def readSerFileRec():
    try:
        sf = open("SerFileBCCDRec.txt","rt")

        stRec = sf.readline()
        while stRec != "":
            fieldNo = 0
            stName = ''
            stClass = ''
            stFee = ''

            for i in range(len(stRec)-1): #stRec.strip()
                ch = stRec[i]
                if ch == '#':
                    fieldNo += 1
                else:
                    if fieldNo == 0:
                        stName = stName + ch
                    elif fieldNo == 1:
                        stClass = stClass + ch
                    else:
                        stFee = stFee + ch
            print(stName, stClass, stFee)
            stRec = sf.readline()
        sf.close()
    except:
        print("File doesn't exist...")

def searchSerFileRec():
    try:
        found = False
        searchName = input("Enter name to search for: ")
        sf = open("SerFileBCCDRec.txt","rt")

        stRec = sf.readline()
        while stRec != "":
            fieldNo = 0
            stName = ''
            stClass = ''
            stFee = ''
            for i in range(len(stRec)-1): #stRec.strip()
                ch = stRec[i]
                if ch == '#':
                    fieldNo += 1
                else:
                    if fieldNo == 0:
                        stName = stName + ch
                    elif fieldNo == 1:
                        stClass = stClass + ch
                    else:
                        stFee = stFee + ch
            if stName == searchName:
                found = True
                print(stName, stClass, stFee)
            stRec = sf.readline()
        if found is False:
            print(searchName, "was not found...")
        sf.close()
    except:
        print("File not found...")

def options():
    print("One field per line serial file ops.")
    print("1. Add")
    print("2. Read")
    print("3. Search")
    print("4. Delete")
    print("5. Edit")
    print()
    print("One record per line serial file ops.")
    print("6. Add")
    print("7. Read")
    print("8. Search")
    print("9. Delete")
    print("10. Edit")
    print()
    print("0. Quit")
    x = int(input("enter option... "))
    return x

# main program
opt = options()
while opt != 0:
    if opt == 1: addSerFileField()
    if opt == 2: readSerFileField()
    if opt == 3: searchSerFileField()
    if opt == 4: delSerFileField()
    if opt == 5: editSerFileField()

    if opt == 6: addSerFileRec()
    if opt == 7: readSerFileRec()
    if opt == 8: searchSerFileRec()
    if opt == 9: delSerFileRec()
    if opt == 10: print("do it yourself...")
    opt = options()