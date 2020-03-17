import tkinter
from random import *
master = tkinter.Tk()
canvas = tkinter.Canvas(master,width = 640, height = 480, bg = 'green')
canvas.pack()
data = []
riadkov = 96   #v premennej riadkov si pamätáme počet riadkov cesty
cesta = [270]*riadkov   #Každý riadok cesty si pamätáme v zozname - x-ová súradnica ľavého okraja cesty

counter = 0
level = 0
cas = 45
posun = 1
dotyk = False
autop = False

def kresli_cestu():
    canvas.delete('cesta')
    for i in range(riadkov):
        canvas.create_rectangle(cesta[i], i*5, cesta[i]+100, i*5+5,fill = 'white', outline = '', tags = 'cesta')
"""
Funkcia najprv zmaže nakreslenú cestu (podľa tagu pre cestu)
for cyklom prejdeme všetky riadky cesty a podľa x-ovej súradnici v zozname cesta pre príslušný riadok nakreslíme biely obdĺžnik (cestu)
Y-ovú súradnicu si nemusíme pamätať, každý riadok má výšku 10 pixelov tak ju vypočítame podľa i
V časovači zavoláme funkciu posun_cestu(), ktorá posunie cestu o jeden riadok dole a vygeneruje nový riadok
Následne sa cesta vykreslí a plánuje sa ďalšie spustenie animácie
"""
def animacia():
    global counter, level, dotyk
    if dotyk == True:
        return
    posun_cestu()
    kresli_cestu()
    kresli_auto()
    canvas.after(100, animacia)
    counter -= 1
    if (counter < 1):
        counter = 10000
        level += 1
        canvas.create_text (150, 440, text = "level " + str(level))


def posun_cestu():
    global posun
    novy = cesta[0] + randint(-posun, posun)*5
    if novy < 0:
        novy = 0
    if novy > 540:
        novy = 540
    cesta.insert(0, novy)
    cesta.pop()

"""
tu vypočítame súradnicu nového riadku, ktorý sa vloží na vrch plátna zo súradnice terajšieho nultého riadku a k nemu pričítame náhodne
+10 alebo 0 alebo -10 (treba si uvedomiť, že k tomu nepotrebujeme if)
If-om ošetríme, aby nová súradnica nebola mešia ako 0 a väčšia ako 540 (640 - 100)- aby ostala na plátne
novú x-ovú súradnicu nultého riadku vložíme na začiatok zoznamu metódou insert.
zároveň z konca zoznamu odoberieme posledný riadok metódou pop()
"""
def animacia():
    global counter, level, cas, posun, dotyk, autop, cesta, autox, data
    data.append([autox, cesta[93]])
    if dotyk == True:
        return
    posun_cestu()
    kresli_cestu()
    kresli_auto()
    if autop:
        while(cesta[93] + 40 > autox):
            vpravo("")
        while(cesta[93]+40 < autox):
            vlavo("")
    counter -= 1
    if (counter < 1):
        if(cas>3):
            cas = int(cas *4/5)
        else:
            posun += 1
        canvas.delete("level")
        counter = 300
        level += 1
        canvas.create_text (50, 440, text = "level " + str(level), tag = "level")
    canvas.after(cas, animacia)

def kresli_auto():
    global dotyk, autox, autoy
    bodyx = [autox-1,autox+21]
    bodyy = [autoy-1, autoy+21]
    for i in bodyx:
        for j in bodyy:
            x=canvas.find_overlapping(i,j,i,j)
            if len(x)<1:
                dotyk = True
                prehra()
                return

    canvas.delete('auto')
    canvas.create_rectangle(autox, autoy, autox+20, autoy+20, fill = 'red',tags = 'auto')

#pohyb auta v smere osi x
    
def vlavo(event):
    global autox
    autox -= 6 

def vpravo(event):
    global autox
    autox += 6

def prehra():
    global data
    canvas.unbind_all("<Left>")
    canvas.unbind_all("<Right>")
    canvas.delete(tkinter.ALL)
    f = open("data.txt", "w")
    for i in data:
        f.write(i[0] + " "+ i[1] + "\n")
    f.close()
    canvas.create_text(320, 240, text="Gratulujeme. Úspešne si prehral!", fill="white", font="arial 20 bold")

autox = 310   #globálne premenné autox a autoy a s hodnotami tak, aby bolo auto v strede cesty
autoy = 450
canvas.bind_all('<Left>', vlavo)
canvas.bind_all('<Right>', vpravo)
animacia()

def autopilot():
    global autop
    canvas.unbind_all("<Left>")
    canvas.unbind_all("<Right>")
    autop = True

but = tkinter.Button(master, text = "Autopilot", command=autopilot)
but.pack()
master.mainloop()
#kresli_auto()

