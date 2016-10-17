#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import sys

import classes as cls
import gui
import utils

# Set parameters if given ######################################################
utils.set_parameters(sys.argv[1:])

# Initialisation of the data ###################################################
GRID = cls.Grid()
GRID.add_bombs()

# Creation of the GUI ##########################################################
window = gui.create_main_window()
flag, mine = gui.create_images()
BOARD = gui.create_board(window, GRID, flag, mine)
top_frame = gui.create_top_frame(window, GRID, BOARD)

tk.mainloop()
