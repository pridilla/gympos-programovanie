file = open("data.txt", "r")
data_raw = file.readlines()
file.close()

kapacita = int(data_raw[0])
data = []
for i in data_raw[1:]:
    slova = i.strip().split()
    zastavka = slova[2]
    if (len(slova)>3):
        zastavka += " " + slova[3]
    data.append([int(slova[0]), int(slova[1]), zastavka])

print("Pocet zastavok: " + str(len(data)))
print("Zastavky: ", end="")
for i in data:
    print(i[2], end= ", ")
print("")

max = 0
volne = kapacita
for i in data:
    volne -= i[0]
    volne += i[1]
    if(volne < 0):
        print(i[2] + ": " + "Povolena kapacita prekrocena o " + str(-(volne)))
        if(-volne > max):
            max = -volne
print("Najvyssie prekrocenie: " + str(max))            

