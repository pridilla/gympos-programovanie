import tkinter as tkinter

rozmery = [600,400]
farby = ["purple", "blue", "green", "yellow", "orange", "red"]



c1 = input("Prajete si zadat vysku? Zadajte ano alebo nie: ").strip()
if(c1 == "ano"):
    rozmery[1] = int(input("Zadajte vysku: "))
    rozmery[0] = rozmery[1]*3/2
elif(c1 == "nie"):
    c2 = input("Prajete si zadat sirku? Zadajte ano alebo nie: ").strip()
    if(c2 == "ano"):
        rozmery[0] = int(input("Zadajte sirku: "))
        rozmery[1] = rozmery[0]*2/3
    else:
        print("\nNastavene predvolene rozmery 600x400")
else:
    print("\nNastavene predvolene rozmery 600x400")

canvas = tkinter.Canvas(height = rozmery[1], width = rozmery[0])
canvas.configure(highlightthickness=0, borderwidth=0)

canvas.pack()

polomer = rozmery[1]/8


def kruhy(x,y,r):
    for i in range(6):
        canvas.create_oval(x + r*i/6, y + r*i/6, x + 2*r - r*i/6, y + 2*r - r*i/6, fill=farby[i], outline = "")

for i in range(4):
    for j in range(6):
        kruhy(j*rozmery[0]/6, i*rozmery[1]/4, polomer)




canvas.mainloop()

