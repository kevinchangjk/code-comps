from math import log

t = int(input())

for i in range(t):
    n = int(input())
    res = int(log(n, 10))+1
    print(res)