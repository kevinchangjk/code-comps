import math

t = int(input())
res = []

for i in range(t):
    n, m, x = list(map(int, input().split()))
    
    xcd = (x // n)
    if x % n == 0:
        ycd = n
    else:
        ycd = x % n
        xcd +=1
    
    res.append(xcd + ((ycd-1) * m))
    
print(*res)
    