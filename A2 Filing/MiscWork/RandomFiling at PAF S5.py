# Write your code here :-)
import struct
import os

class sRecType:
    def __init__(self):
        self.stuID = 0
        self.stuName = ''
        self.stuClass = ''
        self.stuFee = 0.0

myRec = sRecType()
recFormat = 'i20s4sf'
totalRecs = 0

sf = open('PAFs5Ran.DAT','a+b')
sf.seek(0, os.SEEK_END)
totalRecs = sf.tell()/struct.calcsize(recFormat)

myRec.stuID = int(totalRecs) +1
print("ID:", myRec.stuID)
myRec.stuName = input("Enter name: ")
myRec.stuClass = input("Enter class: ")
myRec.stuFee = float(input("Enter fee: "))

buffer = struct.pack(recFormat, myRec.stuID, \
         bytes(myRec.stuName, 'ascii'), \
         bytes(myRec.stuClass, 'ascii'), myRec.stuFee)

sf.seek(int(totalRecs * struct.calcsize(recFormat)))
sf.write(buffer)
sf.close()

# reading all records
myRec = sRecType()
recFormat = 'i20s4sf'
totalRecs = 0
buffer = ''
sf = open('PAFs5Ran.DAT','rb')
sf.seek(0, os.SEEK_END)
totalRecs = int(sf.tell()/struct.calcsize(recFormat))

for i in range(totalRecs):
    sf.seek(int(i * struct.calcsize(recFormat)))
    buffer = sf.read(struct.calcsize(recFormat))
    myRec.stuID, myRec.stuName, myRec.stuClass, myRec.stuFee = struct.unpack(recFormat, buffer)

    print("ID:" , myRec.stuID)
    print("Name:" , myRec.stuName.decode())
    print("Class:" , myRec.stuClass.decode())
    print("Fee:" , myRec.stuFee)
    print()

sf.close()
