import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

suborr = open('../lib/anketa.txt', 'r', encoding="cp1250")

otazka = suborr.readline().strip()
celkovy_pocet = 0
najvyssi_pocet = 0

def dlzka(x, y):
    return int(x*200/y)

def riadok(x, y, dlzka, rekord = 0):
    farba = "green"
    if rekord == 1:
        farba = "red"
    canvas.create_rectangle(x,y,x+dlzka,y+20, fill = farba, outline = 'black', tags = "graf")

def vypis(x, y, itext, ip, inp, i):
    canvas.create_text(x, y, text = itext + " (" + str(int(ip*100/celkovy_pocet)) + " %)", anchor = tkinter.E, tags =("moznost " + str(i), "graf"))

def update(array):
    canvas.delete("graf")
    for i in range(len(array)):
        global najvyssi_pocet
        if array[i][1] > najvyssi_pocet:
            najvyssi_pocet = array[i][1]

        vypis(150, 110 + i * 20, array[i][0], array[i][1], najvyssi_pocet, i)
        stav = 0
        if najvyssi_pocet == array[i][1]:
            stav = 1
        riadok(170, 100 + i * 20, dlzka(array[i][1], celkovy_pocet), stav)

def add(i):
    global celkovy_pocet
    global zoznam
    zoznam[i][1] += 1
    celkovy_pocet += 1
    update(zoznam)
    file_update()

def file_update():
    suborr = open('../lib/anketa.txt', 'w', encoding="cp1250")
    suborr.write(otazka)
    for i in range(len(zoznam)):
        for j in range(len(zoznam[i])):
            suborr.write("\n")
            suborr.write(str(zoznam[i][j]))
    suborr.close()

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

    zoznam.append([polozka, pocet])

suborr.close()

canvas.create_text(200, 10, text=otazka, fill = "red", font = "Arial 20 bold")
update(zoznam)

buttons = []

for i in range(len(zoznam)):
    buttons.append(tkinter.Button(text = zoznam[i][0], command = lambda a=i : add(a)))
    buttons[i].pack()
    print(i)

    canvas.tag_bind('moznost ' + str(i), '<Button-1>', lambda event, a = i: add(a))

canvas.mainloop()