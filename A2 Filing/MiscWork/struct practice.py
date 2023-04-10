import pickle # this library is required to create binary files
import struct

class myRec: # udt for student record in a variable
    def __init__ (self):
        stID = 0
        stName = ''
        stClass = ''
        stFee = 0

student = myRec()
stuFile = open('studentFile.DAT', 'ab') # open file for binary write
record = ''
"""
student.stID = int(input("Enter student ID. (0 to end): "))
while student.stID !=0: # loop for each array element
    student.stName = input("Enter student name: ")
    student.stClass = input("Enter student class: ")
    student.stFee = float(input("Enter student fee: "))

    record = struct.pack('i20s4sf', student.stID, bytes(student.stName , 'ascii'), bytes(student.stClass, 'ascii'), student.stFee)
    pickle.dump(record, stuFile) # write a whole record to the binary file
    student.stID = int(input("Enter student ID. (0 to end): "))
stuFile.close() # close file
"""

stuFile = open('studentFile.DAT', 'rb') # open file for binary read
student = myRec() # start with empty list
recNo = 0
recLen = 0

try:
    #recNo = int(input("enter record number to search for: ")) -1
    stuFile.seek(39)
    record = pickle.load(stuFile)
    #recLen = len(record)
    record = pickle.load(stuFile)
    student.stID, student.stName, student.stClass, student.stFee = struct.unpack('i20s4sf', record)
    print(student.stID)
    print(student.stName.decode())
    print(student.stClass.decode())
    print(student.stFee)
    print()
except Exception as e:
    print(e)
stuFile.close()