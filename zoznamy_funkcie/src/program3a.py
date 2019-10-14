import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, width = 300, height = 300)
canvas.pack()

def najdiDelitele(x):
    delitele = []
    for i in range(x):
        if x % (i+1) == 0:
            delitele.append(i+1)
    return (delitele)

def jePrvocislo(y):
    l = najdiDelitele(y)
    if(len(l) == 2):
        return 1
    else:
        return 0

def najdiPrvocisla(z):
    if(z == 1):
        return []
    m = najdiDelitele(z)
    prvocisla = []
    for j in m:
        if jePrvocislo(j) == 1:
            prvocisla.append(j)
    return prvocisla

def vykresli(icislo, ifarba):
    ic = icislo - 1
    y = 20 + 30*int(ic/10)
    x = 20 + 30*(ic%10)
    canvas.create_text(x,y,text=str(icislo), fill=ifarba)

for i in range(1,101):
    farba = "red"
    if najdiDelitele(i).count(2) > 0 :
        farba = "green"
    vykresli(i, farba)

canvas.mainloop()
