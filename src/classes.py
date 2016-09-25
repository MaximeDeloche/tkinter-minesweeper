#! /usr/bin/env python3
# -*- coding: utf-8 -*-


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



        # -------->
        # |       y
        # |
        # V x


