cislo = int(input("Zadajte číslo: "))

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

def najdiPrvocisla(z):
    if(z == 1):
        return []
    m = najdiDelitele(z)
    prvocisla = []
    for j in m:
        if jePrvocislo(j) == 1:
            prvocisla.append(j)
    return prvocisla

print("Prvočíselne delitele čísla " + str(cislo) + " sú: " + str(najdiPrvocisla(cislo)))