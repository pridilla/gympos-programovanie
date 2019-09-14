import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

suborr = open('../lib/anketa.txt', 'r', encoding="cp1250")

otazka = suborr.readline().strip()
celkovy_pocet = 0
najvyssia_polozka = ""
najvyssi_pocet = 0

def dlzka(x, y):
    return int(x*100/y)

def riadok(x, y, dlzka, rekord = 0):
    farba = "green"
    if rekord == 1:
        farba = "red"
    canvas.create_rectangle(x,y,x+dlzka,y+20, fill = farba, outline = 'black')

def vypis(x, y, itext, ip, inp, i):
    canvas.create_text(x, y, text = itext + " (" + str(int(ip*100/celkovy_pocet)) + " %)", anchor = tkinter.E, tags ="moznost " + str(i) )

def update(array):
    for i in range(len(array)):
        if(najvyssi_pocet == array[i][1]):
            vypis(200, 105 + i * 20, array[i][0], array[i][1], najvyssi_pocet, i, 1)
        riadok(230, 100 + i * 20, dlzka(array[i][1], najvyssi_pocet))

zoznam = []
while True:
    polozka = suborr.readline().strip()
    if polozka == "":
        break
    pocet = suborr.readline().strip()
    if pocet == "":
        break
    pocet = int(pocet)
    celkovy_pocet = celkovy_pocet + pocet
    if pocet > najvyssi_pocet:
        najvyssi_pocet = pocet
        najvyssia_polozka = polozka

    zoznam.append([polozka, pocet])

suborr.close()

canvas.create_text(200, 10, text=otazka, fill = "red", font = "Arial 20 bold")
update(zoznam)

canvas.mainloop()