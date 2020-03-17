import os, tkinter
dirname = os.path.dirname(__file__)

filename = os.path.join(dirname, 'libs/udaje.txt')
f = open(filename, "r")
rawu = f.readlines()
f.close()

filename = os.path.join(dirname, 'libs/platby.txt')
f = open(filename, "r")
rawp = f.readlines()
f.close()

udaje = {}
for i in rawu:
    x = i.split()
    udaje[x[1] + " " + x[2]] = int(x[0])

platby = {}
for i in rawp:
    x = i.split()
    platby[x[0] + " " + x[1]] = int(x[2])


spolujr = []
spolusr = []
for i in list(udaje.keys()):
    vek = udaje[i]
    platba = platby[i]
    if vek > 16:
        spolusr.append([vek, i, platba])
    else:
        spolujr.append([vek, i, platba])

filename = os.path.join(dirname, 'libs/nad16.txt')
f = open(filename, "w")
for i in spolusr:
    f.write(str(i[0]) + " " + i[1] + " " + str(i[2]) + "\n")
f.close()

filename = os.path.join(dirname, 'libs/do16.txt')
f = open(filename, "w")
for i in spolujr:
    f.write(str(i[0]) + " " + i[1] + " " + str(i[2]) + "\n")
f.close()

while True:
    x = input("\n\nZadajte platby pre zobrazenie platieb. Zadajte udaje pre zobrazenie udajov. Ctr+C - ukoncenie.\n")
    if x == "platby":
        for i in rawp:
            print(i, end="")
    if x == "udaje":
        for i in rawu:
            print(i, end="")