import tkinter

master = tkinter.Tk()

zlomokframe = tkinter.Frame(master)
zlomokframe.pack()
citatel = tkinter.Entry(zlomokframe)
citatel.pack(side=tkinter.LEFT)
label = tkinter.Label(zlomokframe, text="/")
label.pack(side=tkinter.LEFT)
menovatel = tkinter.Entry(zlomokframe)
menovatel.pack(side=tkinter.LEFT)

button = tkinter.Button(master, text="Zjednodus")
button.pack()

zlomok = tkinter.Label(master)
zlomok.pack()

citatelvyhodnotenie = tkinter.Label(master)
menovatelvyhodnotenie = tkinter.Label(master)
citatelvyhodnotenie.pack()
menovatelvyhodnotenie.pack()

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

def rozkladPrvocisla(q):
    rozklad = {}
    prv = najdiPrvocisla(q)
    for i in prv:
        pocet = 1
        while(q % i**(pocet+1) == 0 and q >= i**(pocet+1)):
            pocet +=1
        rozklad[i] = pocet
    return rozklad

def mensie(x,y):
    if(x>y):
        return y
    return x

def nsd(x,y):
    xr = rozkladPrvocisla(x)
    yr = rozkladPrvocisla(y)

    vysl = []
    res = 1

    for i in list(yr.keys()):
        if list(xr.keys()).count(i) == 1:
            vysl.append([i, mensie(xr[i], yr[i])])

    for i in vysl:
        res *= i[0]**i[1]
    return res

def jePrvocisloSprava(x):
    if(jePrvocislo(x) == 1):
        return "je prvocislo!"
    return "nie je prvocislo!"

def vyhodnot():
    cit = int(citatel.get())
    men = int(menovatel.get())

    NSD = nsd(cit,men)
    cit = int(cit/NSD)
    men = int(men/NSD)

    cele = 0

    zlomok["text"] = str(cit) + "/" + str(men)
    if(cit > men):
        cele = int(cit/men)
        cit = cit % men
        zlomok["text"] = str(cele) + " + (" + str(cit) + "/" + str(men) + ")"
    citatelvyhodnotenie["text"] = "Citatel " + jePrvocisloSprava(cit)
    menovatelvyhodnotenie["text"] = "Menovatel " + jePrvocisloSprava(men)

button["command"] = vyhodnot
master.mainloop()