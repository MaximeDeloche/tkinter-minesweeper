#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import utils
import tkinter as tk
   
# images
flag = tk.PhotoImage(file="red_flag.gif")
mine = tk.PhotoImage(file="mine.gif")

class Square(tk.Button):
    """ A square of the game """

    def __init__(self, master=None, cnf={}, **args):
        tk.Button.__init__(self, master, cnf, **args)
        self.is_bomb = False
        self.revealed = False
        self.number = 0

    def __left_handler(self, event, row, column, height, width):
        if event.widget["image"] == "" and not self.revealed:
            self.revealed = True
            event.widget["relief"] = tk.SUNKEN
            if self.is_bomb:
                event.widget["state"] = "normal"
                event.widget["image"] = mine
                # TODO : end game properly
                # it means : make the game unresponsive, without closing it
                # disable frames ? Unbind_all ?
            else:
                event.widget["text"] = self.number
                if self.number == 0:
                    print("Need to discover neighbours")
                    # for (x, y) in utils.neighbours(row, column, height, width):
                        # if not 
                    # it has to discover all neighbours
                    # + same recursively if neighbours are zero
                    # therefore needs the position of the pressed event
                    # then access with grid.squares
                    # CROSS THE FINGERS, IT WILL FUCKIN WORK


    def right_handler(self, event):
        if not self.revealed:
            if event.widget["image"] == "":
                event.widget["state"] = "normal"
                event.widget["image"] = flag
                print("flag added")
            else:
                event.widget["state"] = "disabled"
                event.widget["image"] = ""
                print("flag removed")


class Grid(tk.Frame):
    """ A grid of the game, containing Squares """

    def __init__(self, master=None, cnf={}, **args):
        tk.Frame.__init__(self, master, cnf, **args)
        self.height = 0
        self.width = 0
        self.bombs = 0
        self.squares = list()

        # create a list of list of Squares
        # -------->
        # |       y
        # |
        # V x



    def fill(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            row = list()
            for j in range(width):
                f = tk.Frame(self, height=25, width=25)
                f.pack_propagate(False)
                f.grid_propagate(False)
                f.grid(row=i, column=j)
                sq = Square(f, borderwidth=1, state="disabled",
                            disabledforeground="#000000")
                sq.pack(fill=tk.BOTH, expand=True)
                # bind mouse clicks with actions
                def left_handler(event, row=i, column=j, h=height, w=width):
                    return sq.__left_handler(event, row, column, h, w)
                # def right_handler(event, row=i, column=j):
                #     return __right_handler(event, row, column)
                sq.bind("<Button-1>", left_handler)
                sq.bind("<Button-3>", sq.right_handler)

                row.append(sq)

            self.squares.append(row)




    def add_bombs(self, bombs):
        if bombs <= 0 or bombs >= self.width * self.height:
            raise Exception("Invalid number of bombs.")
        else:
            self.bombs = bombs
            # sample makes random choices with distinct elements
            # we don't want several bombs on the same square
            pos = random.sample([(x, y) 
                for x in range(self.height) 
                for y in range (self.width)], bombs)

            for (i, j) in pos:
                self.squares[i][j].is_bomb = True
                for (x, y) in utils.neighbours(i, j, self.height, self.width):
                    self.squares[x][y].number += 1



    def __str__(self):
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                if self.squares[i][j].is_bomb:
                    res += "."
                else:
                    res += str(self.squares[i][j].number)
            res += "\n"
        return res


