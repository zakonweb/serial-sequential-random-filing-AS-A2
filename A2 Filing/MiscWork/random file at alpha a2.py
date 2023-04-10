import struct
import os

class sRecType():
    def __init__(self):
        self.stID = 0
        self.stName = ''
        self.stClass = ''
        self.stFee = 0.0

myRec = sRecType()
recStructure = 'i20s4sf'
totalRecs = 0
recSize = 0
fileSize = 0
sf = open("alphaStu.DAT", 'ab+')
sf.seek(0, os.SEEK_END)
fileSize = sf.tell()
recSize = struct.calcsize(recStructure)
totalRecs = int(fileSize/recSize)

myRec.stID = totalRecs +1
print("ID:", myRec.stID)
myRec.stName = input("Enter name: ")
myRec.stClass = input("Enter class: ")
myRec.stFee = float(input("Enter fee: "))

package = struct.pack(recStructure, myRec.stID, bytes(myRec.stName, 'ascii'), \
                      bytes(myRec.stClass, 'ascii'), myRec.stFee)

sf.write(package)
sf.close()

# Reading all records
myRec = sRecType()
sf = open("alphaStu.DAT", 'rb')
sf.seek(0, os.SEEK_END)
fileSize = sf.tell()
recSize = struct.calcsize(recStructure)
totalRecs = int(fileSize/recSize)

for i in range(totalRecs):
    sf.seek(int(i * recSize))
    package = sf.read(recSize)
    myRec.stID, myRec.stName, myRec.stClass, myRec.stFee = \
        struct.unpack(recStructure, package)

    print("ID:", myRec.stID)
    print("Name:", myRec.stName.decode())
    print("Class:", myRec.stClass.decode())
    print("Fee:", myRec.stFee)
    print()

sf.close()