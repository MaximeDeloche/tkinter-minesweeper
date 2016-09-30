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

# def options():
#     """ Called when click on Options """
#     return
#     # TODO
#     # set global variables for the next game, applied when new_game()
#
# def disp_help():
#     """ Called when click on Help """
#     return
#     # TODO
#     # display a doc page on how to play


