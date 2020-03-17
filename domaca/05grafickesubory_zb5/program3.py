import tkinter

master = tkinter.Tk()

nameframe = tkinter.Frame(master)
nameframe.pack()
namelabel = tkinter.Label(nameframe, text="Zadajte meno studenta: ")
namelabel.pack(side=tkinter.LEFT)
nameentry = tkinter.Entry(nameframe)
nameentry.pack(side=tkinter.LEFT)

noteframe = tkinter.Frame(master)
noteframe.pack()
notelabel = tkinter.Label(noteframe, text="Zadajte znamku studenta: ")
notelabel.pack(side=tkinter.LEFT)
noteentry = tkinter.Entry(noteframe)
noteentry.pack(side=tkinter.LEFT)

buttonframe = tkinter.Frame(master)
buttonframe.pack()
button_add = tkinter.Button(buttonframe, text="Pridaj studenta")
button_show = tkinter.Button(buttonframe, text="Zobraz abecedne")
button_del = tkinter.Button(buttonframe, text="Zmaz zoznam")
button_add.pack(side=tkinter.LEFT)
button_show.pack(side=tkinter.LEFT)
button_del.pack(side=tkinter.LEFT)

tkinter.Label(master, text="Meno (znamka)")

def jeZnamka(x):
    try: 
        int(x)
    except ValueError:
        return False
    return int(x) >0 and int(x) < 6

tabulka = []
def pridaj():
    global tabulka
    meno = nameentry.get()
    znamka = noteentry.get()
    if(jeZnamka(znamka) == False):
        return None
    znamka = int(znamka)
    tabulka.append([meno,znamka])
button_add["command"]=pridaj

labels= []
def zobraz():
    global labels, tabulka
    for i in labels:
        i.destroy()
    labels = []
    tabulka.sort()
    for i in tabulka:
        labels.append(tkinter.Label(master, text=i[0] + " (" + str(i[1]) + ")"))
    for i in labels:
        i.pack()
button_show["command"] = zobraz

def zmaz():
    global tabulka
    tabulka = []
    zobraz()
button_del["command"] = zmaz
master.mainloop()