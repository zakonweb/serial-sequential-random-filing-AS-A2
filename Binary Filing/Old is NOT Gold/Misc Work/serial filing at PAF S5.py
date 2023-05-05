# serial file operations

def addSerialFile():
    sf = open("studentFieldWise.txt", "wt")

    StName = input("Enter name. (Blank to stop entry): ")
    while StName != "":
        StClass = input("Enter class: ")
        StFee = float(input("Enter fee: "))

        sf.write(StName + "\n")
        sf.write(StClass + "\n")
        sf.write(str(StFee) + "\n")

        StName = input("Enter name. (Blank to stop entry): ")
    sf.close()

def readSerialFile():
    sf = open("studentFieldWise.txt", "rt")

    StName = sf.readline()
    while StName != "":
        StClass = sf.readline()
        StFee = sf.readline()

        print(StName, end='')
        print(StClass, end='')
        print(str(StFee), end='')

        StName = sf.readline()
    sf.close()

def searchSerialFile():
    found = False
    searchName = input("Enter a name to search for: ")
    sf = open("studentFieldWise.txt", "rt")

    StName = sf.readline()
    while StName != "":
        StClass = sf.readline()
        StFee = sf.readline()

        if StName.strip() == searchName:
            found = True
            print(StName, end='')
            print(StClass, end='')
            print(str(StFee), end='')

        StName = sf.readline()
    sf.close()
    if found is False: print(searchName, 'is not found.')

def addRecordSerialFile():
    sf = open("studentRecordWise.txt", "wt")

    StName = input("Enter name. (Blank to stop entry): ")
    while StName != "":
        StClass = input("Enter class: ")
        StFee = float(input("Enter fee: "))

        sf.write(StName + "#" + StClass + "#" + str(StFee) + "\n")

        StName = input("Enter name. (Blank to stop entry): ")
    sf.close()

def readSerialRecordFile():
    sf = open("studentRecordWise.txt", "rt")

    recLine = sf.readline()
    while recLine != "":
        fno = 0
        StName = ''
        StClass = ''
        StFee = ''
        for i in range(len(recLine)-1):
            myChar = recLine[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                StName = StName + myChar
            elif fno == 1:
                StClass = StClass + myChar
            else:
                StFee = StFee + myChar
        print(StName, StClass, StFee)
        recLine = sf.readline()
    sf.close()

def searchSerialRecordFile():
    found = False
    searchName = input("Enter a name to search for: ")

    sf = open("studentRecordWise.txt", "rt")

    recLine = sf.readline()
    while recLine != "":
        fno = 0
        StName = ''
        StClass = ''
        StFee = ''
        for i in range(len(recLine)-1):
            myChar = recLine[i]
            if myChar == '#':
                fno += 1
            elif fno == 0:
                StName = StName + myChar
            elif fno == 1:
                StClass = StClass + myChar
            else:
                StFee = StFee + myChar

        if StName == searchName:
            found = True
            print(StName, StClass, StFee)
        recLine = sf.readline()
    sf.close()
    if found == False: print(searchName, "is not found.")

#addRecordSerialFile()
#readSerialRecordFile()
searchSerialRecordFile()