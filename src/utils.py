#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes as cls
import random as rd
import tkinter as tk

import global_vars as g


def neighbours(i, j):
    l = []
    for (x, y) in [ (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i, j-1), (i, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(g.HEIGHT) and y in range(g.WIDTH):
            l.append((x, y))
    return l


def add_bombs(board):
    if g.BOMBS <= 0 or g.BOMBS >= g.WIDTH*g.HEIGHT:
        raise Exception("Invalid number of g.BOMBS.")
    else:
        # sample makes random choices with distinct elements
        # we don't want several g.BOMBS on the same square
        pos = rd.sample([(x, y) for x in range(g.HEIGHT) 
                                for y in range (g.WIDTH)], g.BOMBS)

        for (i, j) in pos:
            board[i][j].is_bomb = True
            for (x, y) in neighbours(i, j):
                board[x][y].bombs_around += 1


# Event handlers ###############################################################

def left_handler(board, grid, i, j, mine):
    if grid[i][j]["image"] == "" and not board[i][j].revealed:
        board[i][j].revealed = True
        grid[i][j]["state"] = "disabled"
        grid[i][j]["relief"] = tk.SUNKEN
        if board[i][j].is_bomb:
            grid[i][j]["image"] = mine
            grid[i][j]["state"] = "normal"
            unbind_all_buttons(grid)
        elif board[i][j].bombs_around != 0:
            grid[i][j]["text"] = board[i][j].bombs_around
        else:
            for (x, y) in neighbours(i, j):
                left_handler(board, grid, x, y, mine)


def right_handler(board, grid, i, j, flag):
    if not board[i][j].revealed:
        if grid[i][j]["image"] == "":
            grid[i][j]["image"] = flag
            grid[i][j]["state"] = "normal"
            g.BOMBS_LEFT -= 1
        else:
            grid[i][j]["state"] = "disabled"
            grid[i][j]["image"] = ""
            g.BOMBS_LEFT += 1



def unbind_all_buttons(grid):
    for i in range(g.HEIGHT):
        for j in range(g.WIDTH):
            grid[i][j]["state"] = "disabled"
            grid[i][j].unbind("<Button-1>")
            grid[i][j].unbind("<Button-3>")


def print_board(board):
    for line in board:
        for elt in line:
            if elt.is_bomb:
                print(".", end="")
            else:
                print(elt.bombs_around, end="")
        print("")

