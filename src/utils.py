#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def neighbours(i, j):
    return [(i-1, j-1), (i-1, j), (i-1, j+1),
            (i, j-1), (i, j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1)]
        


