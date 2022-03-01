# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:26:09 2021

@author: Kevin Chang

Project: Codeforces Problem 476C

"""

a, b = list(map(int, input().split()))
modu = 10**9+7

#res = (b*(b-1)//2)*((b*a*(a+1)//2)+a)%modu
#print(res)

res = (a*b*(b-1))/2 + (a*(a+1)*b*b*(b-1))/4
print(int(res % modu))