# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 01:10:46 2021

@author: Kevin Chang

Project: Codeforces Problem 799A

"""

import math

n, t, k, d = map(int, input().split())

cycles = math.ceil(n/k)

if cycles == 1 or (d/t >= cycles-1):
    print("NO")

else:
    print("YES")
    