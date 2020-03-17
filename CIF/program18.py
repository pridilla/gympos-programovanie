import tkinter, random
canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()



def hodnotenie(x,y):
    global canvas
    hodnota = random.randint(0,10)
    canvas.create_rectangle(x,y,x+60,y+40, fill="darkgreen")
    canvas.create_text(x+30, y+20, text=str(hodnota), font="times 18 bold", fill="white")
    return hodnota

def vysl_skore():
    hod = []
    for i in range(5):
        hod.append(hodnotenie(i*80+40, 200))
    hod.sort()
    hod = hod[1:4]
    suma = sum(hod)
    canvas.create_text(250, 350, text="Hodnotenie: " + str(suma), font="times 30 bold", fill="black")

vysl_skore()
canvas.mainloop()