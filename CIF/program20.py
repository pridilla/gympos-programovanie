import tkinter, math, random

farby = ["black", "blue", "yellow", "red", "green", "pink"]

a=500
canvas = tkinter.Canvas(width=a, height=a)
canvas.pack()

coords = [0,0]

def length(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

hold = False
letter = "A"

def handler(event,x):
    global coords, hold, letter
    ecoo = [event.x,event.y]

    if(x == "press"):
        hold = True
        letter = "A"

    elif (x == "release"):
        hold = False
    elif(x == "motion" and length(ecoo, coords)>35 and hold):
        coords = ecoo
        canvas.create_text(event.x, event.y, text=letter, fill = random.choice(farby), font= "times 30 bold")
        if(letter == "Z"):
            letter = "A"
        else:
            letter = chr(ord(letter) + 1)

canvas.bind("<Motion>",lambda x:handler(x,'motion'))
canvas.bind("<Button-1>",lambda x:handler(x,'press'))
canvas.bind("<ButtonRelease-1>",lambda x:handler(x,'release'))

canvas.mainloop()



