import tkinter, string

master = tkinter.Tk()

label = tkinter.Label(master, text= "Zadajte retazec na prevod: ")
label.pack()
entry = tkinter.Entry(master)
entry.pack()
button = tkinter.Button(master, text="Prevod")
button.pack()
canvas = tkinter.Canvas(master, width=500, height=500)
canvas.pack()

x = 10
y = 10

def breakl():
    global x,y
    x = 10
    y += 20

def kruh():
    global x,y,canvas
    if(x > 460):
        breakl()
    canvas.create_oval(x,y,x+10,y+10,outline="", fill="grey", tag="mor")
    x += 12

def obdlznik():
    global x,y,canvas
    if(x > 460):
        breakl()
    canvas.create_rectangle(x,y,x+20,y+10,outline="", fill="grey", tag="mor")
    x += 22

def space():
    global x
    if(x > 460):
        breakl()
    x += 15

def jeCislo(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def vykresli():
    global entry, canvas, x,y
    canvas.delete("mor")
    x = 10
    y = 10
    s = entry.get()
    abeceda = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    cisla = ["-----", ".----", "..---","...--","....-",".....","-....", "--...", "---..","----."]
    poziadavka = ""
    for i in s:
        if(jeCislo(i)):
            poziadavka += cisla[int(i)]
        elif i==" ":
            poziadavka += " "
        else:
            if(i.isupper()):
                poziadavka += abeceda[ord(i)-ord("A")] + "x"
            elif(i.islower()):
                poziadavka += abeceda[ord(i)-ord("a")] + "x"
    for i in poziadavka:
        if(i == "."):
            kruh()
        elif (i=="-"):
            obdlznik()
        elif (i=="x"):
            space()
        elif (i==" "):
            space()
            space()

button["command"] = vykresli
master.mainloop()