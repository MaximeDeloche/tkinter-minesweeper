#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports ######################################################################
import tkinter as tk
import tkinter.font as tkf
import time

import classes as cls
import utils
import handlers
import global_vars as g


# Main unresizable window ######################################################
def create_main_window():
    window = tk.Tk()
    window['bg'] = 'white'
    window.resizable(width=False, height=False)
    return window


# Images #######################################################################
def create_images():
    flag = tk.PhotoImage(file="images/red_flag.gif")
    mine = tk.PhotoImage(file="images/mine.gif")
    return (flag, mine)



# Game frame ###################################################################
def create_board(window, flag, mine):
    game_frame = tk.Frame(window, borderwidth=2, relief=tk.SUNKEN)

    def create_square(i, j):
        f = tk.Frame(game_frame, height=30, width=30)
        s = tk.Button(f, borderwidth=1, state="normal",
                        disabledforeground="#000000")
        s.pack(fill=tk.BOTH, expand=True)

        # buttons bindings
        def __handler(event, x=i, y=j):
            if event.num == 1:
                handlers.left_handler()
            elif event.num == 3:
                handlers.right_handler()
            else:
                raise Exception('Invalid event code.')
        s.bind("<Button-1>", __handler)
        s.bind("<Button-3>", __handler)

        f.pack_propagate(False)
        f.grid(row=i, column=j)
        return s

    BOARD = [[create_square(i, j)   for j in range(g.WIDTH)] 
                                    for i in range(g.HEIGHT)]
    game_frame.pack(padx=10, pady=10, side=tk.BOTTOM)
    return BOARD


# Top frame ####################################################################

def create_top_frame(window):
    top_frame = tk.Frame(window, borderwidth=2, height=40, relief=tk.GROOVE)
    top_frame.pack(padx=0, pady=0, side=tk.TOP, fill="x")
    for i in range(5):
        top_frame.columnconfigure(i, weight=1)
    create_bombs_counter(top_frame)
    create_new_game_button(top_frame)
    create_options_button(top_frame)
    create_help_button(top_frame)
    create_time_counter(top_frame)
    return top_frame

def create_bombs_counter(top_frame):
    """ bombs_counter, left """
    bombs_counter_str = tk.StringVar()
    bombs_counter_str.set(g.BOMBS_LEFT)
    bombs_counter = tk.Label(   top_frame, height=1, width=4, bg='white', 
                                textvariable=bombs_counter_str, 
                                font=tkf.Font(weight='bold', size=10))
    bombs_counter.grid(row=0, column=0, padx=5, sticky=tk.W)


def create_new_game_button(top_frame):
    """ new game button, middle left """
    newgame_button = tk.Button( top_frame, bd=1, text="New game",
                                command='')
    newgame_button.grid(row=0, column=1, padx=0, sticky=tk.E)


def create_options_button(top_frame):
    """ options button, middle """
    options_button = tk.Button( top_frame, bd=1, text="Options",
                                command='')
    options_button.grid(row=0, column=2, padx=0)


def create_help_button(top_frame):
    """ help button, middle right """
    help_button = tk.Button(top_frame, bd=1, text="Help", 
                            command='')
    help_button.grid(row=0, column=3, padx=0, sticky=tk.W)


def create_time_counter(top_frame):
    """ time counter, right """
    time_counter_str = tk.StringVar()
    time_counter = tk.Label(top_frame, height=1, width=4, bg='white',
                            textvariable=time_counter_str,
                            font=tkf.Font(slant='italic', size=10))
    time_counter.grid(row=0, column=4, padx=5, sticky=tk.E)


# def update_time():
#     time_counter_str.set(int((time.time()-init_time)//1))
#     time_counter.after(100, update_time)
#
# init_time = time.time()
# update_time()
