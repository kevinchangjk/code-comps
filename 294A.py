# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 01:19:07 2021

@author: Kevin Chang

Project: Codeforces Problem 294A

"""

n = int(input())
a = list(map(int, input().split()))
m = int(input())

def shoot(a):
    x, y = map(int, input().split())
    if x > 1:
        a[x-2] += y-1
    if x < len(a):
        a[x] += a[x-1]-y
    a[x-1] = 0
    return a        

for _ in range(m):
    a = shoot(a)

print("\n".join(list(map(str, a))))