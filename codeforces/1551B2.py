# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 23:00:30 2021

@author: Kevin Chang

Project: Codeforces Problem 1551B2

"""


def paint(ind):
    taken = count[a[ind]]
    choices = [i for i in range(1, k+1) if i not in taken]
    choices_count = [colours[i-1] for i in choices]
    paint = choices[choices_count.index(min(choices_count))]
    res[ind] = (paint)
    colours[paint-1] += 1
    count[a[ind]].append(paint)
    
def unpaint():
    paint = colours.index(max(colours))
    target = res.index(paint+1)
    res[target] = 0
    colours[paint] -= 1

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    count = {0:0,}
    res = [0 for i in range(n)]
    colours = [0 for i in range(k)]
    
    for i in range(n):
        if a[i] in count:
            if len(count[a[i]]) < k:
                paint(i)
            else:
                continue
        else:
            count[a[i]] = []
            paint(i)
    """
    while max(colours)-min(colours) > 0:
        unpaint()
    """
    print(*res)