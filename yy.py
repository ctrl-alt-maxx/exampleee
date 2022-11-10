import tkinter

class Starfighter: # Class
    def __init__(self, master): # Constructor
        self.master = master
        self.frame = tkinter.Frame(self.master)
        self.frame.pack()

        self.button = tkinter.Button(self.frame, text = "QUIT", fg = "red", command = self.frame.quit)
        self.button.pack(side = tkinter.LEFT)

        self.hi_there = tkinter.Button(self.frame, text = "Hello", command = self.say_hi)
        self.hi_there.pack(side = tkinter.LEFT)

    def say_hi(self): # Method
        print("Hi there, everyone!")
    