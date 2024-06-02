import os

myPath = os.getcwd()
files = os.listdir(myPath)

for f in files:
    if f.endswith("xyz"):
        print("converting ", f, end=' ')
        fx = open(f)
        lines = fx.readlines()
        fx.close()
        data = ((lines[0]).split(","))
        mytype = data[0]
        mynewfilename = mytype + ".csv"
        print("to ", mynewfilename, "   ...", end='')
        new_file = open(mynewfilename, "w")
        for line in lines:
            new_file.write(line)
        new_file.close()
        print("done.")
        os.remove(f)
