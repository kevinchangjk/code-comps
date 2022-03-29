# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:02:51 2021

@author: Kevin Chang

Project: Codeforces Problem 1542A

"""

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    is_odd = [1 for ai in a if ai%2 == 1]
    if sum(is_odd) == n:
        print("YES")
    else:
        print("NO")
