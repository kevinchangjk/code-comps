# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 21:27:34 2021

@author: Kevin Chang

Project: Codeforces Problem 1535B

"""

from itertools import combinations

def gcd(x, y):
    i = 2
    maxi = min(x, y)
    if x%i == 0 and y%i == 0:
        return 1
    else:
        i += 1
        while i <= maxi:    
            if x%i == 0 and y%i == 0:
                return 1
            else:
                i += 2
        return 0
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    even = [aa for aa in a if aa%2 == 0 ]
    odd = [aa for aa in a if aa%2 == 1]
    res = len(even)*len(odd)+((len(even)*(len(even)-1))//2)
    
    pairs = list(combinations(odd, 2))
    odd_res = sum([gcd(x, y) for (x, y) in pairs])
    
    print(res+odd_res)