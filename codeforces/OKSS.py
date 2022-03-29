# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:12:03 2021

@author: Kevin Chang

Project: Open Kattis Soda Slurper

"""

import sys

e, f, c = map(int, sys.stdin.readline().split())

pos = e + f
res = 0

while pos >= c:
    soda = pos//c
    pos = (pos%c) + soda
    res += soda

print(res)

print(sys.stdin.readline())