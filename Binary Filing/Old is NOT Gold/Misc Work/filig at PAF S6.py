"""
f = open("demofile.txt", "rt")
#print(f.read())
c=0
for x in f:
    c+=1
    if c == 2: print(x)
f.close()
"""

f = open("S6.txt","w")
f.write("Hello! A2S6.\n")
f.close()

f = open("S6.txt","r")
print(f.read())
f.close()
