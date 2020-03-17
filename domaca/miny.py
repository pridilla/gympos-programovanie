
import tkinter as tk, time, os, random, time

#Okno, v ktorom môže hráč spustiť hru
class StartFrame:
    def __init__(self, master):
        self.OBTIAZNOST = [
            ("Bažant", 0, [10,6,6]),
            ("Poručík", 1, [12,8,16]),
            ("Likvidátor", 2, [15,13,47])
        ]
        self.master = master
        self.master.title("Spustiť Míny")
        self.frame = tk.Frame(self.master)
        self.l = tk.Label(self.master, text="Zvoľte si obtiažnosť hry:")
        self.l.pack(pady=5)
        self.v = tk.IntVar()
        self.v.set(1)
        for text, lvl, data in self.OBTIAZNOST:
            self.radio = tk.Radiobutton(self.master, text=text, variable=self.v, value=lvl)
            self.radio.pack(padx=20, pady=1, anchor=tk.W)
        self.buttonStart = tk.Button(self.frame, text = 'Spustiť hru', width = 25, command = lambda: self.start_game(self.OBTIAZNOST[self.v.get()][2]))
        self.buttonStart.pack()
        self.buttonInstructions = tk.Button(self.frame, text = "Nápoveda", width=25, command=self.napoveda)
        self.buttonInstructions.pack()
        self.frame.pack(padx=20, pady=20)

    def start_game(self, data):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = StartGame(self.master, data)

    def napoveda(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = StartInstructions(self.newWindow)

#Okno, v ktorom sa zobrazí nápoveda
class StartInstructions:
    def __init__(self, master):
        self.script_path = os.path.abspath(__file__)
        self.script_dir = os.path.split(self.script_path)[0]
        self.rel_path = "lib/readme.txt"
        self.abs_file_path = os.path.join(self.script_dir, self.rel_path)
        self.master = master
        self.master.title("Nápoveda")
        self.instf = open(self.abs_file_path, "r")
        self.insts = self.instf.readline().strip()
        self.instf.close()
        self.frame = tk.Frame(self.master)
        self.l = tk.Label(self.master, text=self.insts, wraplength=400)
        self.quitButton = tk.Button(self.master, text="Koniec", command = self.quitCommand)
        self.l.pack(pady=5, padx=10)
        self.quitButton.pack()
        self.frame.pack(padx=20, pady=20)

    def quitCommand(self):
        self.master.destroy()

class StartGame:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.master.title("Míny")
        self.frame = tk.Frame(master)
        self.resetBut = tk.Button(self.frame, text="Reset", command=self.reset)        
        self.frame.grid(row=0, column=0, columnspan=data[2], padx=3, pady=10)
        self.resetBut.pack()
        self.upl = tk.Label(self.frame, text="")
        self.upl.pack()
        self.app = GamePad(self.master, data[0], data[1], data[2], self.upl)
        self.master.bind("<Escape>", self.quitCommand)

    def reset(self):
        self.app.stop()
        self.__init__(self.master, self.data)

    def quitCommand(self, event):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = StartFrame(self.master)

class GamePad:
    def locclean(self, pointX, pointY):
        if(self.tiles[pointX][pointY].marked):
            return 0
        self.hidden -= 1
        self.tiles[pointX][pointY].found = True
        self.res = self.tiles[pointX][pointY].clean()
        if(self.res == "boom"):
            self.master.unbind("<Return>")
            for i in self.tiles:
                for j in i:
                    if(j.marked):
                        j.mark(self.joker)
                    j.clean()
        if(self.res[0]=="0"):
            self.temphid = self.hidden
            if (pointX < self.X-1 and self.tiles[pointX+1][pointY].found == False):
                self.locclean(pointX+1,pointY)
                if (pointY < self.Y-1 and self.tiles[pointX+1][pointY+1].found == False):
                    self.locclean(pointX+1,pointY+1)
                if (pointY > 0 and self.tiles[pointX+1][pointY-1].found == False):
                    self.locclean(pointX+1,pointY-1)
            if (pointY < self.Y-1 and self.tiles[pointX][pointY+1].found == False):
                self.locclean(pointX,pointY+1)
            if (pointX > 0 and self.tiles[pointX-1][pointY].found == False):
                self.locclean(pointX-1,pointY)
                if (pointY < self.Y-1 and self.tiles[pointX-1][pointY+1].found == False):
                    self.locclean(pointX-1,pointY+1)
                if (pointY > 0 and self.tiles[pointX-1][pointY-1].found == False):
                    self.locclean(pointX-1,pointY-1)
            if (pointY > 0 and self.tiles[pointX][pointY-1].found == False):
                self.locclean(pointX,pointY-1)

        if(self.hidden == self.K):
            self.timev = time.time() - self.time1
            self.master.destroy()
            self.master = tk.Tk()
            self.app = Victory(self.master, self.timev)

        if(self.temphid == self.hidden):
            return 0

    def __init__(self, master, X, Y, K, label):
        self.time1 = time.time()
        self.X=X
        self.Y=Y
        self.K=K
        self.joker = K
        self.label = label
        self.key_focus = [0,0]
        self.master = master
        self.tiles = []
        self.hidden = X*Y
        self.temphid = 0
        for i in range(X):
            self.tiles.append([])
            for j in range(Y):
                self.tiles[i].append(Tile(self.master))
                self.tiles[i][j].grid(i+1,j)
        self.tiles[0][0].focus()
        for i in range(self.K):
            self.x = random.randint(0,self.X-1)
            self.y = random.randint(0,self.Y-1)
            self.temp = self.tiles[self.x][self.y].mine
            self.tiles[self.x][self.y].mine = True
            while self.temp == True:
                self.x = random.randint(0,self.X-1)
                self.y = random.randint(0,self.Y-1)
                self.temp = self.tiles[self.x][self.y].mine
                self.tiles[self.x][self.y].mine = True
        self.keys = ["<Right>", '<Left>', "<Up>", "<Down>"]
        master.focus_set()
        for i in self.keys:
            master.bind(i, lambda event, a=i: self.change_focus(a))
        master.bind("z", lambda event, x=self.key_focus[0], y=self.key_focus[1]: self.locmark(self.key_focus[0],self.key_focus[1]))
        master.bind('<Return>', lambda event, x=self.key_focus[0], y=self.key_focus[1]: self.locclean(self.key_focus[0],self.key_focus[1]))

        for i in range(self.X):
            for j in range(self.Y):
                self.tile = self.tiles[i][j]
                for k in range(i-1, i+2):
                    if(k < self.X and k > -1):
                        for l in range(j-1, j+2):
                            if((l < self.Y and l > -1) and self.tiles[k][l].mine):
                                self.tile.mines_around += 1
    def locmark(self, x, y):
        if(self.tiles[x][y].found == False):
            self.joker = self.tiles[x][y].mark(self.joker)
            self.label["text"] = "Míny: " + str(self.joker)

    def stop(self):
        self.master.grid
        self.list = self.master.grid_slaves()
        for l in self.list:
            l.destroy()

    def change_focus(self, dir):
        self.tiles[self.key_focus[0]][self.key_focus[1]].focus()
        if(dir == "<Down>" and self.key_focus[0]!=self.X-1):
            self.key_focus[0] += 1
        elif(dir == "<Up>" and self.key_focus[0]!=0):
            self.key_focus[0] -= 1
        elif(dir == "<Right>" and self.key_focus[1]!=self.Y-1):
            self.key_focus[1] += 1
        elif(dir == "<Left>" and self.key_focus[1]!=0):
            self.key_focus[1] -= 1
        self.tiles[self.key_focus[0]][self.key_focus[1]].focus()

class Tile:
    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        self.points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
        return self.canvas.create_polygon(self.points, **kwargs, smooth=True)
    
    def __init__(self, master):
        self.mines_around = 0
        self.mine = False
        self.focused = False
        self.marked = False
        self.found = False
        self.master = master
        self.canvas = tk.Canvas(master, width=27, height=27, bd=-2, highlightthickness=0, borderwidth=0)
        
    def grid(self, r, c):
        self.canvas.grid(row=r, column=c, padx=0, pady=0)
        self.round_rectangle(4,4,24,24, outline="white", fill="lightblue", radius=5)

    def focus(self):
        if(self.focused == False):
            self.focused = True
            self.round_rectangle(3,3,25,25, outline="purple", fill="", radius=5, tag= "focus")
        elif(self.focused == True):
            self.focused = False
            self.canvas.delete("focus")

    def mark(self, jokers):
        if(self.marked == False and jokers != 0):
            self.marked = True
            self.round_rectangle(4,4,24,24, outline="white", fill="orange", radius=5, tag= "mark")
            self.canvas.create_polygon(11,9,11,19,11,15,17,12, fill="red", outline= "black", tag="mark")
            return (jokers-1)
        elif(self.marked == True):
            self.canvas.delete("mark")
            self.marked = False
            return (jokers+1)
        else:
            return jokers

    def boom(self):
        self.round_rectangle(4,4,24,24, outline="white", fill="red", radius=5)
        self.canvas.create_line(7,7,21,21, width=2, fill="black")
        self.canvas.create_line(7,21,21,7, width=2, fill="black")


    def ok(self):
        self.round_rectangle(4,4,24,24, outline="white", fill="lightgreen", radius=5)
        self.txt = "."
        if(self.mines_around>0):
            self.txt = str(self.mines_around)
        self.canvas.create_text(14, 14, text=self.mines_around, font="arial 9 bold", fill = "white")

    def clean(self):
        if(self.mine):
            self.boom()
            return "boom"
        else:
            self.ok()
            return str(self.mines_around) + "ok"

class Victory:
    def __init__(self, master, time):
        self.script_path = os.path.abspath(__file__)
        self.script_dir = os.path.split(self.script_path)[0]
        self.rel_path = "lib/trophy.gif"
        self.abs_file_path = os.path.join(self.script_dir, self.rel_path)
        self.master = master
        self.master.title("Víťazstvo")
        self.img = tk.PhotoImage(file = (self.abs_file_path))
        self.img = self.img.subsample(4)
        self.lab = tk.Label(self.master, image = self.img)
        self.lab.pack()
        self.l = tk.Label(self.master, text="Gratulujeme. Zneškodnili ste všety míny. Váš čas je " + str(int(time)) + " sekúnd.", wraplength=400)
        self.quitButton = tk.Button(self.master, text="Hlavné menu", command = self.quitCommand)
        self.l.pack(pady=5, padx=10)
        self.quitButton.pack()

    def quitCommand(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.app = StartFrame(self.master)

root = tk.Tk()
s = StartFrame(root)
root.mainloop()