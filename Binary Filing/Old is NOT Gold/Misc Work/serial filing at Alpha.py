# serial file operations

def addFieldwiseSerialFile():
    sf = open("AlphaStudents.txt", "wt")

    stName = input("Enter name (blank for ending): ")
    while stName != "":
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        sf.write(stName + "\n")
        sf.write(stClass + "\n")
        sf.write(str(stFee) + "\n")

        stName = input("Enter name (blank for ending): ")
    sf.close()

def addRecordwiseSerialFile():
    sf = open("AlphaStudents1.txt", "wt")

    stName = input("Enter name (blank for ending): ")
    while stName != "":
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))
        sf.write(stName + "#" + stClass + "#" + str(stFee) + "\n")

        stName = input("Enter name (blank for ending): ")
    sf.close()

def readFieldwiseSerialFile():
    sf = open("AlphaStudents.txt", "rt")

    stName = sf.readline()
    while stName != "":
        stClass = sf.readline()
        stFee = sf.readline()
        print("Name: ", stName, end='')
        print("Class: ", stClass, end='')
        print("Fee: ", stFee, end='')

        stName = sf.readline()
    sf.close()

def readRecordwiseSerialFile():
    sf = open("AlphaStudents1.txt", "rt")
    recline = sf.readline()
    while recline != "":
        fno = 0
        stName = ''
        stClass = ''
        stFee = ''
        for i in range(len(recline) - 1):
            myChar = recline[i]
            if myChar == '#':
                fno += 1
                continue
            if fno == 0:
                stName = stName + myChar
            elif fno == 1:
                stClass = stClass + myChar
            else:
                stFee = stFee + myChar
        print(stName)
        print(stClass)
        print(str(stFee))
        recline = sf.readline()
    sf.close()

#main program
readRecordwiseSerialFile()