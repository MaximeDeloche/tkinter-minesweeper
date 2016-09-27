#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import utils
import global_vars as g

class Square():
    """ A square of the game """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def reset(self):
        self.is_bomb = False
        # self.marked_as_bomb = False
        self.revealed = False
        self.bombs_around = 0

    def reveal(self):
        self.revealed = True
        return (self.is_bomb, self.bombs_around)

        # -------->
        # |       y
        # |
        # V x


class Grid():
    """ A game grid, containing Squares """
    def __init__(self):
        self.tab = [[Square(i, j)   for j in range(g.WIDTH)]
                                    for i in range(g.HEIGHT)]

    def reset(self):
        for line in self.tab:
            for sq in line:
                sq.reset()

    def add_bombs(self):
        """ Fill board squares with bombs """
        if g.BOMBS <= 0 or g.BOMBS >= g.HEIGHT*g.WIDTH:
            raise Exception("Invalid number of g.BOMBS.")
        else:
            # sample makes random choices with distinct elements
            # we don't want several bombs on the same square
            pos = random.sample([(i, j) for j in range(g.WIDTH) 
                                        for i in range (g.HEIGHT)], g.BOMBS)
            for (i, j) in pos:
                self.tab[i][j].is_bomb = True
                for (i2, j2) in utils.neighbours(i, j):
                    self.tab[i2][j2].bombs_around += 1

    def disp(self):
        """ Display grid in the terminal / useful for debugging """
        for line in self.tab:
            for sq in line:
                if sq.is_bomb:
                    print('.', end='')
                else:
                    print(sq.bombs_around, end='')
            print()



