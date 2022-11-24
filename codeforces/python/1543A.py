# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:28:31 2021

@author: Kevin Chang

Project: Codeforces Problem 1543A

"""

t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))
    diff = max([a, b])-min([a, b])
    if diff == 0:
        mm = 0
    else:
        minab = min([a, b])
        mm = min([diff-minab%diff, minab%diff])
    print(diff, mm)
