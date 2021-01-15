f = open("E:/filePractice/ABC.txt", "r")
lineCounter = 0
oneLine = f.readline()
while len(oneLine) > 0:
    oneLine = f.readline()
    lineCounter = lineCounter + 1

print("Number of lines in the file is =", lineCounter)