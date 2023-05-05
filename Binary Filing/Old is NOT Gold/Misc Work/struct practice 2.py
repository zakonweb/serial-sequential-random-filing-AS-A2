import os
import struct

class myRec: # udt for student record in a variable
    def __init__ (self):
        stID = 0
        stName = ''
        stClass = ''
        stFee = 0

format_string = 'i20s4sf'
record = ''
student = myRec()

stuFile = open('studentFile1.DAT', 'ab') # open file for binary write

student.stID = int(input("Enter student ID. (0 to end): "))
while student.stID !=0: # loop for each array element
    student.stName = input("Enter student name: ")
    student.stClass = input("Enter student class: ")
    student.stFee = float(input("Enter student fee: "))

    record = struct.pack('i20s4sf', student.stID, bytes(student.stName , 'ascii'), bytes(student.stClass, 'ascii'), student.stFee)
    stuFile.write(record) # write a whole record to the binary file
    student.stID = int(input("Enter student ID. (0 to end): "))
stuFile.close() # close file


stuFile = open('studentFile1.DAT', 'rb') # open file for binary read
student = myRec() # start with empty type
recNo = 0
recLen = struct.calcsize(format_string)
fileSize = stuFile.seek(0, os.SEEK_END)
records = int(fileSize/recLen)
record = ''

try:
    print('Number of records: ', int(fileSize/recLen))
    recNo = int(input("enter record number to search for (0 to end): "))
    while recNo != -1:
        stuFile.seek(recLen * recNo)
        record = stuFile.read(recLen)
        student.stID, student.stName, student.stClass, student.stFee = struct.unpack('i20s4sf', record)
        print(student.stID)
        print(student.stName.decode())
        print(student.stClass.decode())
        print(student.stFee)
        print()
        recNo = int(input("enter record number to search for (0 to end): ")) -1
except Exception as e:
    print(e)
stuFile.close()