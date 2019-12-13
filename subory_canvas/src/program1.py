import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

suborr = open('../lib/stickman.txt', 'r')
line = suborr.readline()
line.strip()
line = int(line)
zoznam = [line]

while True :
    line = suborr.readline()
    if (line == ''):
        break
    line.strip()
    line = int(line)
    zoznam.append(line)

for i in range(0,len(zoznam),4):
    if (i == 0):
        canvas.create_oval(zoznam[i], zoznam[i+1], zoznam[i+2], zoznam[i+3])
    else:
        canvas.create_line(zoznam[i], zoznam[i+1], zoznam[i+2], zoznam[i+3])

canvas.mainloop()
suborr.close()