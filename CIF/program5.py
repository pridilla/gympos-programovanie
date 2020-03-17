import tkinter

i = int(input("Zadajte počet polí v jednom stĺpci: "))
a = int(input("Zadajte rozmer šachovnice: "))

canvas = tkinter.Canvas(height = a, width = a)
canvas.configure(highlightthickness=0, borderwidth=0)
canvas.pack()

def stvorec(x,y, farba):
    canvas.create_rectangle(x,y,x + a/i, y + a/i, outline = "", fill = farba)

for j in range(i):
    for k in range(i):
        farba = "black"
        if((j+k) % 2 == 0):
            farba = "white"
        stvorec(j*a/i, k*a/i, farba)

canvas.mainloop()