#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import tkinter.font as tkf
import classes as cls
import utils
import time

import global_vars as g


# Main unresizable window ######################################################
window = tk.Tk()
window['bg'] = 'white'
window.resizable(width=False, height=False)


# Images #######################################################################
FLAG = tk.PhotoImage(file="red_flag.gif")
MINE = tk.PhotoImage(file="mine.gif")


# Top frame ####################################################################
top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x")
for i in range(4):
    top_frame.columnconfigure(i, weight=1)

# bombs_counter, left
bombs_counter_str = tk.StringVar()
bombs_counter_str.set(g.BOMBS_LEFT)
bombs_counter = tk.Label(   top_frame, height=1, width=4, bg='white', 
                            textvariable=bombs_counter_str, 
                            font=tkf.Font(weight='bold', size=10))
bombs_counter.grid(row=0, column=0, padx=5, sticky=tk.W)

def new_game():
    return
# new game button, middle
newgame_button = tk.Button(top_frame, bd=1, text="New game", command=new_game)
newgame_button.grid(row=0, column=1, padx=3, sticky=tk.E)

# help button, middle
def disp_help():
    return
help_button = tk.Button(top_frame, bd=1, text="Help", command=disp_help)
help_button.grid(row=0, column=2, padx=3, sticky=tk.W)

# time counter, right
time_counter_str = tk.StringVar()
time_counter = tk.Label(top_frame, height=1, width=4, bg='white',
                        textvariable=time_counter_str,
                        font=tkf.Font(slant='italic', size=10))
time_counter.grid(row=0, column=3, padx=5, sticky=tk.E)

def update_time():
    time_counter_str.set(int((time.time()-init_time)//1))
    time_counter.after(100, update_time)



# Game frame ###################################################################
game_frame = tk.Frame(window, borderwidth=2, relief=tk.SUNKEN)

BOARD = [[cls.Square(i, j)  for j in range(g.WIDTH)] 
                            for i in range(g.HEIGHT)]

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
            bombs_counter_str.set(g.BOMBS_LEFT)
        else:
            raise Exception('Invalid event code.')
    s.bind("<Button-1>", __handler)
    s.bind("<Button-3>", __handler)

    f.pack_propagate(False) # still useful ?
    f.grid_propagate(False) # still useful ?
    f.grid(row=i, column=j)
    return s

GRID = [[create_square(i, j) for j in range(g.WIDTH)] for i in range(g.HEIGHT)]
utils.add_bombs(BOARD)
game_frame.pack(padx=10, pady=10, side=tk.BOTTOM)

utils.print_board(BOARD)

init_time = time.time()
update_time()
window.mainloop()
