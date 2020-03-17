import tkinter

najmenej = [0, 0, 1000, "", "d"]
najviac = [0, 0, 0, "", "d"]

stupne = ["podváha", "normálna hmotnosť", "nadváha", "obezita", "ťažká obezita", "veľmi ťažká obezita"]
bmi_stupne = [18.5, 25.0, 30.0, 35.0, 40.0, 10000.0]

data = []

master = tkinter.Tk()


label_hmotnost = tkinter.Label(master, text = "Hmotnosť v kg: ")
label_hmotnost.grid(row=0, column=0)
entry_hmotnost = tkinter.Entry(master)
entry_hmotnost.grid(row=0,column=1)

label_vyska = tkinter.Label(master, text = "Výška v m: ")
label_vyska.grid(row=1, column=0)
entry_vyska = tkinter.Entry(master)
entry_vyska.grid(row=1,column=1)

label_meno = tkinter.Label(master, text = "Meno: ")
label_meno.grid(row=2, column=0)
entry_meno = tkinter.Entry(master)
entry_meno.grid(row=2,column=1)

button = tkinter.Button(master, text="Odoslať")
button.grid(row=3, column=0, columnspan=2)
label_najviac = tkinter.Label(master, text ="Najväčšie BMI: ")
label_najmenej = tkinter.Label(master, text ="Najmenšie BMI: ")
label_bmi = tkinter.Label(master, text="BMI: ")
label_najviac.grid(row=6, column=0, columnspan=2)
label_najmenej.grid(row=5, column=0, columnspan=2)
label_bmi.grid(row=4, column=0, columnspan=2)

def bmi(m, h):
    return float("{0:.2f}".format(m/h**2))

def vyhodnot(x):
    for i in range(len(stupne)):
        if(x < bmi_stupne[i]):
            return stupne[i]
    return "veľmi ťažká obezita"

def odoslat():
    global najviac, najmenej
    vyska = float(entry_vyska.get())
    hmotnost = float(entry_hmotnost.get())
    meno = entry_meno.get()

    bmi_value = bmi(hmotnost, vyska)
    vyhodnotenie = vyhodnot(bmi_value)
    data.append([vyska, hmotnost, bmi_value, vyhodnotenie, meno])

    if(bmi_value < najmenej[2]):
        najmenej = data[-1]

    if(bmi_value > najviac[2]):
        najviac = data[-1]

    label_najviac.config(text="Najväčšie BMI: "+ str(najviac[4]))
    label_najmenej.config(text="Najmenšie BMI: "+ str(najmenej[4]))
    label_bmi.config(text= "BMI: " + str(bmi_value) + " = " + vyhodnotenie)

button.config(command=odoslat)

master.mainloop()

