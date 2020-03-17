import tkinter, string

master = tkinter.Tk()

stlacitframe = tkinter.Frame(master)
stlacitframe.pack()
stlacitlabel = tkinter.Label(stlacitframe, text="Zadajte text na stlacenie: ")
stlacitlabel.pack(side=tkinter.LEFT)
stlacitentry = tkinter.Entry(stlacitframe)
stlacitentry.pack(side=tkinter.LEFT)
stlacitbutton = tkinter.Button(stlacitframe, text="Stlacit")
stlacitbutton.pack(side=tkinter.LEFT)

stlacitvysledok = tkinter.Label(text="")
stlacitvysledok.pack()

spatframe = tkinter.Frame(master)
spatframe.pack()
spatlabel = tkinter.Label(spatframe, text="Zadajte stlaceny text: ")
spatlabel.pack(side=tkinter.LEFT)
spatentry = tkinter.Entry(spatframe)
spatentry.pack(side=tkinter.LEFT)
spatbutton = tkinter.Button(spatframe, text="Spat")
spatbutton.pack(side=tkinter.LEFT)

povodnevysledok = tkinter.Label(text="")
povodnevysledok.pack()

def stlacit(x):
    res = ""
    toCapitalize = False
    for i in range(len(x)):
        if(x[i] == " "):
            toCapitalize = True
        else:
            y = x[i]
            if(toCapitalize):
                toCapitalize = False
                y = x[i].upper()
            res += y
    stlacitvysledok["text"] = res

def spat(x):
    res = ""
    for i in range(len(x)):
        if(x[i].isupper() and i!=0):
            y = x[i].lower()
            res += " " + y
        else:
            res += x[i]
    povodnevysledok["text"] = res.upper()

stlacitbutton["command"] = lambda : stlacit(stlacitentry.get())
spatbutton["command"] = lambda : spat(spatentry.get())

master.mainloop()