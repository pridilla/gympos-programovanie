import tkinter

master = tkinter.Tk()

farby = ["red", "white", "yellow", "black", "blue", "green"]
hold = False

farba = "black"

def zmen_farbu(x):
    global farba
    farba = x

def zmaz(e):
    canvas.delete("paint")

def handler(event,x):
    global hold, farba,w
    r = int(w.get())/2

    if(x == "press"):
        hold = True

    elif (x == "release"):
        hold = False
    elif(x == "motion" and hold):
        canvas.create_oval(event.x-r, event.y-r, event.x+r, event.y+r, fill=farba, outline="", tag="paint")

frame = tkinter.Frame(master)
frame.pack()

for i in farby:
    x = i
    button = tkinter.Button(frame, text=i, command=lambda x=i: zmen_farbu(x))
    button.pack(side=tkinter.LEFT)

w = tkinter.Scale(master, from_=1, to=20, orient=tkinter.HORIZONTAL)
w.pack()

canvas = tkinter.Canvas(master, width=400, height=300)
canvas.pack()
canvas.focus_set()
canvas.bind("<Motion>",lambda x:handler(x,'motion'))
canvas.bind("<Button-1>",lambda x:handler(x,'press'))
canvas.bind("<ButtonRelease-1>",lambda x:handler(x,'release'))
canvas.bind("q", zmaz)

master.mainloop()