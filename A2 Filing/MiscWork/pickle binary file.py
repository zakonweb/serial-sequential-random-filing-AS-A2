import pickle # this library is required to create binary files
import random as r # this library is required to generate random numbers

class myRec: # udt for student record in a variable
    def __init__ (self):
        stID = 0
        stName = ''
        stClass = ''
        stFee = 0

st = myRec()
student = [myRec() for i in range(10)]
stuFile = open('studentFile.DAT', 'wb') # open file for binary write

for i in range(10): # loop for each array element
    student[i].stID = i
    student[i].stName = chr(65 + i)
    student[i].stClass = "AS-" + chr(65 + i)
    student[i].stFee = r.randint(1000, 25000)
    pickle.dump(student[i], stuFile) # write a whole record to the binary file
stuFile.close() # close file

stuFile = open('studentFile.DAT', 'rb') # open file for binary read
student = [] # start with empty list
i = 0

try:
    while True: # check for end of file
        st = pickle.load(stuFile)
        student.append(st) # append record from file to end of list
        print(student[i].stID)
        print(student[i].stName)
        print(student[i].stClass)
        print(student[i].stFee)
        i = i+1
        print()
except:
    pass
stuFile.close()