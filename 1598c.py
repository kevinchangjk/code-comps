# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:50:33 2021

@author: Kevin Chang

Project: Codeforces Problem 1598C

"""

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = sum(a)/len(a)
    if int(k*2) != k*2:
        print(0)
    else:
        a = sorted(a)
        count = Counter(a)
        counted = a[-1]+1
        res = 0
        for key in count:
            target = int(k*2)-key
            if key >= counted:
                break
            elif target == key:
                amt = count[key]
                res += (amt*(amt-1)//2)
                break
            elif target in count:
                res += count[key]*count[target]
                counted = target
            else:
                continue
        print(res)