# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 21:11:33 2021

@author: Kevin Chang

Project: Codeforces Problem 1541A

"""

for _ in range(int(input())):
    n = int(input())
    res = list(range(1, n+1))
    res = [i+1 if i%2 == 1 else i-1 for i in res]
    if len(res)%2== 1:
        res[-2] += 2
        res[-1] -= 3
    print(*res)