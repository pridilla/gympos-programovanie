import tkinter, random, math
master = tkinter.Tk()

pocetframe = tkinter.Frame(master)
pocetframe.pack()
pocetlabel = tkinter.Label(pocetframe, text="Zadajte pocet kruhov: ")
pocetlabel.pack(side=tkinter.LEFT)
pocetentry = tkinter.Entry(pocetframe)
pocetentry.pack(side=tkinter.LEFT)

button = tkinter.Button(master, text="Zobraz")
button.pack()

canvas = tkinter.Canvas(master, width=250, height=250)
canvas.pack()

def jeCislo(x):
    try: 
        int(x)
    except ValueError:
        return False
    return int(x) >0

def abs(x,y):
    if x > y:
        return x-y
    return y-x

def average(x,y):
    return int((x+y)/2)

def getCircle(point1, point2):
    dx = abs(point1[0],point2[0])
    dy = abs(point1[1],point2[1])
    r = int(math.sqrt(dx**2+dy**2)/2)
    x = average(point1[0], point2[0])
    y = average(point1[1], point2[1])
    return [x,y,r]

def getDistance(point1, point2):
    dx = abs(point1[0],point2[0])
    dy = abs(point1[1],point2[1])
    d = int(math.sqrt(dx**2+dy**2))
    return d

def kruh(x,r, f):
    canvas.create_oval(x-r,x-r,x+r, x+r, outline="",fill=f)

def zobraz():
    global canvas
    canvas.destroy()
    a = random.randint(250, 400)
    k = pocetentry.get()
    if(jeCislo(k)):
        k = int(k)
    else:
        k = 10
    canvas = tkinter.Canvas(width=a, height=a, bd=0, highlightthickness=0, relief='ridge')
    canvas.pack()
    canvas.create_rectangle(1,1,a-1,a-1, fill="",outline="red")
    ar = -2*k*k+4*k+2
    br = -4*a
    cr = a*a
    D = math.sqrt(br*br - 4*ar*cr)
    r = (2*a - math.sqrt(2*a*a*(k-1)**2))/(-2*k*k+4*k+2)
    posun = int(math.sqrt(2)*r)
    bod = r
    for i in range(k):
        kruh(int(bod + i*posun), r, '#%06X' % random.randint(0, 0xFFFFFF))

button["command"] = zobraz
master.mainloop()
