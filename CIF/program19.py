import tkinter, random

master=tkinter.Tk()

a = 400
k = 15

farby = ["black", "blue", "yellow", "red", "green", "pink"]

l1 = tkinter.Label(master, text="Pocet kruhov: ")
l2 = tkinter.Label(master, text="Velkost strany: ")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = tkinter.Entry(master, text="10")
e2 = tkinter.Entry(master, text="400")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

can = tkinter.Canvas(master,width=a, height=a)
can.grid(row=3, column=0, columnspan=2)

def vykresli():
    global k, a, can
    can.delete("can")
    d = a/k
    for i in range(k):
        o = can.create_oval(d*i+5, a - d*i+2,d*i + d+5, a-d*i-d+2 , fill=random.choice(farby), tag="can")


def setdata():
    global a,k, can
    can.config(width=a+4, height=a+4)
    a = int(e2.get())
    k = int(e1.get())
    vykresli()

but = tkinter.Button(master, text= "Vykresli", command=setdata)
but.grid(row=2, column=0, columnspan=2)
master.mainloop()
