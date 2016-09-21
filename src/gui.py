#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import classes as cls
import utils

from global_vars import *


# Main unresizable window ######################################################
window = tk.Tk()
window['bg'] = 'white'
window.resizable(width=False, height=False)


# Images #######################################################################
FLAG = tk.PhotoImage(file="red_flag.gif")
MINE = tk.PhotoImage(file="mine.gif")


# Game menu (will probably require a package) ##################################
menubar = tk.Menu(window)
menu1 = tk.Menu(menubar, tearoff=0)
menu2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menu1)
menubar.add_cascade(label="Aide", menu=menu2)
window.config(menu=menubar)


# Top frame ####################################################################
top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x")



# Game frame ###################################################################
game_frame = tk.Frame(window, borderwidth=2, relief=tk.SUNKEN)

BOARD = [[cls.Square(i, j) for j in range(WIDTH)] for i in range(HEIGHT)]

def create_square(i, j):
    f = tk.Frame(game_frame, height=25, width=25)
    s = tk.Button(f, borderwidth=1, state="normal",disabledforeground="#000000")
    s.pack(fill=tk.BOTH, expand=True)
    
    # buttons bindings
    def __handler(event, x=i, y=j):
        if event.num == 1:
            utils.left_handler(BOARD, GRID, x, y, MINE)
        elif event.num == 3:
            utils.right_handler(BOARD, GRID, x, y, FLAG)
        else:
            raise Exception('Invalid event code.')
    s.bind("<Button-1>", __handler)
    s.bind("<Button-3>", __handler)

    f.pack_propagate(False) # still useful ?
    f.grid_propagate(False) # still useful ?
    f.grid(row=i, column=j)
    return s

GRID = [[create_square(i, j) for j in range(WIDTH)] for i in range(HEIGHT)]
utils.add_bombs(BOARD)
game_frame.pack(padx=10, pady=10, side=tk.BOTTOM)

utils.print_board(BOARD)

window.mainloop()
