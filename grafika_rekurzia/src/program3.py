import tkinter, math
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

KORYTNACKA = [100,100, 0]

def uhol(x):
    return 2*math.pi/360

def nastavPoziciu(x,y):
    KORYTNACKA[0] = x
    KORYTNACKA[1] = y

def posunUhol(x):
    KORYTNACKA[2] += x

def chod(x):
    a1 = KORYTNACKA[0]
    b1 = KORYTNACKA[1]

    a2 = a1 + x*math.cos(KORYTNACKA[2])
    b2 = b1 + x*math.sin(KORYTNACKA[2])

canvas.mainloop()