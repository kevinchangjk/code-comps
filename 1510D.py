import math
import itertools

def prod(liss):
    res = 1
    i = 0
    while i < len(liss):
        res *= liss[i]
        i += 1
    return res

n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted([aa for aa in a if aa != 1])
n = len(a)
solva = 0
msum = prod(a)
if str(msum)[-1] == str(d):
    print(n)
    print(*a)
    
else:
    for i in range(1, n):
        if solva == 0:
            combs = list(itertools.combinations(a, i))
            ress = [str(msum // prod(comb))[-1] for comb in combs]
            for j in range(len(ress)):
                if ress[j] == str(d):
                    pops = [a.pop(a.index(combs[j][h])) for h in range(len(combs[j]))]
                    print(len(a))
                    print(*a)
                    solva = 1
                    break
                else:
                    continue
        else:
            break
            
    if solva == 0:
        print(-1)
