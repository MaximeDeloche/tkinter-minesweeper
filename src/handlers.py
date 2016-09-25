#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import global_vars as g
import utils

# Event handlers ###############################################################

def left_handler(board, grid, i, j, mine):
    """ Called when left click on the (i, j) cell """
    if grid[i][j]["image"] == "" and not board[i][j].revealed:
        board[i][j].revealed = True
        grid[i][j]["state"] = "disabled"
        grid[i][j]["relief"] = tk.SUNKEN
        if board[i][j].is_bomb:
            grid[i][j]["image"] = mine
            grid[i][j]["state"] = "normal"
            utils.unbind_all_buttons(grid)
        elif board[i][j].bombs_around != 0:
            grid[i][j]["text"] = board[i][j].bombs_around
        else:
            for (x, y) in utils.neighbours(i, j):
                left_handler(board, grid, x, y, mine)


def right_handler(board, grid, i, j, flag):
    """ Called when right click on the (i, j) cell """
    if not board[i][j].revealed:
        if grid[i][j]["image"] == "":
            grid[i][j]["image"] = flag
            grid[i][j]["state"] = "normal"
            g.BOMBS_LEFT -= 1
        else:
            grid[i][j]["state"] = "disabled"
            grid[i][j]["image"] = ""
            g.BOMBS_LEFT += 1



