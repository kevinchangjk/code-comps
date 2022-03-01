# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:15:37 2021

@author: Kevin Chang

Project: Codeforces Problem 1557B

"""

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    non_desc = 0
    for i in range(1, n):
        if a[i] >= a[i-1]:
            non_desc += 1
        else:
            continue
    print("NYOE S"[non_desc>=(n-k)::2])