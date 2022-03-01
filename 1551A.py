# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 22:36:33 2021

@author: Kevin Chang

Project: Codeforces Problem 1551A

"""

for i in range(int(input())):
    n = int(input())
    b = n//3
    if n%3 == 2:
        a = b
        b += 1
    else:
        a = b + n%3
    print(f"{a} {b}")