import tkinter, math, random
master = tkinter.Tk()
canvas = tkinter.Canvas(width=400, height=400)
canvas.grid(row=0)

def trojuholnik(x,y,a):
    canvas.create_line(x,y,x+a/2,y-int(math.sqrt(3.0/4.0)*a), fill = "red", tag="x")
    canvas.create_line(x+a,y,x+a/2,y-int(math.sqrt(3.0/4.0)*a), fill = "red", tag="x")
    canvas.create_line(x,y,x+a,y, fill = "red", tag="x")

def obdlznik(x,y,a):
    canvas.create_rectangle(x,y,x+a,y+a, fill="white", outline ="blue", tag="x")

def domcek(x,y,a):
    obdlznik(x,y,a)
    trojuholnik(x,y,a)

def vykresli():
    for i in range(10):
        a = random.randint(4,50)
        x = random.randint(a, 400-a)
        y = random.randint(a, 400-a)
        domcek(x,y,a)

def zmaz():
    canvas.delete("x")

btn1 = tkinter.Button(master, text="vykresli", command=vykresli)
btn2 = tkinter.Button(master, text="zmaz", command=zmaz)
btn1.grid(row=1)
btn2.grid(row=2)

canvas.mainloop()