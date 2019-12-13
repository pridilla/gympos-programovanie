from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Rovnice")
txt = Label(root, text="Jednoduché prostredie pre výpočet rovníc o 3 neznámych. \nZadajte príslušné koeficienty do políčok. \nPri správnom vyplnení je možné využiť program aj pre 2 neznáme \n- stačí ak necháte posledný riadok a posledný stĺpec nevyplnené.")
#txt.pack()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

koef = ["x + ","y + ","z = ", ""]
entries = []
labely = []
texty = []

def matica3 (v):
    return v[0][0]*v[1][1]*v[2][2] + v[0][1]*v[1][2]*v[2][0] + v[0][2]*v[1][0]*v[2][1] - v[0][2]*v[1][1]*v[2][0] - v[0][0]*v[1][2]*v[2][1] - v[0][1]*v[1][0]*v[2][2]
def matica(v, k):
    vv = []
    for i in range(3):
        vv.append([])
        for j in range(4):
            if(j == k):
                continue
            vv[i].append(v[i][j])
    return vv
def calc(*args):
    vektory = []
    for i in range(3):
        vektory.append([])
        for j in range(4):
            vektory[i].append(int(texty[i][j].get()))
    
    d = matica3(matica(vektory,3))
    dx = matica3(matica(vektory,0))
    dy = matica3(matica(vektory,1))
    dz = matica3(matica(vektory,2))

    ttk.Label(mainframe, text = "x = " + str(dx/d)).grid(column=1, row = 5)
    ttk.Label(mainframe, text = "y = " + str(-dy/d)).grid(column=1, row = 6)
    ttk.Label(mainframe, text = "z = " + str(dz/d)).grid(column=1, row = 7)

    return 0

for i in range(3):
    texty.append([])
    labely.append([])
    entries.append([])
    for j in range(4):
        texty[i].append(IntVar())
        entries[i].append(ttk.Entry(mainframe, width=5, textvariable = texty[i][j]))
        entries[i][j].grid(column = j*2, row = i+1)
        labely[i].append(ttk.Label(mainframe, text=koef[j]))
        labely[i][j].grid(column = j*2 + 1, row = i+1)
    entries[i].append(ttk.Entry(mainframe, width=5))

txt = ttk.Label(mainframe, text="Jednoduché prostredie pre výpočet rovníc o 3 neznámych. \nZadajte príslušné koeficienty do políčok a stlačte tlačidlo. \nPri správnom vyplnení je možné využiť program aj pre 2 neznáme \n- stačí ak necháte posledný riadok a predposledný stĺpec nevyplnené.")
txt.grid(column=0,row=0, columnspan=13)
        
ttk.Button(mainframe, text="Vypočítaj", command=calc).grid(column=0, row=4, sticky=E)
root.bind('<Return>', calc)

root.mainloop()