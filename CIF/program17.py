import tkinter

master = tkinter.Tk()

data = []

l1 = tkinter.Label(master, text="Zadajte meno: ")
l1.pack()
e1 = tkinter.Entry(master)
e1.pack()

l2 = tkinter.Label(master, text="Zadajte datum narodenia v tvare RRMMDD: ")
l2.pack()
e2 = tkinter.Entry(master)
e2.pack()

def pridat():
    global data
    data.append([e1.get(), e2.get()])
    print(data)

but1 = tkinter.Button(master, text="Pridat")
but2 = tkinter.Button(master, text="Vypis abecedne")
but3 = tkinter.Button(master, text="Vypis pod 10")
but4 = tkinter.Button(master, text="Vypis mesiac")
but1.pack()
but2.pack()
but3.pack()
but4.pack()
l3 = tkinter.Label(master, text="Zadajte mesiac v tvare MM: ")
l3.pack()
e3 = tkinter.Entry(master)
e3.pack()

l4 = tkinter.Label(master)
l4.pack()

def vypis():
    global data
    text = ""
    data.sort()
    for i in data:
        text += i[0] + " " + i[1] + "\n"
    l4["text"] = text

def vypis_mesiac():
    global data, e3
    text = ""
    data.sort()
    for i in data:
        mesiac = i[1][2:4]
        print(mesiac)
        if mesiac != e3.get():
            continue
        text += i[0] + " " + i[1] + "\n"
    l4["text"] = text

def vypis_10():
    global data, e3
    text = ""
    data.sort()
    for i in data:
        rok = int(i[1][:2])
        if rok>20:
            rok +=1900
        else:
            rok +=2000
        if 2020 - rok >=10:
            continue
        text += i[0] + " " + i[1] + "\n"
    l4["text"] = text

but1["command"] = pridat
but2["command"] = vypis
but3["command"] = vypis_10
but4["command"] = vypis_mesiac

master.mainloop()

