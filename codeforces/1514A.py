from itertools import combinations

t = int(input())

def prod(tup):
    res = 1
    for t in tup:
        res *= t
    return res

def psq(num):
    sqr = num**0.5
    if int(sqr) - sqr == 0:
        return 1
    else:
        return 0

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [aa for aa in a if not psq(aa)]
    j = 1
    solve = 1
    
    while solve and j <= n:
        combs = combinations(a, j)
        for comb in combs:
            pd = prod(comb)
            if not psq(pd):
                solve = 0
                break
            else:
                continue
        j += 1
    
    if solve == 1:
        print("NO")
    else:
        print("YES")
    