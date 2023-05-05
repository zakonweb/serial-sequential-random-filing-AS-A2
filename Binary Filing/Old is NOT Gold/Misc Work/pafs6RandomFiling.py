# ADD A RECORD TO RANDOM FILE
import struct
import os

class sRecType:
    def __init__(self):
        self.stuID = 0
        self.stuName = ''
        self.stuClass = ''
        self.stuFee = 0.0

myRec = sRecType()
record_format = 'i20s4sf'
record_size = struct.calcsize(record_format)
total_records = 0
file_size = 0

sf = open("pafs6.DAT", "ab+")
sf.seek(0, os.SEEK_END)
file_size = sf.tell()
total_records = int(file_size / record_size)

myRec.stuID = total_records + 1
print("ID: ", myRec.stuID)
myRec.stuName = input("Enter name: ")
myRec.stuClass = input("Enter class: ")
myRec.stuFee = float(input("Enter fee: "))

record_buffer = struct.pack(record_format, myRec.stuID, bytes(myRec.stuName , 'ascii'), \
                     bytes(myRec.stuClass, 'ascii'), myRec.stuFee)

sf.write(record_buffer)
sf.close()

#-----------------------------------------
sf = open("pafs6.DAT", "rb")
sf.seek(0, os.SEEK_END)
file_size = sf.tell()
total_records = int(file_size / record_size)

for i in range(total_records):
    sf.seek(int(i * record_size))
    record_buffer = sf.read(record_size)
    myRec.stuID, myRec.stuName, myRec.stuClass, \
    myRec.stuFee = struct.unpack(record_format, record_buffer)

    print("ID:", myRec.stuID)
    print("Name:", myRec.stuName.decode())
    print("Class:", myRec.stuClass.decode())
    print("Fee:", myRec.stuFee)

sf.close()