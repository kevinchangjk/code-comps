# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:46:54 2021

@author: Kevin Chang

Project: Codeforces Problem 1557A

"""

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    maxi = a.index(max(a))
    b = a.pop(maxi)
    print(b+sum(a)/(n-1))