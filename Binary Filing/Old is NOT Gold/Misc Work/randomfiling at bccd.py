import struct
import os

class stuRec:
    def __init__(self):
        self.stuID = 0
        self.stuName = ''
        self.stuClass = ''
        self.stuFee = 0.0

def appendFile():
    myRec = stuRec()

    record_structure = 'i20s4sf'
    record_size = struct.calcsize(record_structure)
    sf = open("studentBCCD.dat", 'ab+')
    sf.seek(0, os.SEEK_END)
    file_size = sf.tell()
    totalRecords = int(file_size / record_size)

    myRec.stuName = input("Enter student name. (Leave blank to quit.): ")
    while myRec.stuName != '':
        totalRecords += 1
        myRec.stuID = totalRecords
        myRec.stuClass = input("Enter student class: ")
        myRec.stuFee = float(input("Enter student fee: "))

        record_buffer = struct.pack(record_structure, myRec.stuID, bytes(myRec.stuName, 'ascii'), \
                                    bytes(myRec.stuClass, 'ascii'), myRec.stuFee)
        sf.write(record_buffer)
        myRec.stuName = input("Enter student name. (Leave blank to quit.): ")
    sf.close()

def readFile():
    myRec = stuRec()

    record_structure = 'i20s4sf'
    record_size = struct.calcsize(record_structure)
    sf = open("studentBCCD.dat", 'rb')
    sf.seek(0, os.SEEK_END)
    file_size = sf.tell()
    totalRecords = int(file_size / record_size)

    for i in range(totalRecords):
        sf.seek(i * record_size)
        record_buffer = sf.read(record_size)
        myRec.stuID, myRec.stuName, myRec.stuClass, myRec.stuFee = struct.unpack(record_structure, record_buffer)
        print(myRec.stuID)
        print(myRec.stuName.decode())
        print(myRec.stuClass.decode())
        print(myRec.stuFee)
        print()
    sf.close()

# main program
#appendFile()
readFile()
