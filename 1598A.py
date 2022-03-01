# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:08:22 2021

@author: Kevin Chang

Project: Codeforces Problem 1598A

"""

for _ in range(int(input())):
    n = int(input())
    one = list(map(int, input()))
    two = list(map(int, input()))
    can = True
    
    for i in range(n):
        if one[i] == two[i] == 1:
            print("NO")
            can = False
            break
        else:
            continue
    if can:
        print("YES")