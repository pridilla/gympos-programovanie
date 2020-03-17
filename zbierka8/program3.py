import tkinter


### Napriek zadaniu je implementovana kontrola roznych typov zatvoriek, aby bol program a algoritmus univerzalnejsi
master = tkinter.Tk()
farby = ["red", "blue", "cyan", "green", "grey", "pink", "purple"]
label = tkinter.Label(master, text="Zadajte text s roznymi zatvorkami")
entry = tkinter.Entry(master)
button = tkinter.Button(master, text="Kontrola")
label_hodnotenie = tkinter.Label(master, text="")
label.pack()
entry.pack()
button.pack()
label_hodnotenie.pack()

def kontrola(x):
    front = ["(", "<", "[", "{"]
    back = [")", ">", "]", "}"]
    naspat = ["", []]
    label_hodnotenie["text"] = "Zatvroky su spravne zadane!"
    for i in x:
        if front.count(i) == 1:
            fronti = front.index(i)
            backx = back[fronti]
            naspat[0] = backx + naspat[0]
        if back.count(i) == 1:
            if(len(naspat) != 0 and naspat[0][0] == i):
                naspat[0] = naspat[0][1:]
            else:
                label_hodnotenie["text"] = "Zatvroky su nespravne zadane!"

button["command"] = lambda : kontrola(entry.get())
master.mainloop()