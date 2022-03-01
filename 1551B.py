# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 22:46:32 2021

@author: Kevin Chang

Project: Codeforces Problem 1551B

"""

for i in range(int(input())):
    s = input()
    painted = []
    for ss in s:
        if ss not in painted:
            painted.append(ss)
        elif ss in painted:
            sss = ss + ss
            if sss not in painted:
                painted.append(sss)
            else:
                continue
    print(len(painted)//2)