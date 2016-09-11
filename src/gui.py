#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

# game init (need parameters)
x_size = 20
y_size = 30
bombs = 20

# main unresizable window
# I need to create this before importing classes and utils,
# because they need a root window to be created before
window = tk.Tk()
window['bg'] = 'white'
window.resizable(width=False, height=False)

import classes as cls
import utils


# menu
menubar = tk.Menu(window)
menu1 = tk.Menu(menubar, tearoff=0)
menu2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menubar.add_cascade(label="Aide", menu=menu2)
window.config(menu=menubar)

# frame in which the numbers of bombs and messages will appear
top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x")

# frame in which the buttons will be displayed
game_grid = cls.Grid(window, borderwidth=2, relief=tk.SUNKEN)
game_grid.fill(x_size, y_size)
game_grid.add_bombs(bombs)
game_grid.pack(padx=10, pady=10, side=tk.BOTTOM)


print(game_grid)

window.mainloop()
