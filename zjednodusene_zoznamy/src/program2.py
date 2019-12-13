f = open("../lib/zakaznici.txt", "r")
zoznam = f.readlines()
zoznam = [zoznam[i].strip() for i in range(len(zoznam))]
f.close()
print(zoznam)

zapnute = True

while(zapnute):
    print("Zadajte prikaz (pridaj, ukonci, vypis): ")
    prikaz = input()
    if(prikaz == "pridaj"):
        meno = input("Zadaj meno: ")
        suma = input("Zadajte sumu peňazí v celých €: ")
        try:
            int(suma)
            zoznam.append(meno)
            zoznam.append(suma)
            f = open("../lib/zakaznici.txt", "w")
            for i in zoznam:
                f.write(i + "\n")
            f.close()
        except ValueError:
            print("Neplatná suma")

    elif(prikaz == "vypis" and len(zoznam) > 0):
        for i in range(0, len(zoznam), 2):
            print("Účet " + zoznam[i] + ": " + zoznam[i+1] + "€")
    elif(prikaz == "ukonci"):
        zapnute = False
    else:
        print("Neplatný príkaz")
