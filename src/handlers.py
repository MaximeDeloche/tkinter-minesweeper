#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as tkmsg
import sys
import time

import global_vars as g
import utils

# Event handlers ###############################################################

def left_handler(grid, board, i, j, mine):
    """ Called when left click on the (i, j) cell """
    if board[i][j]["image"] == "" and not grid.tab[i][j].revealed:
        board[i][j]["state"] = "disabled"
        board[i][j]["relief"] = tk.SUNKEN
        if grid.tab[i][j].is_bomb:
            board[i][j]["image"] = mine
            board[i][j]["state"] = "normal"
            end_game(False, grid, board)
        else:
            grid.tab[i][j].revealed = True
            g.SQUARES_REVEALED += 1
            if grid.tab[i][j].bombs_around != 0:
                board[i][j]["text"] = grid.tab[i][j].bombs_around
            else:
                for (x, y) in utils.neighbours(i, j):
                    left_handler(grid, board, x, y, mine)
            if g.SQUARES_REVEALED == (g.WIDTH * g.HEIGHT - g.BOMBS):
                end_game(True, grid, board)


def right_handler(grid, board, i, j, flag):
    """ Called when right click on the (i, j) cell """
    if not grid.tab[i][j].revealed:
        if board[i][j]["image"] == "":
            board[i][j]["image"] = flag
            board[i][j]["state"] = "normal"
            g.BOMBS_LEFT -= 1
        else:
            board[i][j]["state"] = "disabled"
            board[i][j]["image"] = ""
            g.BOMBS_LEFT += 1


def end_game(win, grid, board):
    if win:
        title = "You won !"
        msg = "Good job. Play again ?"
    else:
        title = "You lost..."
        msg = "Try again ?"
    ans = tkmsg.askyesno(title, msg)
    if ans:
        start_new_game(grid, board)
    else:
        sys.exit()


def start_new_game(grid, board):
    if  g.HEIGHT == g.NEXT_HEIGHT and # if options hasn't changed
        g.WIDTH == g.NEXT_WIDTH and
        g.BOMBS == g.NEXT_BOMBS:

        for x in range(g.HEIGHT):
            for y in range(g.WIDTH):
                grid.tab[x][y].reset()
                board[x][y]["image"] = ""
                board[x][y]["text"] = ""
                board[x][y]["state"] = tk.DISABLED
                board[x][y]["relief"] = tk.RAISED
        grid.add_bombs()
        g.SQUARES_REVEALED = 0
        g.BOMBS_LEFT = g.BOMBS
        g.INIT_TIME = time.time()
        grid.disp()

    else: # if options has changed
        return;
        g.HEIGHT = g.NEXT_HEIGHT
        g.WIDTH = g.NEXT_WIDTH
        g.BOMBS = g.NEXT_BOMBS
        grid.add_bombs()

