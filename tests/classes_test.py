#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../src")

from classes import *

a = Grid(10, 7)
a.add_bombs(20)
print(a)
