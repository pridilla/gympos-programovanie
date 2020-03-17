import tkinter, random
master = tkinter.Tk()
canvas = tkinter.Canvas(width=300, height=300)
canvas.grid(row=0)

def kruh(x,y,farba):
    canvas.create_oval(x-20,y-20,x+20,y+20, fill=farba, outline="black", tag="x")

def vykresli():
    for i in range(50):
        x = random.randint(0,300)
        y = random.randint(0,300)
        farba = "grey"
        if(x < 100):
            if(y < 100):
                farba = "blue"
            elif(y > 200):
                farba = "green"
        elif(x > 200):
            if(y < 100):
                farba = "red"
            elif(y > 200):
                farba = "yellow"
        kruh(x,y,farba)

def zmaz():
    canvas.delete("x")

btn1 = tkinter.Button(master, text="vykresli", command=vykresli)
btn2 = tkinter.Button(master, text="zmaz", command=zmaz)
btn1.grid(row=1)
btn2.grid(row=2)

canvas.mainloop()