import tkinter
canvas = tkinter.Canvas(height = 200, width = 400)
canvas.pack()

osemsustava = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
farby = ["black", "grey", "blue", "red", "green", "orange"]

def osmickova(x):
    if (x < 8):
        return str(x) 
    vydelene = int(x/8)
    zvysok = str(x % 8)
    return osmickova(vydelene) + zvysok

vstup = input("Zadajte sestciferne cislo: ")
svstup = str(vstup)
prvstup = 1.0/int(vstup)
obvstup = ""
cif_sucet = 0
for i in svstup:
    obvstup = i + obvstup
    cif_sucet += int(i)
osemvstup = osmickova(int(vstup))

canvas.create_text(200, 30, text = "cislo " + str(vstup))
for i in range(6):
    canvas.create_text(100 + i * 20, 50, text = obvstup[i], font = "arial " + str((6-i*2) + 20) + " bold", fill = farby[i])
canvas.create_text(200, 70, text = "cif sucet: " + str(cif_sucet))
canvas.create_text(200, 90, text = "prevratene: " + str('{:.13f}'.format(round(1/int(vstup), 12))))
canvas.create_text(200, 110, text = "v osmickovej: " + str(osmickova(int(vstup))))


canvas.mainloop()




