#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

game_modes = [  ("Easy", 10, 10, 20),
                ("Normal", 15, 20, 40),
                ("Hard", 20, 30, 80)]

def start_options_window():
    """ Display options window and update global variables """
    options_window = tk.Tk()
    options_window['bg'] = 'white'
    options_window.resizable(width=False, height=False)

    # choices
    choice = tk.IntVar()
    create_choices(options_window, choice)

    # validation button
    create_OK_button(options_window, choice)

    # launch window
    options_window.mainloop()


def create_choices(window, choice):
    for i in range(len(game_modes)):
        tk.Radiobutton( window, text = game_modes[i],
                        variable = choice, value = i).pack()


def create_OK_button(window, choice):
    def valid_changes():
        set_new_values(game_modes[choice.get()], window)
    tk.Button(  window, borderwidth=1, 
                text="OK", command=valid_changes).pack()


def set_new_values(mode, window):
    print("Mode ", mode[0])
    print("Height : ", mode[1])
    print("Width : ", mode[2])
    print("Bombs : ", mode[3])
    window.destroy()


start_options_window()
