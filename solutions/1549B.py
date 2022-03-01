# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:48:24 2021

@author: Kevin Chang

Project: Codeforces Problem 1549B

"""

for _ in range(int(input())):
    n = int(input())
    en = list(map(int, input()))
    gr = list(map(int, input()))
    res = 0
    if gr[0] == 1:
        if en[0] == 0:
            res += 1
        elif en[1] == 1:
            res += 1
            en[1] = 2
        else:
            pass
        
    for i in range(1, n-1):
        if gr[i] == 0:
            continue
        else:
            if en[i] == 0:
                res += 1
                continue
            else:
                if en[i-1] == 1:
                    res += 1
                    en[i-1] = 2
                    continue
                elif en[i+1] == 1:
                    res += 1
                    en[i+1] = 2
                    continue
                else:
                    continue

    if gr[-1] == 1 and (en[-1] == 0 or en[-2] == 1):
        res += 1
    print(res)