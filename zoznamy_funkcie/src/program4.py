retazecCisel = ""

def pomoc():
    print ("Hra Sestka je pre 6 hracov. Jeden hrac hadze kockou, az kym nepadnu za sebou dve sestky. Prvy hrac dostane tolko bodov, kolko medzitym padlo jednotiek, druhy hra tolko bodov, kolko padlo dvojok atd.\n\nNa vyzvu zadania cisla od 1 do 6 mozete zadat prirodzene cislo v tomto rozsahu alebo jeden z prikazov\nskore - pre priebezne vypisanie vysledkov\nkoniec - pre vypisanie skore a ukoncenie hry\npomoc - pre zopakovanie napovedy\n\nVela stastia!")
pomoc()

kon = 0

skore = []
uznaneCisla = []

for i in range(6):
    skore.append(0)
    uznaneCisla.append(str(i+1))

def vypisSkore():
    for i in range(6):
        print ("Hráč " + str(i+1) + " má zatiaľ počet bodov " + str(skore[i]) + ".")

def koniec():
    global kon
    kon = 1
    naj = 0
    for i in range(6):
        if(skore[naj] < skore[i]):
            naj = i
        print ("Hráč " + str(i+1) + " získal počet bodov " + str(skore[i]) + ".")
    print("Hru vyhral hráč " + str(naj+1) + ". Gratulujeme!")

def pridajBody():
    global retazecCisel
    if(len(retazecCisel) < 1):
        return
    for i in retazecCisel:
        skore[int(i)-1] += 1
    retazecCisel = ""

def pridajDoRetazca(x):
    global retazecCisel
    retazecCisel += x
    if(len(retazecCisel) >= 2 and retazecCisel[-2:] == "66"):
        pridajBody()
        vypisSkore()

while(kon == 0):
    inp = input("Zadajte číslo alebo príkaz: ")
    if(inp == "koniec"):
        koniec()
    elif(inp == "skore"):
        vypisSkore()
    elif(inp == "pomoc"):
        pomoc()
    elif(uznaneCisla.count(inp) > 0):
        pridajDoRetazca(inp)
    else:
        print("Nesprávny príkaz alebo neplatn číslo. Pre nápovedu zadajte pomoc.")