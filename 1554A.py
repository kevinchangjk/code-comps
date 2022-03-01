# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:58:00 2021

@author: Kevin Chang

Project: Codeforces Problem 1554A

"""

def pairprod(a):
    maxa = 0
    for i in range(n-1):
        product = a[i]*a[i+1]
        if product > maxa:
            maxa = product
    return maxa
    

for _ in range(int(input())):
    n =int(input())
    a = list(map(int, input().split()))
    print(pairprod(a))