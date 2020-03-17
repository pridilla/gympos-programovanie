import tkinter

master = tkinter.Canvas(width=300, height=600)
master.pack()
files = ["karta1.png", "karta2.png", "karta3.png", "karta4.png"]
imgs = []
for i in range(len(files)):
    imgs.append([tkinter.PhotoImage(file=files[i]), 1, 0])
    master.create_image(150, 50 + 80*i, image = imgs[i][0])
    imgs[i][2] = master.create_rectangle(45, 20 + 80*i, 255, 80 + 80*i, outline = "", fill = "", tag = str(i))

def update(x, imgs):
    print("ide")
    print(imgs[x][1])
    if(imgs[x][1] == 1):
        master.itemconfig(imgs[x][2], outline="black")
    else:
        master.itemconfig(imgs[x][2], outline="")
    imgs[x][1] *= -1

for i in range(len(imgs)):
    master.tag_bind(imgs[i][2], "<Button-1>", lambda e, x=i : update(x, imgs))

txt = master.create_text(150, 450, text="vyhodnot", tag="vyh")
def vyhodn(e):
    global imgs
    for i in range(len(imgs)):
        if(imgs[i][1] == 1):
            imgs[i][1]= 0
        else:
            imgs[i][1] = 1
    r = imgs[3][1]*8 + imgs[2][1]*4 + imgs[1][1]*2 + imgs[0][1]*1
    master.delete("x")
    master.create_text(150, 550, text=str(r), tag="x")
master.tag_bind("vyh", '<Button-1>', vyhodn)

master.mainloop()