# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:18:10 2021

@author: Kevin Chang

Project: Codeforces Problem 1598B

"""

for _ in range(int(input())):
    can = False
    n = int(input())
    half = n//2
    student = []
    for i in range(n):
        student.append(list(map(int, input().split())))
    
    days = [[j for j in range(n) if student[j][i] == 1] for i in range(5)]
    possible = [i for i in range(5) if len(days[i]) >= half]
    
    for da in possible:
        if can:
            break
        else:
            for db in possible:
                if da == db:
                    continue
                elif len(set(days[da]+days[db])) == n:
                    print("YES")
                    can = True
                    break
                else:
                    continue
    if not can:
        print("NO")
            