import tkinter as tk
import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "draw foward"
        self.hi_there["command"] = self.updef
        self.hi_there.pack(side="right")

        self.red = tk.Button(self)
        self.red["text"] = "draw backward"
        self.red["command"] = self.downdef
        self.red.pack(side="right")

        self.green = tk.Button(self)
        self.green["text"] = "turn left"
        self.green["command"] = self.leftdef
        self.green.pack(side="right")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "turn right"
        self.yellow["command"] = self.rightdef
        self.yellow.pack(side="right")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "no draw on"
        self.yellow["command"] = self.nodrawondef
        self.yellow.pack(side="left")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "no draw off"
        self.yellow["command"] = self.nodrawoffdef
        self.yellow.pack(side="left")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "color green"
        self.yellow["command"] = self.greendef
        self.yellow.pack(side="left")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "color red"
        self.yellow["command"] = self.reddef
        self.yellow.pack(side="left")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "undo"
        self.yellow["command"] = self.undodef
        self.yellow.pack(side="left")

        self.yellow = tk.Button(self)
        self.yellow["text"] = "clear"
        self.yellow["command"] = self.cleardef
        self.yellow.pack(side="left")

    def updef(self):
        t.forward(10)

    def downdef(self):
        t.backward(10)

    def leftdef(self):
        t.left(10)

    def rightdef(self):
        t.right(10)

    def nodrawondef(self):
        t.pensize(0)

    def nodrawoffdef(self):
        t.pensize(1)

    def greendef(self):
        t.pencolor("green")

    def reddef(self):
        t.pencolor("red")

    def undodef(self):
        t.undo()

    def cleardef(self):
        t.clear()


root = tk.Tk()
app = Application(master=root)
app.mainloop()