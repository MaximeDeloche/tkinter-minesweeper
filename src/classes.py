#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import utils
import tkinter as tk
   

class Square(tk.Frame):
    """ A square of the game """

    def __init__(self, x, y, master=None, cnf={}, **args):
        self.x = x
        self.y = y
        tk.Frame.__init__(self, master, cnf, **args)
        self.is_bomb = False
        self.marked_as_bomb = False
        self.revealed = False
        self.bombs_around = 0

        self.button = tk.Button(self, borderwidth=1, state="normal",
                                disabledforeground="#000000")
        self.button.pack(fill=tk.BOTH, expand=True)

        def __handler(event, x=self.x, y=self.y):
            return utils.handler(event, x, y)

        # left button binding
        self.button.bind("<Button-1>", __handler)
        # right button binding
        self.button.bind("<Button-3>", __handler)
 


    def reveal(self):
        self.revealed = True
        self["relief"] = tk.SUNKEN
        if self.is_bomb:
            self["state"] = "normal"
            self["image"] = mine
            # TODO : end game properly
            # it means : make the game unresponsive, without closing it
            # disable frames ? Unbind_all ? Raise error ?
        else:
            if self.number != 0:
                self["text"] = self.number


    def add_flag(self):
        return

    def remove_flag(self):
        return

    def add_bomb(self):
        return
            


        # -------->
        # |       y
        # |
        # V x


