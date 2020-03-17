import tkinter as tk, time, random
master = tk.Tk()
tk.Label(master, text="Velkost strany: ", anchor=tk.E).grid(row=0)
tk.Label(master, text="Pocet riadkov: ", anchor =tk.E).grid(row=1)

farby = ["black", "yellow", "blue", "cyan", "green", "red", "orange", "white", "grey", "pink"]

canvas = tk.Canvas(width=400, height=400)
canvas.grid(row=4, columnspan=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def stvorec(x,y,a):
    canvas.create_rectangle(x-a, y, x, y+a, fill= random.choice(farby), outline="black", tag="stvorec")

def rad(x,y,a,k):
    for i in range(k):
        stvorec(x+i*a,y,a)

def pyramida(xstred,y,a,k):
    xpociatok = xstred - a*k/2
    rad(xpociatok,y,a,k)
    if(k > 1):
        pyramida(xstred, y-a, a, k-1)

def spusti_pyramidu():
    pyramida(200,380,int(e1.get()), int(e2.get()))

def zmaz():
    canvas.delete("stvorec")

tk.Button(master, text="Nakresli", command = spusti_pyramidu).grid(row=2, columnspan=2)
tk.Button(master, text="Zmaz", command = zmaz).grid(row=3, columnspan=2)

master.mainloop()