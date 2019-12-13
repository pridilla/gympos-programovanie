import tkinter
canvas = tkinter.Canvas(height = 400, width = 400)
canvas.pack()

osemsustava = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
farby = ["black", "yellow", "blue", "red", "green", "orange"]
def osmickova(x):
    zvysok = x % 8
    ind = 8
    while(ind*8 < x):
        ind *= 8
    if(x < 8):
        return osemsustava[x]
    return osemsustava[int(x/ind)] + osmickova(zvysok)

vstup = input("Zadajte stvorciferne cislo: ")
svstup = str(vstup)
prvstup = 1.0/int(vstup)
obvstup = ""
cif_sucet = 0
for i in svstup:
    obvstup = i + obvstup
    cif_sucet += int(i)
osemvstup = osmickova(int(vstup))

canvas.create_text(100, 30, text = "cislo " + str(vstup))
for i in range(6):
    canvas.create_text(100 + i * 20, 50, text = obvstup[i], font = "arial " + str((6-i) + 20) + " bold", fill = farby[i])
canvas.create_text(100, 70, text = "cif sucet  " + str(cif_sucet))

canvas.mainloop()




