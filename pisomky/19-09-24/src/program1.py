import string

subor = open('../lib/vstupp1.txt','r')
lines = subor.readlines()
subor.close()

samohlasky = ['a', 'e', 'i', 'o', 'u', 'y']
spoluhlasky = []
spoluhlasky_pocet = []

for i in range(len(lines)):
    lines[i] = lines[i].strip()

if(lines[-1]==""):
    lines.remove[-1]
print("Pocet riadkov v dokumente je " + str(len(lines)) + ".")

for i in string.ascii_lowercase:
    if samohlasky.count(i) == 0:
        spoluhlasky.append(i)

dlzka = 0
najdlhsi = ""
for i in lines:
    if len(i) > dlzka:
        dlzka = len(i)
        najdlhsi = i
najdlhsi = najdlhsi.replace(" ", '')
print("Pocet znakov bez medzier v najdlsom riadku je " + str(len(najdlhsi)) + ".")

posledny_riadok = lines[-1]
posledny_riadok = posledny_riadok.strip()
posledny_riadok.replace(" ", '')
posledny_riadok.lower()
pocet_spoluhlasok = 0
for i in spoluhlasky:
    spoluhlasky_pocet.append([i, posledny_riadok.count(i)])
    pocet_spoluhlasok += posledny_riadok.count(i)
print("Pocet spoluhlasok v poslednom riadku je " + str(pocet_spoluhlasok) + ".")
for i in spoluhlasky_pocet:
    if(i[1] == 0):
        continue 
    print("Spoluhlaska " + i[0] + " sa nachadza v poslednom riadku " + str(i[1]) + "-krat.")

subor = open("../lib/ridilla_1sk.txt", "w")
for i in range(len(lines)):
    for j in range(len(lines[-i -1])):
        subor.write(lines[-i-1][-j-1])
    subor.write("\n")
subor.close()