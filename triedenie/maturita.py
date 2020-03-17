import random

studentov = 30
otazok = 50

while True:
    studentov = int(input("Zadajte pocet studentov: "))
    otazok = int(input("Zadajte pocet otazok: "))
    if(studentov > otazok):
        print("Otázok nesmie byt menej ako studentov.")
    else:
        break

otazky = []
for i in range(otazok):
    otazky.append(str(i+1))

studenti = []
for i in range(studentov):
    studenti.append(str(i+1))

def utriedSelectionSortX(polein, ind):
    pole = list(polein)
    if len(pole) == 0:
        return []
    najmensie = int(pole[0][ind])
    index = 0
    for i in range(len(pole)):
        if najmensie > int(pole[i][ind]):
            najmensie = int(pole[i][ind])
            index = i
    najmesniepole = [pole[index]]
    pole[index]=pole[0]
    npole = najmesniepole
    rpole = utriedSelectionSortX(pole[1:], ind)
    return npole + rpole

def rpops():
    global studenti
    index = random.randint(0, len(studenti)-1)
    r = studenti[index]
    studenti.pop(index)
    return r

def rpopo(modulo):
    global otazky
    funkcia = True ### Mozno zakomentovat
    r = random.choice(otazky)
    if(funkcia):
        while int(r) % 2 != modulo:
            r = random.choice(otazky)
    for i in range(len(otazky)):
        if(otazky[i] == r):
            otazky.pop(i)
            break        
    return r

poradie = []
for i in range(len(studenti)):
    poradie.append([i+1, rpops(), rpopo(i%2)])

print("")
print("Podľa poradia: ")
for i in poradie:
    print(str(i[0]) + ". -> studetn c." + str(i[1]) + " s otazkou " + str(i[2]))
print("")

print("Podľa studenta: ")
for i in utriedSelectionSortX(poradie, 1):
    print("Student c."+ str(i[1]) + " -> v poradi je " + str(i[0]) + ". s otazkou " + str(i[2]))
print("")

print("Podľa otázky: ")
for i in utriedSelectionSortX(poradie, 2):
    print("Otazka c."+ str(i[2]) + " -> v poradi je " + str(i[0]) + "., student c." + str(i[1]))
print("")