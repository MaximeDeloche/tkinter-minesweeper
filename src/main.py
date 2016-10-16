#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import time

import classes as cls
import gui
import global_vars as g


# Initialisation of the data ###################################################
GRID = cls.Grid()
GRID.add_bombs()
GRID.disp()

# Creation of the GUI ##########################################################
window = gui.create_main_window()
flag, mine = gui.create_images()
BOARD = gui.create_board(window, GRID, flag, mine)
top_frame = gui.create_top_frame(window, GRID, BOARD)

# new idea
# window = gui.create_main_window()
# flag, mine = gui.create_images()
#  create_new_game (window, flag, mine)
# New Game Button would call 'create_new_game'

tk.mainloop()
