#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes as cls
import utils
import tkinter as tk

# game init (need parameters)
x_size = 20
y_size = 30
bombs = 20


# main unresizable window
window = tk.Tk()
window['bg'] = 'white'
window.resizable(width=False, height=False)

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

# images
flag = tk.PhotoImage(file="red_flag.gif")
mine = tk.PhotoImage(file="mine.gif")

# click handlings => package ?
def __left_handler(event, row, column):
    print("left")
    # print("(", row, ", ", column, ")")
    # if not grid.squares[row][column].revealed:
    #     if event.widget["image"] == "":
    #         (is_bomb, number) = grid.squares[row][column].left_click()
    #         if is_bomb:
    #             event.widget["state"] = "normal"
    #             event.widget["image"] = mine
    #             # TODO : end game properly
    #         else:
    #             event.widget["text"] = number
    #             if number == 0: # then we discover neighbours
    #                 print("Zero in (", row, ", ", column, ")")
    #                 for (x, y) in utils.neighbours( row, column,
    #                                                 grid.height, grid.width):
    #                     if not grid.squares[x][y].revealed:
    #                         print(x, ",", y)
    #                         __left_handler(event, x, y)
    #
    #         event.widget["relief"] = SUNKEN
    #

def __right_handler(event, row, column):
    print("right")
    # if not grid.squares[row][column].revealed:
    #     if event.widget["image"] == "":
    #         event.widget["state"] = "normal"
    #         event.widget["image"] = flag
    #     else:
    #         event.widget["state"] = "disabled"
    #         event.widget["image"] = ""



print(game_grid)

window.mainloop()
