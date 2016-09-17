#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes as cls
import random as rd


def neighbours(i, j, height_max, width_max):
    l = []
    for (x, y) in [ (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i, j-1), (i, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(height_max) and y in range(width_max):
            l.append((x, y))
    return l


def add_bombs(squares, bombs, w, h):
    if bombs <= 0 or bombs >= w * h:
        raise Exception("Invalid number of bombs.")
    else:
        # sample makes random choices with distinct elements
        # we don't want several bombs on the same square
        pos = rd.sample([(x, y) for x in range(h) for y in range (w)], bombs)

        for (i, j) in pos:
            squares[i][j].is_bomb = True
            for (x, y) in neighbours(i, j, h, w):
                squares[x][y].bombs_around += 1


# Event handlers ###############################################################
def handler(event, x, y):
    if event.num == 1:
        left_handler(x, y)
    elif event.num == 3:
        right_handler(x, y)
    else:
        raise Exception('Invalid event code.')


def left_handler(i, j):
    if squares[i][j]["image"] =="" and not self.squares[i][j].revealed:
        squares[i][j].reveal()
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
        else:
            event.widget["state"] = "disabled"
            event.widget["image"] = ""
            event.widget.marked_as_bomb = False
            self.bombs_left += 1
        print("Bombs left = ", self.bombs_left)



#
#
# def __str__(self):
#     res = ""
#     for i in range(self.height):
#         for j in range(self.width):
#             if self.squares[i][j].is_bomb:
#                 res += "."
#             else:
#                 res += str(self.squares[i][j].number)
#         res += "\n"
#     return res


