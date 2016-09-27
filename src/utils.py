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

# def unbind_all_buttons(grid):
#     """ Make all squares unresponsive to click """
#     # TODO improvable
#     for i in range(g.HEIGHT):
#         for j in range(g.WIDTH):
#             grid[i][j]["state"] = "disabled"
#             grid[i][j].unbind("<Button-1>")
#             grid[i][j].unbind("<Button-3>")
#

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
#
# def reset_game(board, grid):
#     for x in range(g.HEIGHT):
#         for y in range(g.WIDTH):
#             board[x][y].reset()
#             grid[x][y]["image"] = ""
#             grid[x][y]["text"] = ""
#             grid[x][y]["state"] = "normal"
#             grid[x][y]["relief"] = tk.RAISED
#     add_bombs(board)
#     print("\n")
#     print_board(board)
#
#
# def end_game(win, grid):
#     if win:
#         ans = tkmsg.askyesno("You won !", "Your name $username and your \
#         time $time are registered. High scores : $high_scores. \
#         \n\n Play again ?")
#     else:
#         ans = tkmsg.askyesno("You lost...", "High scores : $high_scores. \
#         \n\n Play again ?")
#
#     if ans:
#         return
#         # TODO : start game again => no idea how to do it
#     else:
#         sys.exit()
#

