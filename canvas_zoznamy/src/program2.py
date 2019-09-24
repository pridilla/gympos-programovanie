subor = open('../lib/skok_do_dialky.txt', 'r')

data = []
krajiny = []
naj_vysledky = []
naj = []

while True:
    line = subor.readline()
    if line == "":
        break
    line = line.strip()
    data_short = line.split(' ')

    vysledky = []
    for i in range(5):
        vysledky.append(int(data_short[2+i]))
    najvyssie = max(vysledky)

    data_later = [data_short[0], data_short[1], najvyssie]
    data.append(data_later)
    krajiny.append(data_short[1])
    naj_vysledky.append(najvyssie)

zoznam_krajin = list(dict.fromkeys(krajiny))
print("Zucastnilo sa " + str(len(zoznam_krajin)) + " krajin.\n")

for i in zoznam_krajin:
    print("Z " + i + " sa zucastnilo " + str(krajiny.count(i)) + " ucastnikov.")
print()

rekord = max(naj_vysledky)
for i in data:
    if(rekord == i[2]):
        naj.append(i[0])
print("Rekord " + str(rekord) + " dosiahli ", end='')
for i in naj:
    print(i, end=',')
print()
print()




