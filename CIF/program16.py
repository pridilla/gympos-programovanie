import tkinter

master = tkinter.Tk()
canvas = tkinter.Canvas(master, width=500, height=500)
canvas.pack()

button = tkinter.Button(master, text= "Vypocitaj")
button.pack()

l = tkinter.Label(master, text="Pocet stupani: ")
l.pack()

stupanie = 0
x = -1
y = -1
def oznac(e):
    global x,y,canvas, stupanie
    if(x != -1):
        canvas.create_line(x,y, e.x,e.y)
    if(y > e.y):
        stupanie += 1
    x = e.x
    y = e.y       

def vypocitaj():
    global stupanie, l
    l["text"] = "Pocet stupani: " + str(stupanie)

canvas.bind("<Button-1>", oznac)
button["command"] = vypocitaj
master.mainloop()