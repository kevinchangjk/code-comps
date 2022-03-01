# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:14:31 2021

@author: Kevin Chang

Project: Codeforces Problem {Contest+Question}

"""


def in_set(n, a, b):
    if n in [1, a, b+1]:
        return "YES"
    elif n % a == 0:
        if in_set(n//a, a, b) == "YES":
            return "YES"
    elif n > b:
        if in_set(n-b, a, b) == "YES":
            return "YES"
    else:
        return "NO"
    

t = int(input())

for i in range(t):
    n, a, b = list(map(int, input().split()))
    print(in_set(n, a, b))
