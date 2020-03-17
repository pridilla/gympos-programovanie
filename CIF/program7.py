import tkinter, string
master = tkinter.Tk()

tkinter.Label(master, text="Zadajte retazec: ").grid(row=0, columnspan = 2)
vstup = tkinter.Entry(master)
vstup.grid(row=1, column=0)
tkinter.Label(master, text="Retazec odzadu a počty znakov: ").grid(row=2, columnspan = 2)
vysledok = tkinter.Label(master, text="")
vysledok.grid(row=3, columnspan=2)

def spracuj():
    svstup = vstup.get().strip()
    odzadu = ""
    for i in svstup:
        odzadu = i + odzadu

    pismena = {}
    svstup = svstup.lower()

    for i in svstup:
        if(i==" "):
            i = "medzera"
        if (list(pismena.keys()).count(i) == 0 and i!="."):
            pismena[i] = 1
        else:
            pismena[i] = 1 + pismena[i]

    txt = odzadu + "\n\n"
    for i in pismena.keys():
        txt += i + ": " + str(pismena[i]) + "\n"

    vysledok.config(text = txt)


but = tkinter.Button(master, text = "Spracuj", command=spracuj)
but.grid(row=1, column=1)

master.mainloop()