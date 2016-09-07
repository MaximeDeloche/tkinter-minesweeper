#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes
from tkinter import *

# main window
window = Tk()

# title of the game
title = Label(window, text="Minesweeper")
title.pack(side="top")

# frame in which the buttons will be displayed
frame = Frame(window, borderwidth=10)
frame.pack(fill=BOTH)
button = Button(frame, command=window.quit)
button.pack()
window.mainloop()
