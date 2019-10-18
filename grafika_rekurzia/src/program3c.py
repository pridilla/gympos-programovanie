import tkinter, math
r = 500
canvas = tkinter.Canvas(width = r, height = r)
canvas.pack()

KORYTNACKA = [r/2,r/2,0]

def uhol(x):
    return x*2*math.pi/360

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

    canvas.create_line(a1,b1,a2,b2)
    nastavPoziciu(a2,b2)

def krok(x):
    if(x > r):
        return 0
    chod(x)
    posunUhol(uhol(30))
    chod(x)
    posunUhol(uhol(-90))
    krok(x+1)

krok(1)

canvas.mainloop()
