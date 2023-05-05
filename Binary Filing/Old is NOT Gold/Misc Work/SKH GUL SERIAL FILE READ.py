# SERIAL FILING READING
# ONE FIELD PER LINE

ID = 0
NAME = ""
CLASS = ""
FEE = 0.0

sf = open("SKHGUL.txt", "rt")
ID = sf.readline()
while ID != "":
    NAME = sf.readline()
    CLASS = sf.readline()
    FEE = sf.readline()

    print("ID: ", ID.strip())
    print("NAME: ", NAME.strip())
    print("CLASS: ", CLASS.strip())
    print("FEE: ", FEE)

    ID = sf.readline()
sf.close()