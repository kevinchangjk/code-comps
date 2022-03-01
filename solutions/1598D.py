# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:44:24 2021

@author: Kevin Chang

Project: Codeforces Problem 1598D

"""

from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    combi = combinations(range(n), 3)
    count = 0
    for inds in combi:
        aa = [a[i] for i in inds]
        bb = [b[i] for i in inds]
        if len(set(aa)) == 3 or len(set(bb)) == 3:
            count += 1
        else:
            continue
    print(count)