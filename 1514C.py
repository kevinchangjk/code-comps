from itertools import combinations

def prod(tup):
    res = 1
    for t in tup:
        res *= t
    return res

def facts(x):
    res = [dv for dv in range(2, x//2+1) if x%dv == 0]
    return res

n = int(input())

a = list(range(1, n))
a = [aa for aa in a if aa not in facts(n)]
solve = 1
i = 1

while solve == 1:
    combs = combinations(a, n-i)
    for comb in combs:
        if prod(comb)%n == 1:
            solve = 0
            resu = list(comb)
        else:
            continue
    i += 1

print(len(resu))
print(*resu)