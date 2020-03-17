import tkinter, string, re
master = tkinter.Tk()

tkinter.Label(master, text="Zadajte vetu: ").grid(row=0, columnspan = 2)
vstup = tkinter.Entry(master)
vstup.grid(row=1, column=0)
tkinter.Label(master, text="Rozdelené slová: ").grid(row=2, columnspan = 2)
vysledok = tkinter.Label(master, text="")
vysledok.grid(row=3, columnspan=2)

def rozdel():
    svstup = vstup.get().strip()
    zoznam = re.split('; |, |\*|\n| ', svstup)
    txt = ""
    for i in zoznam:
        txt = txt + "\n" + i
    vysledok.config(text=txt)
    

btn1 = tkinter.Button(master, text="rozdel", command=rozdel)
btn1.grid(row=1, column=1)

tkinter.Label(master, text="Cézarová šifra. Zadajte číslo celé\nčíslo pre zašifrovanie a opačné\nčíslo pre odšifrovanie: ").grid(row=4, columnspan = 2)
vstup_sifra = tkinter.Entry(master)
vstup_sifra.grid(row=5, columnspan=2)
tkinter.Label(master, text="Zadajte text pre zašifrovanie: ").grid(row=6, columnspan = 2)
vstup_text = tkinter.Entry(master)
vstup_text.grid(row=7, columnspan=2)
vysledok2 = tkinter.Label(master, text="")
vysledok2.grid(row=8, columnspan=2)

def sifra():
    text = vstup_text.get().strip()
    s = int(vstup_sifra.get().strip())
    result = ""
    for char in text:
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    vysledok2.config(text=result)

btn2 = tkinter.Button(master, text="zašifruj", command=sifra)
btn2.grid(row=9, columnspan=2)


master.mainloop()