# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 17:29:39 2021

@author: Kevin Chang

Project: Codeforces Problem 455A

"""

from collections import Counter

def adamake(n):
    res = [ad[n], ad[n]*n, ad[n]*n-ad[n-1]*(n-1)-ad[n+1]*(n+1)]
    return res

n = int(input())

a = list(map(int, input().split()))
a.sort()
ad = Counter(a)
ada = ad.copy()
for n in ad:
    ada[n] = adamake(n)

solving = 1
while solving:
    if ada.keys(1) == ada.keys(0)+1:
        if ada[ada.keys(0)][2] > ada[ada.keys(1)][2]:
            del(ada[ada.keys(1)])
            res += ada[ada.keys(0)][1]
        else:
            
        