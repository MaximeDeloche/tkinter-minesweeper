#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import classes as cls

# useful functions
def neighbours(i, j, height, width):
    l = []
    for (x, y) in [(i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1), (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(height) and y in range(width):
            l.append((x, y))
    
    return l
            



# def add_bombs(self, bombs):
#     if bombs <= 0 or bombs >= self.width * self.height:
#         raise Exception("Invalid number of bombs.")
#     else:
#         self.bombs = bombs
#         self.bombs_left = bombs
#         # sample makes random choices with distinct elements
#         # we don't want several bombs on the same square
#         pos = random.sample([(x, y) 
#             for x in range(self.height) 
#             for y in range (self.width)], bombs)
#
#         for (i, j) in pos:
#             self.squares[i][j].is_bomb = True
#             for (x, y) in utils.neighbours(i, j, self.height, self.width):
#                 self.squares[x][y].number += 1
#
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


