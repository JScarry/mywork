# messing with files
#Author: Jarlath Scarry

filename = "test.txt"
with open(filename, 'w+t') as f:
    f.write("Hello World")
    f.seek(0)
    data = f.readline()
    print(data)

print ("done")

with open("learningFiles.py", "r") as f:
    for line in f:
        print (line[:-1])

