import tkinter, time
canvas = tkinter.Canvas(height = 400, width = 400)
canvas.pack()
# kruhy sa generuju kliknutim na modre pole
canvas.create_rectangle(0,0,400,400, fill="blue")

def kruh(x,y,r):
    canvas.create_oval(x-r,y-r,x+r,y+r, outline = "white", fill = "", tag = "kruh")

def kruhy(event):
    for i in range(5):
        kruh(event.x,event.y, (i+1)*30)
        time.sleep(0.1)
        canvas.update()

def zmaz():
    canvas.delete("kruh")

button = tkinter.Button(text = "Zmazat", command = zmaz)
button.configure(width = 60, activebackground = "#33B5E5", relief = tkinter.FLAT)
button1_window = canvas.create_window(200, 400,anchor=tkinter.S, window=button, width= 60)

canvas.bind("<Button-1>", kruhy)

canvas.mainloop()