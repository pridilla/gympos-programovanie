import tkinter


### Šípkami pridávate/uberáte rýchlosť do konkrétnej strany
f = "vozik.png"
c = tkinter.Canvas(width = 700, height= 250)
c.pack()
vozik = tkinter.PhotoImage(file=f)
c.create_line(0,150,700,150)
img = c.create_image(350, 127, image=vozik)
y = 350

velocity = 0
def changeVelocity(x):
    global velocity
    velocity +=x

c.focus_set()
c.bind("<Left>", lambda x:changeVelocity(-1))
c.bind("<Right>", lambda x:changeVelocity(1))

def pohyb():
    global y
    x = 700 - y
    if(y<=0):
        c.move(img, x-y, 0)
        y = x
    elif(y>=700):
        c.move(img, x-y, 0)
        y=x
    y += velocity
    c.move(img, velocity, 0)
    c.after(100, pohyb)

pohyb()

c.mainloop()