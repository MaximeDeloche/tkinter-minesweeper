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


def handler_test(x, y):
    print("click on ", x, y)

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


