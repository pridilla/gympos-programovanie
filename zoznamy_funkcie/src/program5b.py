import tkinter
canvas = tkinter.Canvas(width=1000, height = 500)
canvas.pack()

pocet = int(input("Zadajte počet súťažiacich: "))
vysl = []
for i in range(pocet):
    meno = input("Ako sa volá hráč číslo " + str(i+1) + "? ")
    metre = int(input("Koľko metrov doskočil/a " + meno + "? "))
    cas = int(input("Aký mal/a čas doskoku " + meno + "? "))
    vysl.append([meno, metre, cas])

def vykresli_dlzku(m, d, c, y):
    canvas.create_rectangle(20,y,20 + 5*d, y+10)
    canvas.create_text(20 + 5*d+ 20, y+5, anchor=tkinter.W, text=m + " doskočil " + str(d) + " metrov za " + str(c) + " sekúnd.")

def vykresli():
    for i in range(pocet):
        vykresli_dlzku(vysl[i][0], vysl[i][1], vysl[i][2], 30 + i*40)

vykresli()

canvas.mainloop()