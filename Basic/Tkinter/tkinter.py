#!/usr/bin/env python3

from tkinter import *

root = Tk()
app = Window(root)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()