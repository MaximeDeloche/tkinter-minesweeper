#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def neighbours(i, j, height, width):
    l = []
    for (x, y) in [(i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1), (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)]:
        if x in range(height) and y in range(width):
            l.append((x, y))
    
    return l
            
 
