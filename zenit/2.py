def najdiDelitele(x):
    delitele = []
    for i in range(x):
        if x % (i+1) == 0:
            delitele.append(i+1)
    return (delitele)

def jePrvocislo(y):
    l = najdiDelitele(y)
    if(len(l) == 2):
        return 1
    else:
        return 0

for i in range(40,1000):
    if (jePrvocislo(i) and jePrvocislo(i+2)):
        for j in range(2):
            print(str(i + 2*j), end =" ")