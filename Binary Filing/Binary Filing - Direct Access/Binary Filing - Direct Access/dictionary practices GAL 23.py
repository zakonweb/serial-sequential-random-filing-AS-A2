names = ['' for i in range(5)]
i = 0
myFile = open('names.txt', 'rt')
x = myFile.readline()
while x != '':
    y = myFile.readline()
    dictItem = {"ID" : x.strip(), "Name" : y.strip()}
    names[i] = dictItem
    i = i + 1
    x = myFile.readline()
myFile.close()

for i in range(4):
    print(names[i]["ID"], names[i]["Name"])
