from math import log

t = int(input())
for i in range(t):
    l, r = list(map(int, input().split()))
    if str(r)[-1] == "0":
        res = int(log(r))