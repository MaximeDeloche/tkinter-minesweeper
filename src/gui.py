#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes
from tkinter import *

# game init (need parameters)
x_size = 10
y_size = 15
grid = classes.Grid(x_size, y_size)
grid.add_bombs(20)

# main unresizable window
window = Tk()
window['bg'] = 'white'
window.resizable(width=False, height=False)

# menu
menubar = Menu(window)
menu1 = Menu(menubar, tearoff=0)
menu2 = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menubar.add_cascade(label="Aide", menu=menu2)
window.config(menu=menubar)

# frame in which the buttons will be displayed
frame = Frame(window, borderwidth=2, relief=SUNKEN)
frame.pack(padx=10, pady=10)

def __left_handler(event, row, column):
    # (is_bomb, number) = grid.squares[row][column].left_click()
    print("Ta gueule")

def right_handler(event):
    if event.widget["text"] == "":
        event.widget["text"] = "?"
    else:
        event.widget["text"] = ""


for i in range(x_size):
    for j in range(y_size):
        b = Button(frame, command=None, borderwidth=1)
        b.grid(row=i, column=j)
        def left_handler(event, row=i, column=j):
            return __left_handler(event, row, column)
        b.bind("<Button-1>", left_handler)
        b.bind("<Button-3>", right_handler)

window.mainloop()
