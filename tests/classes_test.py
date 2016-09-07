#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from src.classes import *

a = Grid(4, 2)
a.add_bombs(3)
print(a)
