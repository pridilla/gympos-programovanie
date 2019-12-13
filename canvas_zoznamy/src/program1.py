import tkinter
import time

master = tkinter.Tk()
canvas = tkinter.Canvas(master, width = 700, height = 700)
canvas.pack()

subor = open('../lib/kresli3.txt', 'r')
lines = []
line = subor.readline()

def mmove(event):
    x = event.x
    y = event.y
    canvas.create_oval(x,y,x,y,fill="grey", tags="user")
    print(event.x, event.y)

def reset():
    canvas.delete("user")


def draw():
    for i in range(len(lines)-1):
        canvas.create_line(lines[i][1], lines[i][2], lines[i+1][1], lines[i+1][2], tags = "user")
        time.sleep(1)
        canvas.update()
    

canvas.bind('<B1-Motion>', mmove)

def bod(udaj):
    canvas.create_oval(int(udaj[1])-1, int(udaj[2])-1, int(udaj[1])+1, int(udaj[2])+1, fill = "black")
    canvas.create_text(int(udaj[1])+9, int(udaj[2])+9, text = udaj[0])

while line != "" :
    line = line.strip()
    lines.append(line.split(' '))
    #print(lines[-1])
    bod(lines[-1])
    line = subor.readline()

subor.close()

button = tkinter.Button(master, text = "Reset", command = reset)
button.place(x=10, y=10)

button2 = tkinter.Button(master, text = "Draw", command = draw)
button2.place(x=10, y=40)

canvas.mainloop()