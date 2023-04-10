# SERIAL FILING
# ONE FIELD PER LINE

ID = 0
NAME = ""
CLASS = ""
FEE = 0.0

sf = open("SKHGUL.txt", "at")
ID = int(input("Enter ID. (0 to end...): "))
while ID != 0:
    NAME = input("Enter name: ")
    CLASS = input("Enter class: ")
    FEE = float(input("Enter fee: "))

    sf.write(str(ID) + "\n")
    sf.write(NAME + "\n")
    sf.write(CLASS + "\n")
    sf.write(str(FEE) + "\n")
    ID = int(input("Enter ID. (0 to end...): "))
sf.close()