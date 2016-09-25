#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes as cls
import random as rd
import tkinter as tk

import global_vars as g


def neighbours(i, j):
    """ Return the list of coordinates of the neighbours of the (i, j) cell"""
    l = []
    for (x, y) in [ (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i, j-1), (i, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(g.HEIGHT) and y in range(g.WIDTH):
            l.append((x, y))
    return l


def add_bombs(board):
    """ Fill board squares with bombs """
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


def unbind_all_buttons(grid):
    """ Make all squares unresponsive to click """
    # TODO improvable
    for i in range(g.HEIGHT):
        for j in range(g.WIDTH):
            grid[i][j]["state"] = "disabled"
            grid[i][j].unbind("<Button-1>")
            grid[i][j].unbind("<Button-3>")


def new_game():
    """ Called when click on New game """
    return
    # TODO
    # need to generate new board, new grid, reset counters...
    # change global variables and start gui program again ?

def options():
    """ Called when click on Options """
    return
    # TODO
    # set global variables for the next game, applied when new_game()

def disp_help():
    """ Called when click on Help """
    return
    # TODO
    # display a doc page on how to play

def reset_game(board, grid):
    for x in range(g.HEIGHT):
        for y in range(g.WIDTH):
            board[x][y].reset()
            grid[x][y]["image"] = ""
            grid[x][y]["text"] = ""
            grid[x][y]["state"] = "normal"
            grid[x][y]["relief"] = tk.RAISED
    add_bombs(board)



def print_board(board):
    """ Print the board in the shell (used for debugging) """
    for line in board:
        for elt in line:
            if elt.is_bomb:
                print(".", end="")
            else:
                print(elt.bombs_around, end="")
        print("")

