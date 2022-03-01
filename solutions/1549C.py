# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:46:15 2021

@author: Kevin Chang

Project: Codeforces Problem 1549C

"""

def add_edge(u, v):
    nobles[u].append(v)
    nobles[v].append(u)
    
def rem_edge(u, v):
    nobles[u].remove(v)
    nobles[v].remove(u)
    
def vuln(noble):
    for friend in nobles[noble]:
        if friend > noble:
            return 1
    return 0    
    
def proc():
    vulnerables = [vuln(j) for j in range(n)]
    return n-sum(vulnerables)

n, m = map(int, input().split())

nobles = [[] for i in range(n)]
    
for __ in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    add_edge(u, v)

q = int(input())
for ___ in range(q):
    query = input()
    if len(query) == 1:
        print(proc())
    else:
        if int(query[0]) == 1:
            add_edge(int(query[2])-1, int(query[4])-1)
        else:
            rem_edge(int(query[2])-1, int(query[4])-1)