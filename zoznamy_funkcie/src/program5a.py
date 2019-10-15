import tkinter

f = open("../lib/trojskok.txt", "r")
canvas = tkinter.Canvas(width=1000, height = 500)
canvas.pack()

vysl = []
while(1 == 1):
    meno = f.readline().strip()
    if(meno == ""):
        break
    metre = int(f.readline().strip())
    cas = int(f.readline().strip())
    vysl.append([meno, metre, cas])
f.close()

def vykresli_dlzku(m, d, c, y):
    canvas.create_rectangle(20,y,20 + 5*d, y+10)
    canvas.create_text(20 + 5*d+ 20, y+5, anchor=tkinter.W, text=m + " doskočil " + str(d) + " metrov za " + str(c) + " sekúnd.")

def vykresli():
    for i in range(len(vysl)):
        vykresli_dlzku(vysl[i][0], vysl[i][1], vysl[i][2], 30 + i*40)

vykresli()

canvas.mainloop()