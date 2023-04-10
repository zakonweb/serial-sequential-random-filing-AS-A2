import pickle # this library is required to create binary files
import datetime

class StuRecord: # declaring a class without other methods
    def __init__(self): # constructor
        self.StuID = 0
        self.StuName = ""
        self.DateOfBirth = datetime.datetime.now()
        self.StuClass = ""
        self.StuFee = 0.0

SR = StuRecord()
studentFile = open("student.DAT","w+b")

SR.StuID = input("Enter ID: ")
SR.StuName = input("Enter name: ")
print("Enter DOB:")
year = int(input("Enter year (yyyy): "))
month = int(input("Enter month (mm): "))
day = int(input("Enter day (dd): "))
SR.DateOfBirth = datetime.datetime(year, month, day)
SR.StuClass = input("Enter class: ")
SR.StuFee = input("Enter fee: ")

pickle.dump(SR, studentFile)
studentFile.close()

studentFile = open("student.DAT","rb")
SR = pickle.load(studentFile)
print("Student ID:", SR.StuID)
print("Student name:", SR.StuName)
print("Student DOB:", SR.DateOfBirth)
print("Student class:", SR.StuClass)
print("Student fee:", SR.StuFee)
studentFile.close()