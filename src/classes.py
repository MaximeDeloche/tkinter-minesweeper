#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import utils
import tkinter as tk
   


class Square(tk.Frame):
    """ A square of the game """

    def __init__(self, master=None, cnf={}, **args):
        tk.Frame.__init__(self, master, cnf, **args)
        self.button = tk.Button(self, borderwidth=1, state="disabled",
                                disabledforeground="#000000")
        self.button.pack(fill=tk.BOTH, expand=True)
        self.is_bomb = False
        self.marked_as_bomb = False
        self.revealed = False
        self.number = 0


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
            


        # -------->
        # |       y
        # |
        # V x


