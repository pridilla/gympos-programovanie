import string
list = ['Zr', 'Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B', 'Ba', 'Be', 'Bh', 'Bi', 'Bk', 'Br', 'C', 'Ca', 'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Cn', 'Co', 'Cr', 'Cs', 'Cu', 'Db', 'Ds', 'Dy', 'Er', 'Es', 'Eu', 'F', 'Fe', 'Fl', 'Fm', 'Fr', 'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'Hs', 'I', 'In', 'Ir', 'K', 'Kr', 'La', 'Li', 'Lr', 'Lu', 'Lv', 'Md', 'Mg', 'Mn', 'Mo', 'Mt', 'N', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'No', 'Np', 'O', 'Os', 'P', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re', 'Rf', 'Rg', 'Rh', 'Rn', 'Ru', 'S', 'Sb', 'Sc', 'Se', 'Sg', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm', 'U', 'Uuo', 'Uup', 'Uus', 'Uut', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn']
male = "kdumocflbpgyvnaetirhs"
velke = "ZGACOTKNHWBFUEIVDSLRXYMPQ"
velkel =[]
for i in velke:
    velkel.append(i)
dict = {'Z': ['r', 'n'], 'G': ['a', 'd', 'e'], 'A': ['c', 'g', 'l', 'm', 'r', 's', 't', 'u'], 'C': ['x', 'a', 'd', 'e', 'f', 'l', 'm', 'n', 'o', 'r', 's', 'u'], 'O': ['x', 's'], 'T': ['a', 'b', 'c', 'e', 'h', 'i', 'l', 'm'], 'K': ['x', 'r'], 'N': ['x', 'a', 'b', 'd', 'e', 'i', 'o', 'p'], 'H': ['x', 'e', 'f', 'g', 'o', 's'], 'W': ['x'], 'B': ['x', 'a', 'e', 'h', 'i', 'k', 'r'], 'F': ['x', 'e', 'l', 'm', 'r'], 'U': ['x', 'uo', 'up', 'us', 'ut'], 'E': ['r', 's', 'u'], 'I': ['x', 'n', 'r'], 'V': ['x'], 'D': ['b', 's', 'y'], 'S': ['x', 'b', 'c', 'e', 'g', 'i', 'm', 'n', 'r'], 'L': ['a', 'i', 'r', 'u', 'v'], 'R': ['a', 'b', 'e', 'f', 'g', 'h', 'n', 'u'], 'X': ['e'], 'Y': ['x', 'b'], 'M': ['d', 'g', 'n', 'o', 't'], 'P': ['x', 'a', 'b', 'd', 'm', 'o', 'r', 't', 'u']}
y = input()
y += "QQQ"
uprava = ""
hotovo = False

a = []

def dostan(x, uprava):
    global hotovo
    
    if velkel.count(x[0]) == 0:
        hotovo = True
    if(hotovo):
        return 0
    dalsie2 = str(x[1]).lower()
    dalsie3 = dalsie2 + str(x[2]).lower()
    if(x[0] == "Q"):
        a.append(uprava)
        hotovo = True
        return 0
    li = dict.get(x[0])
    if(li.count(dalsie2) == 1):
        uprava += str(x[0]) + dalsie2
        dostan(x[2:], uprava)
    if(li.count(dalsie3) == 1):
        uprava += str(x[0]) + dalsie3
        dostan(x[3:], uprava)
    if(li.count("x") == 1):
        uprava += str(x[0])
        dostan(x[1:], uprava)

dostan(y, "")
if(len(a) > 0):
    print(a[0])
else:
    print("neda sa")
    


