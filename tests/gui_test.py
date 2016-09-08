#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../src")

from tkinter import *

window = Tk()

def fct(event):
    event.widget["image"] = ""

flag = PhotoImage(file="red_flag.gif")

for i in range(3):
    for j in range(3):
        f = Frame(window, height=200, width=100)
        f.pack_propagate(False)
        f.grid_propagate(False)
        f.grid(row=i, column=j)
        b = Button(f, image=flag)
        b.pack(fill=BOTH, expand=True)
        b.bind("<Button-3>", fct)


window.mainloop()
