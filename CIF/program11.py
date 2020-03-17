import tkinter,random, math
canvas = tkinter.Canvas(height = 200, width=200)
canvas.pack()

def kruh(x,y):
    r=10
    canvas.create_oval(x-r,y-r,x+r,y+r, fill="purple")

for i in range(500):
    x = random.randint(50,150)
    maxy = int(math.sqrt(50**2 - (x-100)**2))
    y = random.randint(100-maxy,100+maxy)
    kruh(x,y)

canvas.mainloop()