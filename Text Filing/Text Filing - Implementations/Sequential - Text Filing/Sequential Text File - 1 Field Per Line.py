# SEQUNTIAL FILE PRACTICES
# ONE FIELD PER LINE WISE
import os

def addFieldWiseSeq():
    try:
        sf = open("studentGALSeq.txt","rt")
    except:
        sf = open("studentGALSeq.txt","xt")
        sf = open("studentGALSeq.txt","rt")
    tf = open("temp.txt", "wt")

    stID = input("Enter student ID (Leave blank to end): ")
    if stID != "":
        stName = input("Enter Name: ")
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        added = False
        IDS = sf.readline()
        while IDS != '':
            nameS = sf.readline()
            classS = sf.readline()
            feeS = sf.readline()

            if int(IDS) > int(stID) and added is False:
                added = True
                tf.write(stID + "\n")
                tf.write(stName + "\n")
                tf.write(stClass + "\n")
                tf.write(str(stFee) + "\n")

            tf.write(IDS)
            tf.write(nameS)
            tf.write(classS)
            tf.write(feeS)

            IDS = sf.readline()
        if added == False:
            tf.write(stID + "\n")
            tf.write(stName + "\n")
            tf.write(stClass + "\n")
            tf.write(str(stFee) + "\n")
    sf.close()
    tf.close()
    os.remove("studentGALSeq.txt")
    os.rename("temp.txt", "studentGALSeq.txt")

def displayFieldWiseSeq():
    try:
        sf = open("studentGALSeq.txt","rt")
        stID = sf.readline()
        while stID != "":
            stName = sf.readline()
            stClass = sf.readline()
            stFee = sf.readline()

            print(stID, end='')
            print(stName, end='')
            print(stClass, end='')
            print(stFee)
            stID = sf.readline()

        sf.close()
    except:
        print("File doesn't exists...")

def searchFieldWiseSeq():
    found = False
    searchID = input("Enter ID to search for: ")
    try:
        sf = open("studentGALSeq.txt","rt")
        stID = sf.readline()
        while stID != "":
            stName = sf.readline()
            stClass = sf.readline()
            stFee = sf.readline()

            if int(searchID) == int(stID):
                found = True
                print(stID, end='')
                print(stName, end='')
                print(stClass, end='')
                print(stFee)
            stID = sf.readline()
        sf.close()
        if not found:
            print(searchID, "is not found...")
    except:
        print("File doesn't exists...")

def delFieldWiseSeq():
    found = False
    searchID = input("Enter ID to delete record: ")
    try:
        sf = open("studentGALSeq.txt","rt")
        tf = open("temp.txt","wt")

        stID = sf.readline()
        while stID != "":
            stName = sf.readline()
            stClass = sf.readline()
            stFee = sf.readline()

            if int(searchID) != int(stID):
                tf.write(stID)
                tf.write(stName)
                tf.write(stClass)
                tf.write(stFee)
            else:
                found = True
            stID = sf.readline()
        sf.close()
        tf.close()
        if not found:
            print(searchID, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("studentGALSeq.txt")
            os.rename("temp.txt","studentGALSeq.txt")
    except:
        print("File doesn't exists...")

def editFieldWiseSeq():
    found = False
    searchID = input("Enter ID to edit record: ")
    try:
        sf = open("studentGALSeq.txt","rt")
        tf = open("temp.txt","wt")

        stID = sf.readline()
        while stID != "":
            stName = sf.readline()
            stClass = sf.readline()
            stFee = sf.readline()

            if int(searchID) != int(stID):
                tf.write(stID)
                tf.write(stName)
                tf.write(stClass)
                tf.write(stFee)
            else:
                found = True
                print(stID, end='')
                print(stName, end='')
                print(stClass, end='')
                print(stFee)
                print("Now enter new data or enter blank to keep previous data.")
                # IDs are never updated
                sN = input("Enter updated name: ")
                if sN == "":
                    sN = stName.strip()
                sC = input("Enter updated class: ")
                if sC == "":
                    sC = stClass.strip()
                sF = input("Enter updated fee: ")
                if sF == "":
                    sF = stFee.strip()
                tf.write(stID)
                tf.write(sN + "\n")
                tf.write(sC + "\n")
                tf.write(sF + "\n")
            stID = sf.readline()
        sf.close()
        tf.close()
        if not found:
            print(searchID, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("studentGALSeq.txt")
            os.rename("temp.txt","studentGALSeq.txt")
    except:
        print("File doesn't exists...")

def options():
    print("Sequential File processing menu:")
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
    if opt == 1: addFieldWiseSeq()
    if opt == 2: displayFieldWiseSeq()
    if opt == 3: searchFieldWiseSeq()
    if opt == 4: delFieldWiseSeq()
    if opt == 5: editFieldWiseSeq()
    opt = options()