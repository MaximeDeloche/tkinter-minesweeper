#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# import sys
# import tkinter as tk
# import tkinter.messagebox as tkmsg

import global_vars as g
# import classes as cls


def neighbours(i, j):
    """ Return the list of coordinates of the neighbours of the (i, j) cell"""
    l = []
    for (x, y) in [ (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i, j-1), (i, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(g.HEIGHT) and y in range(g.WIDTH):
            l.append((x, y))
    return l


def set_parameters(argv):
    # if there's not 3 args
    if len(argv) != 3:
        if len(argv) != 0:
            print("Warning : Invalid parameters")
            print("Need 3 arguments (height, width, bombs)")
        return

    # if they aren't ints
    try:
        height = int(argv[0])
        width = int(argv[1])
        bombs = int(argv[2])
    except ValueError:
        print("Warning : Invalid parameters")
        print("Arguments aren't ints")
        return

    # if constraints aren't respected
    if  height <= 0 or width <= 0 or bombs <= 0 or bombs >= height*width:
        print("Warning : Invalid parameters")
        print("Can't create game with these values")
        return

    g.HEIGHT = height
    g.WIDTH = width
    g.BOMBS = bombs
    g.BOMBS_LEFT = bombs
