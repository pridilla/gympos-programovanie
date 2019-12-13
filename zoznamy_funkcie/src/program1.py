import random, tkinter

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

def rozkladPrvocisla(q):
    rozklad = {}
    prv = najdiPrvocisla(q)
    for i in prv:
        pocet = 1
        while(q % i**(pocet+1) == 0 and q >= i**(pocet+1)):
            pocet +=1
        rozklad[i] = pocet
    return rozklad

def rozkladCifry(s):
    rozklad = []
    ss = str(s)
    for i in ss:
        rozklad.append(int(i))
    return rozklad

def jeDokonale(t):
    suc = 0
    for i in najdiDelitele(t):
        suc += i
    if(2*t == suc):
        return 1
    return 0

def cifSucet(u):
    suc = 0
    for i in rozkladCifry(u):
        suc += i
    return suc

def jeAmstrongovo(v):
    suc = 0
    for i in rozkladCifry(v):
        suc += i**3
    if(suc == v):
        return 1
    return 0

def nsd(a,b):
    ad = rozkladPrvocisla(a)
    bd = rozkladPrvocisla(b)
    ak = set(list(ad.keys()))
    bk = set(list(bd.keys()))
    res = list(ak - bk) + list(bk)
    sucin = 1
    for i in res:
        sucin *= i**min(ad.get(i, 0), bd.get(i, 0))
    return sucin

def faktorial(c):
    if c == 0:
        return 1
    suc = 1
    for i in range(c):
        suc *= i+1
    return suc

def intervalFaktorial(c, d):
    if c == 0:
        return faktorial(d)
    suc = 1
    for i in range(c, d+1):
        suc *= i
    return suc

def kombinovane(n,k):
    return intervalFaktorial(n-k+1, n)/faktorial(k)

canvas = tkinter.Canvas(width = 300, height = 300)
canvas.pack()

def jeParne(x):
    if najdiDelitele(x).count(2) > 0:
        return "Číslo je párne."
    return "Číslo je nepárne"

def pyramida(n):
    rozmer = 30
    for i in range(n+1):
        for j in range(i+1):
            y = 20 + i*30
            x = y/2 + 20 + (n+1)*rozmer/2 + (j/2 - j)*30*2
            canvas.create_text(x,y,text=str(int(kombinovane(i,j))))

inp = input("Zadajte cele cislo: ")
inp = int(inp)
print(jeParne(inp))
if(jePrvocislo(inp)==1):
    print("Číslo je prvočíslo.")
else:
    print("Číslo nie je prvočíslo.")
print("Počet deliteľov čísla je " + str(len(najdiDelitele(inp))))
print("Delitele čísla sú " + str(najdiDelitele(inp)))
r = random.randint(2,9)
print("Náhodne vygenerované číslo: " + str(r))
print("Najväčší spoločný násobok týchto dvoch čísel je " + str(nsd(r, inp)))

print("\n")
inpi = jeDokonale(inp)
if(inpi==1):
    print("Číslo je dokonalé.")
else:
    print("Číslo nie je dokonalé.")

inpi = jeAmstrongovo(inp)
if(inpi==1):
    print("Číslo je amstrongovo číslo.")
else:
    print("Číslo nie je amstrongovo číslo.")

r = random.randint(2,9)
print("Náhodne vygenerované číslo: " + str(r))

if(najdiDelitele(inp).count(r) > 0):
    print("Číslo je deliteľné vygenerovaným číslom.")
else:
    print("Číslo nie je deliteľné vygenerovaným číslom.")


print("Faktoriál čísla je " + str(faktorial(inp)) + ".")
if(inp < r):
    print("Kombinačné číslo nemožno vypočítať")
else:
    print("Kombinačné číslo je " + str(kombinovane(inp, r)))
pyramida(inp)

canvas.mainloop()