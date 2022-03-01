# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:53:19 2021

@author: Kevin Chang

Project: Codeforces Problem 1554B

"""

def cobb(x, y):
    return x*y-k*(x^y)

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    for i in range(n):
        for j in range(1, n):
            print(cobb(a[i], a[j]))
    