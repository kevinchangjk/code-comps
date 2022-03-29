import time

n = int(input())

p = list(map(int, input().split()))

def opa(p):
    pp = [p[i + 1 - 2 * (i % 2)] for i in range(len(p))]
    return pp

def opb(p):
    n = len(p) // 2
    pp = p[n:]
    pp.extend(p[:n])
    return pp

goal = list(range(1, 2*n+1))

if p == goal:
    print(0)
    
else:
    runn = 0
    pa, pb = p, p
    
    while runn < n:
        pa, pb = opa(pb), opb(pa)
        runn += 1
        if pa == goal or pb == goal:
            print(runn)
            runn = n+1
    
    if runn == n:
        print(-1)
        
            