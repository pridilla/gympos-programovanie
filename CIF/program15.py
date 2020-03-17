import tkinter, random

master = tkinter.Tk()

t = 10
hadane = random.randint(1,20)
prebieha = True

sek = tkinter.Label(master, text="Pocet sekund: ", anchor=tkinter.NW)
e = tkinter.Entry(master, text="-1")
cisla = tkinter.Label(master, text= "Nepsravne hadane: ")
button = tkinter.Button(master, text="Spustit")
vysl = tkinter.Label(master, text="Spustite a hadajte od 1 do 20 ")

sek.pack()
e.pack()
button.pack()
cisla.pack()
vysl.pack()

def hadaj():
    global vysl, e, cisla, hadane, prebieha
    s= e.get()
    if(hadane == int(s)):
        vysl["text"] = "Gratulujeme, vyhrali ste"
        prebieha = False
    else:
        cisla["text"] += s + " "

def spustit():
    global sek, e, cisla, vysl, t, master, prebieha, button, hadane
    hadane = random.randint(1,20)
    prebieha = True
    sek.destroy()
    button.destroy()
    cisla.destroy()
    e.destroy()
    vysl.destroy()
    t = 10
    sek = tkinter.Label(master, text="Pocet sekund: ", anchor=tkinter.NW)
    e = tkinter.Entry(master, text="-1")
    button = tkinter.Button(master, text="Spustit")
    cisla = tkinter.Label(master, text= "Nepsravne hadane: ")
    vysl = tkinter.Label(master, text="Spustite a hadajte od 1 do 20 ")
    sek.pack()
    e.pack()
    button.pack()
    cisla.pack()
    vysl.pack()
    button["command"] = hadaj
    button["text"] = "Hadaj"
    time_update()

def time_update():
    global t, sek, vysl, prebieha, button
    if(t > 0 and prebieha):
        sek["text"] = "Pocet sekund: " + str(t)
        t -=1
        master.after(1000, time_update)
    elif(prebieha):
        prebieha = False
        vysl["text"] = "Cas vyprsal"
        button["text"] = "Spusti"
        button["command"] = spustit         

button["command"] = spustit         

master.mainloop()