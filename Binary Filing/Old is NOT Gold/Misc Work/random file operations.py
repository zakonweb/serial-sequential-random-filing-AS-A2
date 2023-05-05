# RANDOM FILE PRACTICES
# FIXED LENGTH RECORDS

import os
import struct

class stuType():
    def __init__(self):
        self.stuID = 0
        self.stuName = ''
        self.stuClass = ''
        self.stuFee = 0.0

record_format = "i20s4sf"
record_size = struct.calcsize(record_format)
stuRec = stuType()
records = 0

def addRec():
    global records
    sf = open("studentRand.DAT","ab")
    records += 1
    stuRec.stID = records

    print("New ID:", stuRec.stID)
    stuRec.stName = input("Enter Name: ")
    stuRec.stClass = input("Enter class: ")
    stuRec.stFee = float(input("Enter fee: "))

    buffer = struct.pack(record_format, stuRec.stID, bytes(stuRec.stName, 'ascii'), \
                        bytes(stuRec.stClass, 'ascii'), stuRec.stFee)
    sf.write(buffer)
    sf.close()

def displayAllRec():
    if records == 0:
        print("There are no records to read...")
    try:
        sf = open("studentRand.DAT","rb")
        for i in range(records):
            sf.seek(i * record_size)
            buffer = sf.read(record_size)
            stuRec.stID, stuRec.stName, stuRec.stClass, stuRec.stFee = struct.unpack(record_format, buffer)

            print(stuRec.stID)
            print(stuRec.stName.decode())
            print(stuRec.stClass.decode())
            print(stuRec.stFee)
            print()
        sf.close()
    except:
        print("File doesn't exists...")

def searchRec():
    found = False
    searchID = int(input("Enter ID to search for: ")) -1
    try:
        sf = open("studentRand.DAT","rb")
        sf.seek(searchID * record_size)
        buffer = sf.read(record_size)
        stuRec.stID, stuRec.stName, stuRec.stClass, stuRec.stFee = struct.unpack(record_format, buffer)

        print(stuRec.stID)
        print(stuRec.stName.decode())
        print(stuRec.stClass.decode())
        print(stuRec.stFee)
        print()
        sf.close()
    except:
        print("ID" , searchID+1, "couldn't be found...")
'''
def delRec():
    global records
    found = False
    searchID = input("Enter ID to delete record: ")
    try:
        sf = open("studentRand.DAT","rb")
        tf = open("temp.DAT","wb")

        for i in range(records):
            sf.seek(i * record_size)
            buffer = sf.read(record_size)
            stuRec.stID, stuRec.stName, stuRec.stClass, stuRec.stFee = struct.unpack(record_format, buffer)

            if int(searchID) != stuRec.stID:
                tf.write(buffer)
            else:
                found = True
                records -= 1
        sf.close()
        tf.close()

        if not found:
            print(searchID, "is not found...")
            os.remove("temp.DAT")
        else:
            print(searchID, "is deleted...")
            os.remove("studentRand.DAT")
            os.rename("temp.DAT", "studentRand.DAT")
    except Exception as e:
        print(e)
'''

def delRec():
    global records
    found = False
    recList = []
    searchID = input("Enter ID to delete record: ")
    try:
        sf = open("studentRand.DAT","rb")

        for i in range(records):
            sf.seek(i * record_size)
            buffer = sf.read(record_size)
            stuRec.stID, stuRec.stName, stuRec.stClass, stuRec.stFee = \
            struct.unpack(record_format, buffer)

            if int(searchID) != stuRec.stID:
                recList.append(buffer)
            else:
                found = True
                records -= 1
        sf.close()

        if not found:
            print(searchID, "is not found...")
        else:
            sf = open("studentRand.DAT","wb")
            for i in range(len(recList)):
                sf.write(recList[i])
            sf.close()
            print(searchID, "is deleted...")

    except Exception as e:
        print(e)

def editRec():
    searchID = int(input("Enter ID/record number to edit record: ")) -1
    try:
        sf = open("studentRand.DAT","rb+")
        sf.seek(searchID * record_size)
        buffer = sf.read(record_size)
        stuRec.stID, stuRec.stName, stuRec.stClass, stuRec.stFee = struct.unpack(record_format, buffer)

        print(stuRec.stID)
        print(stuRec.stName.decode())
        print(stuRec.stClass.decode())
        print(stuRec.stFee)
        print()

        print("Now enter updated data (leave blank to carry same data...)")
        ID = input("Enter ID: ")
        Name = input("Enter Name: ")
        Class = input("Enter class: ")
        Fee = input("Enter fee: ")

        if ID == '':
            ID = int(stuRec.stID)
        else:
            ID = int(ID)

        if Name == '': Name = stuRec.stName.decode()
        if Class == '': Class = stuRec.stClass.decode()
        if Fee == '':
            Fee = float(stuRec.stFee)
        else:
            Fee = float(Fee)
        buffer = struct.pack(record_format, ID, bytes(Name, 'ascii'), bytes(Class, 'ascii'), Fee)

        sf.seek(searchID * record_size)
        sf.write(buffer)
        sf.close()
        print("Record updated.")
    except:
        print("ID" , searchID+1, "couldn't be found...")

def options():
    print("Random File processing menu:")
    print("1. Add record.")
    print("2. Read/Travers complte record.")
    print("3. Search file.")
    print("4. Delete file.")
    print("5. Edit record.")
    print("0. Quit.")
    opt = int(input("Enter the choice... "))
    return opt

# main program
try:
    sf = open("studentRand.DAT","rb")
    # go to end of file to calculate the file size in bytes
    sf.seek(0, os.SEEK_END)
    fileSize = sf.tell()
    records = int(fileSize/record_size)
    sf.close
except:
    records = 0

opt = options()
while opt != 0:
    if opt == 1: addRec()
    if opt == 2: displayAllRec()
    if opt == 3: searchRec()
    if opt == 4: delRec()
    if opt == 5: editRec()
    opt = options()