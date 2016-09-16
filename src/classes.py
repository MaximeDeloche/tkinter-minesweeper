#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import utils
import tkinter as tk
   
# images
flag = tk.PhotoImage(file="red_flag.gif")
mine = tk.PhotoImage(file="mine.gif")

# class TopFrame(tvk.Frame):
#     """ The top frame displaying the number of bombs left and the time """
#     def __init__



class Square(tk.Button):
    """ A square of the game """

    def __init__(self, master=None, cnf={}, **args):
        tk.Button.__init__(self, master, cnf, **args)
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
            


class Grid(tk.Frame):
    """ A grid of the game, containing Squares """

    def __init__(self, master=None, cnf={}, **args):
        tk.Frame.__init__(self, master, cnf, **args)
        self.height = 0
        self.width = 0
        self.bombs = 0
        self.bombs_left = 0
        self.squares = list()

        # create a list of list of Squares
        # -------->
        # |       y
        # |
        # V x

    def __left_handler(self, event, i, j):
        if self.squares[i][j]["image"] =="" and not self.squares[i][j].revealed:
            self.squares[i][j].reveal()
            if self.squares[i][j].number == 0:
                for (x, y) in utils.neighbours(i, j, self.height, self.width):
                    self.__left_handler(event, x, y)
                            

    def __right_handler(self, event):
        if not event.widget.revealed:
            if event.widget["image"] == "":
                event.widget["state"] = "normal"
                event.widget["image"] = flag
                event.widget.marked_as_bomb = True
                self.bombs_left -= 1
                print("Bombs left = ", self.bombs_left)
            else:
                event.widget["state"] = "disabled"
                event.widget["image"] = ""
                event.widget.marked_as_bomb = False
                self.bombs_left += 1
                print("Bombs left = ", self.bombs_left)



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
                def left_handler(event, row=i, column=j):
                    return self.__left_handler(event, row, column)
                sq.bind("<Button-1>", left_handler)
                sq.bind("<Button-3>", self.__right_handler)

                row.append(sq)

            self.squares.append(row)




    def add_bombs(self, bombs):
        if bombs <= 0 or bombs >= self.width * self.height:
            raise Exception("Invalid number of bombs.")
        else:
            self.bombs = bombs
            self.bombs_left = bombs
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


