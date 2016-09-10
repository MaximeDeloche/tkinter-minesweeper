#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes
from tkinter import *

# game init (need parameters)
x_size = 20
y_size = 30
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
main_frame = Frame(window, borderwidth=2, relief=SUNKEN)
main_frame.pack(padx=10, pady=10)


# click handlings => package ?
def __left_handler(event, row, column):
    if not grid.squares[row][column].revealed:
        if event.widget["image"] == "":
            (is_bomb, number) = grid.squares[row][column].left_click()
            if is_bomb:
                print("PERDU PUTAIN")
            else:
                event.widget["text"] = number
            event.widget["relief"] = SUNKEN

def __right_handler(event, row, column):
    if not grid.squares[row][column].revealed:
        if event.widget["image"] == "":
            event.widget["state"] = "normal"
            event.widget["image"] = flag
        else:
            event.widget["state"] = "disabled"
            event.widget["image"] = ""


# grid generation
flag = PhotoImage(file="red_flag.gif")

for i in range(x_size):
    for j in range(y_size):
        # need to put buttons in frames to have a fixed size
        f = Frame(main_frame, height=30, width=30)
        f.pack_propagate(False)
        f.grid_propagate(False)
        f.grid(row=i, column=j)

        b = Button( f, borderwidth=1,
                    state="disabled",
                    disabledforeground="#000000")
        b.pack(fill=BOTH, expand=True)

        # bind mouse clicks with actions
        def left_handler(event, row=i, column=j):
            return __left_handler(event, row, column)
        def right_handler(event, row=i, column=j):
            return __right_handler(event, row, column)
        b.bind("<Button-1>", left_handler)
        b.bind("<Button-3>", right_handler)

window.mainloop()
