import random

def jeAmstrongovo(x):
    r = 0
    for i in str(x):
        r += int(i)**3
    return r == x

def nahodneAmstrongovo():
    r = random.randrange(0, 1000)
    while jeAmstrongovo(r) != True:
        r -= 1
    return r

def rozdiel(x,y):
    if x > y:
        return x-y
    return y-x

zoznam = []
ide = True
while ide:
    x = input("Zadajte trojciferne cislo domu alebo koniec.\n")
    if(x == "koniec"):
        ide = False
    else:
        if(len(x) < 4):

            zoznam.append([0, int(x)])

for i in range(len(zoznam)):
    zoznam[i][0] = rozdiel(nahodneAmstrongovo(), zoznam[i][1])

zoznam = sorted(zoznam)
print(zoznam)