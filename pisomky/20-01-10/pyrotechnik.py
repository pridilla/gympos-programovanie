import tkinter, random
canvas = tkinter.Canvas(height = 200, width = 400)
canvas.pack()
farby = ["green", "red", "grey", "blue", "orange"]

spravna = ""
cas = 90
cas_temp = 0
ok = False
destroyed = False

def spusti():
    global cas, cas_temp, spravna, ok, destroyed
    ok = False
    cas = int(cas*2/3)
    cas_temp = cas
    time_update()
    if(destroyed):
        return 0
    canvas.delete(tkinter.ALL)
    canvas.create_text(200, 20, text= "Pyrotechnik", fill= "blue", font="arial 20 bold")
    canvas.create_text(200, 40, text= "označ správny káblik")
    spravna = random.choice(farby)
    for i in range(len(farby)):
        kablik(70 + 10*i, farby[i])

def kablik(x,farba):
    canvas.create_rectangle(50,x,250,x+10, fill=farba, tag=farba)
    canvas.tag_bind(farba, "<Button-1>", lambda event, f=farba: event_kablik(f))

def event_kablik(farba):
    global cas, cas_temp, spravna, ok
    if(farba == spravna):
        ok = True
    else:
        canvas.delete(farba)


def koniec(up):
    canvas.unbind_all("<Button-1>")
    canvas.create_text(100, 150, text = up, font="arial 20 bold")
    canvas.update()
    canvas.after(2000, spusti)

def time_update():
    global cas_temp, ok, cas, destroyed

    canvas.delete("cas")
    canvas.create_text(350, 100, fill="red", text=int(cas_temp), tag="cas", font="arial 50 bold")
    cas_temp -= 1
    if cas < 2:
        canvas.quit()
        destroyed = True
    elif ok == True:
        koniec("Vyhral si!")
        ok = False
    elif cas_temp < 0:
        koniec("Prehral si, čas vypršal")
    else:
        canvas.after(1000,time_update)

spusti()
canvas.mainloop()