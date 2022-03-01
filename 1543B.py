# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:51:26 2021

@author: Kevin Chang

Project: Codeforces Problem 1543B

"""

t = int(input())

for i in range(t):
    n = int(input())    
    a = list(map(int, input().split()))
    suma = sum(a)
    extras = suma%n
    print(extras*(n-extras))